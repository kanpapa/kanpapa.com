---
title: "debian Linuxを玄箱にセットアップ その１"
date: 2007-03-25
slug: "debian-linux"
categories: 
  - "server"
tags: 
  - "玄箱"
---

玄箱(KURO-BOX)にDebian Linuxをインストールしてみました。

参考としたホームページは以下の通りです。

- [玄箱うぉううぉう♪](http://kuro.dsk.jp/)
- [オモイノホカ日々徒然　Debian化キットの導入 (2006.06.11)](http://www17.ocn.ne.jp/~tuzre/kurobox/kb_debian_woody.html)

覚え書きとして手順を書いておきます。

1.「玄箱うぉううぉう♪」さんから、debian\_2006\_06\_10\_dist.tgzをダウンロード

2.「オモイノホカ日々徒然」さんにある手順の通りにセットアップ

3\. パスワードの設定

> Debian GNU/Linux 3.0 KURO-BOX
> 
> KURO-BOX login: tmp-kun
> 
> Password: xxxxxxx
> 
> Last login: Sun May 2 15:10:53 2004 from 192.168.0.32 on pts/0
> 
> Linux KURO-BOX 2.4.17\_kuro-box #4 2004年 4月 16日 金曜日 11:45:05 JST ppc unknown
> 
> : 省略
> 
> tmp-kun@KURO-BOX:~$ su -
> 
> Password: xxxxxxxx
> 
> KURO-BOX:~# passwd root
> 
> Enter new UNIX password: newpassword
> 
> Retype new UNIX password: newpassword
> 
> passwd: password updated successfully
> 
> KURO-BOX:~# passwd tmp-kun
> 
> Enter new UNIX password: newpassword
> 
> Retype new UNIX password: newpassword
> 
> passwd: password updated successfully

4\. IPアドレスの変更

> KURO-BOX:/etc# vi /etc/hosts
> 
> 127.0.0.1 localhost
> 
> #192.168.0.100 KURO-BOX ←コメントにする
> 
> 192.168.3.121 KURO-BOX　　←新しいIPを設定
> 
> KURO-BOX:/etc# vi /etc/hosts.allow
> 
> 　：省略
> 
> #ALL : 192.168.0.0/255.255.255.0　←コメントにする
> 
> ALL : 192.168.3.0/255.255.255.0　←新しいIPを設定
> 
> ALL : 127.0.0.1
> 
> KURO-BOX:/etc# vi /etc/resolv.conf
> 
> search
> 
> #nameserver 192.168.0.1　←コメントにする
> 
> nameserver 192.168.3.1　←我が家のDNSサーバ(ルータ)に変更
> 
> KURO-BOX:/etc # vi /etc/network/interfaces
> 
> 　：省略
> 
> iface eth0 inet static
> 
> #address 192.168.0.100　←コメントにする
> 
> #network 192.168.0.0　←コメントにする
> 
> #netmask 255.255.255.0　←コメントにする
> 
> #broadcast 192.168.0.255　←コメントにする
> 
> #gateway 192.168.0.1　←コメントにする
> 
> address 192.168.3.121　←我が家のネットワークに合わせて書き換え
> 
> network 192.168.3.0　←我が家のネットワークに合わせて書き換え
> 
> netmask 255.255.255.0　←我が家のネットワークに合わせて書き換え
> 
> broadcast 192.168.3.255　←我が家のネットワークに合わせて書き換え
> 
> gateway 192.168.3.1　←我が家のネットワークに合わせて書き換え
> 
> iface lo inet loopback
> 
> auto eth0 lo

5\. 作業用ユーザアカウントの登録

> KURO-BOX:~# df -k
> 
> Filesystem 1k-blocks Used Available Use% Mounted on
> 
> /dev/hda1 2063504 154080 1804604 8% /
> 
> /dev/hda3 55375288 398944 54976344 1% /mnt
> 
> KURO-BOX:~# mkdir /mnt/home/username
> 
> KURO-BOX:~# useradd -u 1001 -g users -d /mnt/home/newuser -s /bin/bash newuser
> 
> KURO-BOX:~# passwd newuser
> 
> Enter new UNIX password: xxxxxxxx
> 
> Retype new UNIX password: xxxxxxxx
> 
> passwd: password updated successfully
> 
> KURO-BOX:~# chown newuser:users /mnt/home/newuser

6\. 再起動

> KURO-BOX:/mnt/home# sync
> 
> KURO-BOX:/mnt/home# sync
> 
> KURO-BOX:/mnt/home# sync
> 
> KURO-BOX:/mnt/home# reboot

これでネットワークとアカウントの設定までできました。簡単です。
