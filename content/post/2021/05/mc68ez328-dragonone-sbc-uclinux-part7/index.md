---
title: "MC68EZ328 DragonOne SBCでuClinuxを動かす(7) ～rootにmountする～"
date: 2021-05-25
slug: "mc68ez328-dragonone-sbc-uclinux-part7"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/mc68ez328_dragonone_sbc_uclinux_part7_mount_root_msg2.png"
---

前回に続いて[initから呼び出されるprepare\_namespace()](https://kanpapa.com/2021/05/mc68ez328-dragonone-sbc-uclinux-part6.html "MC68EZ328 DragonOne SBCでuClinuxを動かす(6) ～initスレッドを追う～")を探ってみます。

### prepare\_namespace()

ここから先は慎重にみていきます。 ソースはそんなに長くありません。（不要な部分は削っています）

```
/*
* Prepare the namespace - decide what/where to mount, load ramdisks, etc.
*/
void prepare_namespace(void)
{
int is_floppy = MAJOR(ROOT_DEV) == FLOPPY_MAJOR;
sys_mkdir("/dev", 0700);
sys_mkdir("/root", 0700);
sys_mknod("/dev/console", S_IFCHR|0600, MKDEV(TTYAUX_MAJOR, 1));
create_dev("/dev/root", ROOT_DEV, NULL);
if (mount_initrd) {
if (initrd_load() && ROOT_DEV != MKDEV(RAMDISK_MAJOR, 0)) {
handle_initrd();
goto out;
}
} else if (is_floppy && rd_doload && rd_load_disk(0))
ROOT_DEV = MKDEV(RAMDISK_MAJOR, 0);
mount_root();
out:
sys_umount("/dev", 0);
sys_mount(".", "/", NULL, MS_MOVE, NULL);
sys_chroot(".");
mount_devfs_fs ();
}

```

最初に/dev, /rootのディレクトリを作ります。その次は/dev/consoleのデバイスファイルを作ります。TTYAUX\_MAJORは5なので、MAJOR=5, MINOR=1のデバイスファイルです。

ここでUbuntuで試しにmountしたromfsの/dev/consoleをみてみると、MAJOR=5, MINOR=1となっていたので一致しています。

![mc68ez328_dragonone_sbc_uclinux_part7_dev_console.png](images/mc68ez328_dragonone_sbc_uclinux_part7_dev_console.png)
<!--more-->

### create\_dev()

次にcreate\_dev()で/dev/rootのデバイスファイルを作ります。この関数はinit/do\_mount.cにあります。

```
static int __init create_dev(char *name, kdev_t dev, char *devfs_name)
{
void *handle;
char path[64];
int n;
sys_unlink(name);
if (!do_devfs)
return sys_mknod(name, S_IFBLK|0600, kdev_t_to_nr(dev));
　：
}
```

ここでは、DEVFSは使用しない設定になっているので、do\_devfsはFALSEです。そのため、sys\_mknodで/dev/rootのデバイスファイルを作るだけで、prepare\_namespace()にもどります。

prepare\_namespace()にもどったあと、mount\_initrdの部分やフロッピィディスクの部分は該当しないので素通りして、続いての関数はmount\_root()になります。

### mount\_root()

まさにここでrootディレクトリがmountされるのでしょうか。関数をみてみます。

```
static void __init mount_root(void)
{
devfs_make_root(root_device_name);
create_dev("/dev/root", ROOT_DEV, root_device_name);
mount_block_root("/dev/root", root_mountflags);
}
```

たった３行しかありません。しかもdevfsは使わないので、devfs\_make\_root()はそのままリターンで戻ってきます。次に再びcreate\_dev()です。さっきも実行したのですが、今度はroot\_device\_nameに値が入っています。しかし、devfsは使わないのでこの情報は特に使われず、/dev/rootをunlinkしたあとにsys\_mknod()が行われ、再び/dev/rootのデバイスファイルができます。

### mount\_block\_root()

次の関数はmount\_block\_root()です。この関数をみてみます。

```
static void __init mount_block_root(char *name, int flags)
{
char *fs_names = __getname();
char *p;
get_fs_names(fs_names);
retry:
for (p = fs_names; *p; p += strlen(p)+1) {
int err = sys_mount(name, "/root", p, flags, root_mount_data);
switch (err) {
case 0:
goto out;
case -EACCES:
flags |= MS_RDONLY;
goto retry;
case -EINVAL:
case -EBUSY:
continue;
}
/*
* Allow the user to distinguish between failed open
* and bad superblock on root device.
*/
printk ("VFS: Cannot open root device \"%s\" or %s\n",
root_device_name, kdevname (ROOT_DEV));
printk ("Please append a correct \"root=\" boot option\n");
panic("VFS: Unable to mount root fs on %s",
kdevname(ROOT_DEV));
}
panic("VFS: Unable to mount root fs on %s", kdevname(ROOT_DEV));
out:
putname(fs_names);
sys_chdir("/root");
ROOT_DEV = current->fs->pwdmnt->mnt_sb->s_dev;
printk("VFS: Mounted root (%s filesystem)%s.\n",
current->fs->pwdmnt->mnt_sb->s_type->name,
(current->fs->pwdmnt->mnt_sb->s_flags & MS_RDONLY) ? " readonly" : "");
}

```

sys\_mount()で/dev/rootデバイスを/rootファイルシステムにmountしているように見えます。fs\_namesでループしていますが、これはどのファイルシステムを使うかを試しているようです。私が仕込んだデバックログでは以下のように表示されました。

```
mount_root:mount_block_root(/dev/root) root_mountflags=32769
get_fs_names() fs_names=/dev/root
get_fs_names() errno=0
sys_mount(): name=/dev/root p=ext2 flags=32769 root_mount_data=
sys_mount(): errno=0 err=-22  ※ext2ではなかった
sys_mount(): name=/dev/root p=romfs flags=32769 root_mount_data=
sys_mount(): errno=0 err=0    ※romfsと認識
putname() fs_names=ext2
putname() errno=0
sys_chdir(/root) errno=0
VFS: MAJOR=31, MINOR=0
VFS: Mounted root (romfs filesystem) readonly.
mount_root:mount_block_root(/dev/root) errno=0

```

putname()でext2を指定していますが、この実体はkmem\_cache\_free()なので使わないキャッシュを開放しているようです。そのあとにsys\_chdir()で/rootにカレントディレクトリを移動しています。

その後rootにマウントが完了したというメッセージが表示されます。

```
VFS: Mounted root (romfs filesystem) readonly.
```

### 最後の仕上げ

mount\_root()から戻ってきた後は、最後の仕上げとしてカレントディレクトリを/にします。

まずは、sys\_umount("/dev", 0);で、/devをumountします。その後カレントディレクトリを/にmountします。

そのあと、sys\_chroot(".");でカレントディレクトリをルートディレクトリに変更します。これでromfsがルートにmountされます。その後、mount\_devfs\_fs()がありますが、devfsは使っていないのですぐリターンしてきます。

```
           :
mount_root();
out:
sys_umount("/dev", 0);
sys_mount(".", "/", NULL, MS_MOVE, NULL);
sys_chroot(".");
mount_devfs_fs ();
}

```

以上で、prepare\_namespace()は終わりです。再びinitに戻ります。

### おかしなところが見当たらない

ここまでのステップでは私が組み込んだデバックログにエラーはみあたりません。

![mc68ez328_dragonone_sbc_uclinux_part7_mount_root_msg2.png](images/mc68ez328_dragonone_sbc_uclinux_part7_mount_root_msg2.png)

mount\_root()が終わった時点でromfsが/rootにmountできているように見え、その後ルートディレクトリにmountされているように見えるのですが。（続く）
