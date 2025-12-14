---
title: "玄箱でseti@homeに参加する"
date: 2007-04-02
categories: 
  - "server"
tags: 
  - "玄箱"
---

動き出した玄箱ですが、せっかく常時稼働しているのでBOINCを動かしてseti@homeに参加してみることにしました。

BOINCとかseti@homeとは何ぞやというのはそちらのページを読んでいただくこととして早速インストールです。

Debianのドキュメントをさがしてみたところこんなページがありました。

[http://wiki.debian.org/BOINC](http://wiki.debian.org/BOINC)

これによると、boinc-clientとboinc-managerとboinc-devというパッケージがあるようです。boinc-managerはboinc-clientを管理するGUIなので、KURO-BOXでは不要でしょう。

boinc-devはboincのアプリケーションを作成するためのパッケージなのでこれもあとでいれることとします。

boinc-clientで検索したところ、testingとunstableのパッケージしかないようです。そこで/etc/apt/sources.listを以下のように書き換えます。今回はCDNを使ってみました。

> $ sudo vi /etc/apt/sources.list
> 
> \# sources.list
> 
> deb [http://security.debian.org/](http://security.debian.org/) stable/updates main contrib non-free
> 
> deb [http://cdn.debian.or.jp/debian/](http://cdn.debian.or.jp/debian/) testing main contrib non-free
> 
> deb-src [http://cdn.debian.or.jp/debian/](http://cdn.debian.or.jp/debian/) testing main contrib non-free

書き換えが終わったらupdateです。

> $ sudo apt-get update
> 
> Get:1 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/main Packages \[5555kB\]
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/main Packages
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/main Release
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/contrib Packages
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/contrib Release
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/non-free Packages
> 
> Hit [http://security.debian.org](http://security.debian.org) stable/updates/non-free Release
> 
> Get:2 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/main Release \[84B\]
> 
> Get:3 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/contrib Packages \[56.4kB\]
> 
> Get:4 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/contrib Release \[87B\]
> 
> Get:5 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/non-free Packages \[74.7kB\]
> 
> Get:6 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/non-free Release \[88B\]
> 
> Get:7 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/main Sources \[1653kB\]
> 
> Get:8 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/main Release \[83B\]
> 
> Get:9 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/contrib Sources \[21.1kB\]
> 
> Get:10 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/contrib Release \[86B\]
> 
> Get:11 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/non-free Sources \[33.2kB\]
> 
> Get:12 [http://cdn.debian.or.jp](http://cdn.debian.or.jp) testing/non-free Release \[87B\]
> 
> Fetched 7394kB in 20s (361kB/s)
> 
> Reading Package Lists... Done

BOINC関係のパッケージがあるか確認します。

> $ sudo apt-cache search boinc
> 
> boinc-app-seti - SETI@home application for the BOINC client
> 
> boinc-client - core client for the BOINC distributed computing infrastructure
> 
> boinc-dev - development files to build applications for BOINC projects
> 
> boinc-manager - GUI to control and monitor the BOINC core client
> 
> kboincspy - monitoring utility for the BOINC client
> 
> kboincspy-dev - development files for KBoincSpy plugins

まずは、boinc-clientをインストールします。

> $ sudo apt-get install boinc-client

これでBOINCクライアントのインストールは完了しました。

さて、いよいよBOINCを動かします。続きはまた。
