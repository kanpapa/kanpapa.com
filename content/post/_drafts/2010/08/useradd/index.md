---
title: "１日目 アカウントを作る"
date: 2010-08-18
slug: "useradd"
draft: true
---

さくらのVPSに申し込むとサーバのIPアドレスとrootのパスワードの通知があるのでそれでログインする。

```
$ ssh root@XX.XXX.XXX.XXX
root@XX.XXX.XXX.XXX's password:
[root@XXXXXXXX ~]# ps ax
PID TTY      STAT   TIME COMMAND
1 ?        Ss     0:00 init [3]
　　　：（省略）
1656 ?        Rs     0:00 sshd: root@pts/0
1658 pts/0    Ss     0:00 -bash
1681 pts/0    R+     0:00 ps ax
[root@XXXXXXXX ~]# df -k
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/hda2             18222732   1582936  15699192  10% /
/dev/hda1               101086     11917     83950  13% /boot
tmpfs                   255264         0    255264   0% /dev/shm
[root@XXXXXXXX ~]# ps ax

```

ふ〜ん。とりあえずユーザアカウントを作ろう。

```
[root@XXXXXXXX ~]# useradd XXXXXXXX
[root@XXXXXXXX ~]# passwd XXXXXXXX
Changing password for user XXXXXXXX.
New UNIX password:
Retype new UNIX password:
passwd: all authentication tokens updated successfully.
[root@XXXXXXXX ~]# cat /etc/passwd
　　：

```

ふーん、デフォルトのシェルは/bin/bashね。 とりあえずrootになれるようにwheelグループに入れとこう。

```
[root@XXXXXXXX ~]# usermod -G wheel XXXXXXXX
[root@XXXXXXXX ~]# cat /etc/group
　　：

```

おっけ〜 とりあえず、Webサーバをいれよう。

```
[root@XXXXXXXX ~]# yum -y install httpd
Loaded plugins: fastestmirror
Determining fastest mirrors
* addons: rsync.atworks.co.jp
* base: rsync.atworks.co.jp
* extras: rsync.atworks.co.jp
* updates: rsync.atworks.co.jp
addons                                                   |  951 B     00:00
base                                                     | 2.1 kB     00:00
extras                                                   | 2.1 kB     00:00
updates                                                  | 1.9 kB     00:00
updates/primary_db                                       | 346 kB     00:00
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package httpd.x86_64 0:2.2.3-43.el5.centos set to be updated
addons/filelists                                         |  197 B     00:00
base/filelists_db                                        | 4.0 MB     00:00
extras/filelists_db                                      | 220 kB     00:00
updates/filelists_db                                     | 1.2 MB     00:00
--> Finished Dependency Resolution
Dependencies Resolved
================================================================================
Package       Arch           Version                        Repository    Size
================================================================================
Installing:
httpd         x86_64         2.2.3-43.el5.centos            base         1.2 M
Transaction Summary
================================================================================
Install       1 Package(s)
Upgrade       0 Package(s)
Total download size: 1.2 M
Downloading Packages:
httpd-2.2.3-43.el5.centos.x86_64.rpm                     | 1.2 MB     00:00
warning: rpmts_HdrFromFdno: Header V3 DSA signature: NOKEY, key ID e8562897
base/gpgkey                                              | 1.5 kB     00:00
Importing GPG key 0xE8562897 "CentOS-5 Key (CentOS 5 Official Signing Key) " from /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
Installing     : httpd                                                    1/1
Installed:
httpd.x86_64 0:2.2.3-43.el5.centos
Complete!
[root@XXXXXXXX ~]#

```

おっけー ついでに、PHPもいれちゃおう。

