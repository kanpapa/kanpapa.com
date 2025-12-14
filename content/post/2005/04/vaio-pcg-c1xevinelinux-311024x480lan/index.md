---
title: "VAIO PCG-C1/XEにVineLinux 3.1をインストールしたメモ（1024x480と無線LAN)"
date: 2005-04-10
slug: "vaio-pcg-c1xevinelinux-311024x480lan"
categories: 
  - "pc"
tags: 
  - "linux"
  - "vaio"
---

VAIO PCG-C1にVineLinux 3.1をインストールしてみました。 普通のPCへのインストールは行えることが前提です。 ここではVAIO C1特有の画面サイズを1024x480に設定する方法と、無線LANの設定方法が中心です。 1. CD-ROM焼き 　Mac miniで焼きました。 2. VineLinux 3.1のインストール 　VAIOに純正CD-ROMを接続してインストールであります。テキストモードで実行しました。 3. /etc/X11/xorg.confの修正 (1) キーボードを106キーボードに。 Option "XkbModel" "pc101" を "jp106"に Option "XkbLayout" "us" を "jp" に (2) Monitorの定義 Section "Monitor" Identifier "VAIO" HorizSync 30-133 VertRefresh 50-200 ModeLine "1024x480" 65.00 1024 1032 1176 1344 480 488 494 563 -hsync -vsync EndSection (3) Deviceの定義 Section "Device" Identifler "VAIO" Driver "neomagic" VideoRam 2048 Option "externDisp" "" Option "internDisp" "" Option "override\_validate\_mode"　←これがミソ EndSection (4) Screenの定義 Section "Screen" Identifier "Screen 1" Device "VAIO" Monitor "VAIO" DefailtDepth 16 Subsection "Display" Depth 16 Modes "1024x480" ViewPort 0 0 EndSubsection EndSection 4. startx で、X11を起動すると、GNOMEが立ち上がる。 5. アプリケーション→システムツール→ネットワークの設定 　追加ボタンを押す 　無線LANの設定 　　無線LANデバイス　　　eth0 を選択 　　ネットワーク名　　　　ESSIDを入力 6. 無線LANのWEPパスワードの設定 　設定ファイル： /etc/sysconfig/network-scripts/ifcfg-eth0 BOOTPROTO=dhcp ONBOOT=yes USERCTL=YES NAME="無線 LAN カード" DEVICE=eth0 ESSID=XXXXXXXXXX ←さっき入力したESSIDが設定されてるはず。 PEERDNS=yes KEY=s:XXXXXXXXXX ←WEPパスワード。頭のs: は文字列であることを示す。 7. 5.のネットワークの設定で、「有効にする」ボタンを押す。 8. netstat やping でネットワーク接続を確認。 今日はここまで。
