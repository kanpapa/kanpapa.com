---
title: "Let's Note(CF-W2)のdebian Linuxで無線LANに接続"
date: 2008-11-01
slug: "lets-notecf-w2debian-linuxlan"
categories: 
  - "pc"
tags: 
  - "debian"
  - "linux"
  - "無線lan"
---

少し前にPanasonic Let's Note CF-W2にdebian linux 4.0をインストールして、そのまま放置状態だったのですが、久々に電源をいれました。無線LANの接続をまだやっていなかったので、そのあたりの資料を探して接続してみました。ちなみにCF-W2の無線LANはIntel PRO /Wireless 2200BGです。

1\. 以下のパッケージをインストール

・installed ipw2200-modules-2.6.18-6-686 2.6.18+1.2.0-4+etch3

その他の必要なパッケージは最初から入っていました。

2\. リブートしたらこんなエラーがでた。ファームウェアが必要らしい。

ipw2200: Detected Intel PRO/Wireless 2200BG Network Connection

ipw2200: ipw2200-bss.fw request\_firmware failed: Reason -2

ipw2200: Unable to load firmware: -2

ipw2200: failed to register network device

3\. ファームウェアを以下のサイトからダウンロード

[http://ipw2200.sourceforge.net/](http://ipw2200.sourceforge.net/)

4\. 展開して指定されたディレクトリにコピー

letsnote:/ipw2200-fw-3.0# cp \*.fw /usr/lib/hotplug/firmware/.

letsnote:/ipw2200-fw-3.0# ls -l /usr/lib/hotplug/firmware/

\-rw-r--r-- 1 root root 191142 2008-11-01 21:30 ipw2200-bss.fw

\-rw-r--r-- 1 root root 185660 2008-11-01 21:30 ipw2200-ibss.fw

\-rw-r--r-- 1 root root 187836 2008-11-01 21:30 ipw2200-sniffer.fw

letsnote:/ipw2200-fw-3.0#

5\. 設定ファイルの作成

WEPの場合であれば、GUIツールが標準で入っているのでそれを使えばいいのだが、我が家の無線LANはWPA-TKIPなので、/etc/networks/interfacesを以下のように直接書き直した。

\# The Secondary network interface

\# wireless (WPA) for DHCP

iface eth1 inet dhcp

wpa-ssid SSIDを記載

wpa-psk パスワードを記載

auto eth1

これでうまくいくかなと思ったら、どうしてもDHCPのところでIPが取得できない。

試しにstaticの設定にしてみた。

\# The Secondary network interface

\# wireless (WPA) for Static

iface eth1 inet static

address 192.168.3.124

netmask 255.255.255.0

gateway 192.168.3.1

wpa-ssid SSIDを記載

wpa-psk パスワードを記載

auto eth1

・・・・結局だめ。

さんざん試したあげくWPAのパスワードが間違っていたというお粗末な結果で、正しいパスワードを設定したらあっさりつながってしまいました。（StaticもDHCPも）

昔のドキュメントではWPAを使用するには、/etc/wpa\_supplicant/wpa\_supplicant.confを設定すると記載しているものが多いですが、今は/etc/networks/interfacesに統合されているので、この設定ファイルだけでOKでした。

さあ、あとはMacBook Proからsshでログインしてサーバ化だ。
