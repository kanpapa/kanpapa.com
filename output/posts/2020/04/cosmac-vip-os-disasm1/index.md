---
title: "COSMAC VIP OSを調べてみました"
date: 2020-04-19
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
coverImage: "vip_os_sample_display1.jpg"
---

[STG1861+HEX KEYの基板](https://kanpapa.com/cosmac/blog/2020/04/cosmac-mbc-stg1861-keyboard-rev01.html "COSMAC MBC STG1861 DISPLAY/HEX KEYBOARD Rev.0.1の基板を発注しました")が無事発送され、すでにTOKYO SKYGATEに届いているものの、手元にまったく届かないので、[COSMAC VIP](http://oldcomputers.net/rca-cosmac-vip.html "RCA COSMAC VIP") OS（モニタに相当するもの）のバイナリを解析してみました。COSMAC VIP OSはダンプリストで公開されていますので、バイナリを逆アセンブルをしてコードとデータを分けなから動きを追ってみます。

COSMACは命令が簡単すぎるので、何をやるにもステップが多くなりがちです。COSMAC VIP OSは$8000～$81FFまでの512byteとコンパクトですが、画面表示やキー入力、カセットテープへの入出力など多機能なものになっています。これを512byteにどうやって納めているのでしょうか。こういう解析を行うことで、プロのコーディングテクニックが分かるので非常に勉強になります。

解析中の様子です。プリンタで出力したリストにコメントを入れながら動きを追っていきます。

![vip_os_disasm1.jpg](images/vip_os_disasm1.jpg)

<!--more-->

COSMAC VIP OSは画面表示に特徴があります。

![vip_os_sample_display1.jpg](images/vip_os_sample_display1.jpg)

画面にはランダムな模様が表示されていますが、実はOSが起動する直前のレジスタの内容を表している部分があるのです。またいつもランダムな動きをしているエリアがありますが、ここはWORKエリアとして使われています。このあたりはCOSMAC VIPのマニュアルにも触れられています。情報を整理すると以下のようになります。

![vip_os_vram_layout1.jpg](images/vip_os_vram_layout1.jpg)

COSMAC VIPはOSに制御をわたす直前に全レジスタをVRAM領域に保存しています。全レジスタに対してGHI(Get HIgh)命令で上位バイトを、GLO(Get LOw)命令で下位バイトを読みださなければなりません。これを素直にコーディングすると、16個のレジスタ分GHI命令、GLO命令を並べなければなりません。そこで、COSMAC VIPではWORKエリアにGHI、GLOの命令を1つずつ書き込み実行することで全レジスタの上位バイト、下位バイトを読み込んでいました。OSにはこのようなテクニックがちりばめられていてなかなかおもしろいです。

まだすべては解析できていませんが、おおまかなところはわかりました。次に動かそうとしているCHIP-8はこのOSに依存しているようなので基板が届くまで、細かく見ておきたいと思います。