```
[root@XXXXXXXX ~]# yum -y install php php-mbstring
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
* addons: rsync.atworks.co.jp
* base: rsync.atworks.co.jp
* extras: rsync.atworks.co.jp
* updates: rsync.atworks.co.jp
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package php.x86_64 0:5.1.6-27.el5 set to be updated
--> Processing Dependency: php-common = 5.1.6-27.el5 for package: php
--> Processing Dependency: php-cli = 5.1.6-27.el5 for package: php
---> Package php-mbstring.x86_64 0:5.1.6-27.el5 set to be updated
--> Running transaction check
---> Package php-cli.x86_64 0:5.1.6-27.el5 set to be updated
---> Package php-common.x86_64 0:5.1.6-27.el5 set to be updated
--> Finished Dependency Resolution
Dependencies Resolved
================================================================================
Package              Arch           Version                 Repository    Size
================================================================================
Installing:
php                  x86_64         5.1.6-27.el5            base         2.3 M
php-mbstring         x86_64         5.1.6-27.el5            base         1.0 M
Installing for dependencies:
php-cli              x86_64         5.1.6-27.el5            base         2.2 M
php-common           x86_64         5.1.6-27.el5            base         153 k
Transaction Summary
================================================================================
Install       4 Package(s)
Upgrade       0 Package(s)
Total download size: 5.6 M
Downloading Packages:
(1/4): php-common-5.1.6-27.el5.x86_64.rpm                | 153 kB     00:00
(2/4): php-mbstring-5.1.6-27.el5.x86_64.rpm              | 1.0 MB     00:00
(3/4): php-cli-5.1.6-27.el5.x86_64.rpm                   | 2.2 MB     00:00
(4/4): php-5.1.6-27.el5.x86_64.rpm                       | 2.3 MB     00:00
--------------------------------------------------------------------------------
Total                                           6.3 MB/s | 5.6 MB     00:00
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
Installing     : php-common                                               1/4
Installing     : php-cli                                                  2/4
Installing     : php-mbstring                                             3/4
Installing     : php                                                      4/4
Installed:
php.x86_64 0:5.1.6-27.el5          php-mbstring.x86_64 0:5.1.6-27.el5
Dependency Installed:
php-cli.x86_64 0:5.1.6-27.el5         php-common.x86_64 0:5.1.6-27.el5
Complete!
[root@XXXXXXXX ~]#

```

Webサーバが動くように最低限の設定を。

```
[root@XXXXXXXX ~]# cd /etc/httpd/conf
[root@XXXXXXXX conf]# ls -l
total 52
-rw-r--r-- 1 root root 33726 Apr  5 06:22 httpd.conf
-rw-r--r-- 1 root root 13139 Apr  5 06:21 magic
[root@XXXXXXXX conf]# mv httpd.conf httpd.conf.org
[root@XXXXXXXX conf]# cp httpd.conf.org httpd.conf
[root@XXXXXXXX conf]# vi httpd.conf
　　：
[root@XXXXXXXX conf]#
[root@XXXXXXXX conf]# /etc/rc.d/init.d/httpd start
Starting httpd:                                            [  OK  ]
[root@XXXXXXXX conf]# ps ax
PID TTY      STAT   TIME COMMAND
1 ?        Ss     0:00 init [3]
2 ?        S<     0:00 [migration/0]
　　：（省略）
1710 pts/1    Ss+    0:00 -bash
1785 ?        Ss     0:00 /usr/sbin/httpd
1787 ?        S      0:00 /usr/sbin/httpd
1788 ?        S      0:00 /usr/sbin/httpd
1789 ?        S      0:00 /usr/sbin/httpd
1790 ?        S      0:00 /usr/sbin/httpd
1791 ?        S      0:00 /usr/sbin/httpd
1792 ?        S      0:00 /usr/sbin/httpd
1793 ?        S      0:00 /usr/sbin/httpd
1794 ?        S      0:00 /usr/sbin/httpd
1795 pts/0    R+     0:00 ps ax
[root@XXXXXXXX conf]#

```

うん、動いてる。 Webブラウザからもアクセス確認。

```
[root@XXXXXXXX conf]# date
Fri Jul 16 00:55:28 JST 2010
[root@XXXXXXXX conf]#

```

１日目はこんなところかな。
