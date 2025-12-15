---
title: "第18回 IT基礎技術勉強会に参加してきました"
date: 2012-07-01
slug: "itbeginner18-html"
categories: 
  - "research"
---

[第18回 IT基礎技術勉強会「Assembler, Kernel, Binary 勉強会(ARM編)」](http://atnd.org/events/29435)に参加してみました。

この勉強会はKOZOSという学習向け自作組み込みOSを開発されている@kozossakaiさんが開催しているものです。

前回はFreeBSD(x86)を使って「Hello World」を追ってみましたが、今回はARMというマイコンが題材です。

ARMは[mbed](http://mbed.org/)や[MARY](http://toragi.cqpub.co.jp/tabid/412/Default.aspx)でなじみがありますが、ARMのアセンブラを直接書いたことはありませんのでぜひ体験したいと考えました。

Interface誌とかトラ技増刊などでARMの基板も付録でついてきますし、秋月電子等でも1000円ぐらいでARMの評価ボードが買える時代です。ARMは知っておくべきでしょう。

準備としては前回同様にノートPC上のFreeBSD-8.3を使いましたが、今回はクロスコンパイル環境ですので、ARM用のgccやgdbなどを事前にビルドしておきました。

勉強会は前回同様な流れで進みましたが、前回とは違って説明資料は無く、ついていくのが精一杯だったのでなるべく[メモ](https://www.evernote.com/shard/s35/sh/7abe4c3b-3d69-4c5c-87ee-f3705d8a2db5/7d1f04ddf39f0393a74d68af938c85d5)を取ることに重点をおきました。

今回おもしろかったのはRISCプロセッサならではの1命令が4バイトの固定長のため、レジスタに定数を設定するだけでも工夫が必要なこと、startup.Sの役割、ゼロから標準ライブラリをどのように作っていくか、ARMは奇数アドレスにコードがあると16ビットコードと認識していることなど、新鮮な内容でした。

今回もかなりスピードが速かったので、[メモ](https://www.evernote.com/shard/s35/sh/7abe4c3b-3d69-4c5c-87ee-f3705d8a2db5/7d1f04ddf39f0393a74d68af938c85d5)を見ながらもう一度復習して、大筋は理解できたかなと思います。

次回はどんなテーマでしょうか。楽しみです。

  

- [第18回 IT基礎技術勉強会の講義内容メモ](https://www.evernote.com/shard/s35/sh/7abe4c3b-3d69-4c5c-87ee-f3705d8a2db5/7d1f04ddf39f0393a74d68af938c85d5)
