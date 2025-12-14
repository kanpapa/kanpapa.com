---
title: "MC68EZ328 DragonOne SBCでuClinuxを動かす(6) ～initスレッドを追う～"
date: 2021-05-23
slug: "mc68ez328-dragonone-sbc-uclinux-part6"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/drgonone-sbc-linux-init1.png"
---

ようやく[initスレッドの起動](https://kanpapa.com/2021/05/mc68ez328-dragonone-sbc-uclinux-part5.html "MC68EZ328 DragonOne SBCでuClinuxを動かす(5) ～initスレッドの起動まで～")までできました。これまでたどったソースから、Linuxの起動メッセージの以下の部分まではたどり着いたはずです。

```
Linux version 2.4.34.5-uc0 (ocha@M715Q-TINY) (gcc version 4.7.2 (GCC) ) #49 Sat May 22 22:05:45 JST 2021
68EZ328 DragonBallEZ support (C) 1999 Rt-Control, Inc
uClinux/MC68EZ328Flat model support (C) 1998,1999 Kenneth Albanowski, D. Jeff Dionne
On node 0 totalpages: 2048
zone(0): 0 pages.
zone(1): 2048 pages.
zone(2): 0 pages.
Kernel command line:
Calibrating delay loop... 0.89 BogoMIPS
Memory available: 7772k/8064k RAM, 0k/0k ROM (341k kernel code, 186k data)
Dentry cache hash table entries: 1024 (order: 1, 8192 bytes)
Inode cache hash table entries: 512 (order: 0, 4096 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 2048 (order: 1, 8192 bytes)
POSIX conformance testing by UNIFIX
```

以降はinitスレッドでの処理になります。この中でルートディレクトリのmount処理も行われます。

### initスレッド

実はinitスレッドはシンプルです。カーネルの初期化を進め最終的にはinitプロセスを起動します。今回はromfsのルートファイルシステムがmountできていないのが問題なのでそこを中心に追います。

```
static int init(void * unused)
{
    struct files_struct *files;
    lock_kernel();
    do_basic_setup();
    prepare_namespace();
    free_initmem();
    unlock_kernel();
    files = current->files;
    if(unshare_files())
        panic("unshare");
    put_files_struct(files);
    if (open("/dev/console", O_RDWR, 0) < 0)
        printk("Warning: unable to open an initial console.\n");
    (void) dup(0);
    (void) dup(0);
    if (execute_command)
        run_init_process(execute_command);
    run_init_process("/sbin/init");
    run_init_process("/etc/init");
    run_init_process("/bin/init");
    run_init_process("/bin/sh");
    panic("No init found.  Try passing init= option to kernel.");
}
```

今回問題となっているNo init foundやinitial consoleの文字が見えます。まずはdo\_basic\_setup()をみておきます。

### do\_basic\_setup

do\_basic\_setupではソケットの初期化と必要なスレッドの初期化を行います。mountに関するものは無さそうです。

```
static void __init do_basic_setup(void)
{
    child_reaper = current;
    /* Networking initialization needs a process context */
    sock_init();
    start_context_thread();
    do_initcalls();
}
```

すでに何度も確認しているのでわかっているのですが、ルートファイルシステムをmountしているのは、prepare\_namespace()です。ここを中心にみていきます。（続く）
