---
title: "SBC4004を組み立ててみました（２）組み立て編"
date: 2023-07-15
categories: 
  - "4004"
  - "retrocomputing"
tags: 
  - "sbc4004"
coverImage: "sbc4004_fpga_board1.jpg"
---

前回は[SBC4004の製作に必要なパーツを揃えました](https://kanpapa.com/2023/07/sbc4004-part1.html "SBC4004を組み立ててみました（１）準備編")。今回はSBC4004の組み立てを進めます。

組み立て方法は作者のサイトに詳しく説明されています。

- [4004マイクロプロセッサ 50周年　～　SBC4004/Busicom-141PFの製作手順(1)](https://jr2xzy.blogspot.com/2021/12/4004-50sbc4004busicom-141pf1.html "4004マイクロプロセッサ 50周年　～　SBC4004/Busicom-141PFの製作手順(1)") (JR2XZYブログ）

この通りに組み立てれば問題ないのですが、私が少しハマったところをまとめます。

SBC4004はFPGAとArduinoを使用していますので、まずはこれらにファームウェアを書き込む必要があります。

### FPGAボードの準備

最初にFPGAボードの改造を行います。

![sbc4004_fpga_board1.jpg](images/sbc4004_fpga_board1.jpg)

<!--more-->

裏面にある指定されたチップ抵抗とチップコンデンサをはんだごてで温めて外します。

![sbc4004_fpga_board2.jpg](images/sbc4004_fpga_board2.jpg)

無事R1、R2、R9、R10、R13、C14を取り外しました。

![sbc4004_fpga_board3.jpg](images/sbc4004_fpga_board3.jpg)

FPGAにファームウェアを書き込むために専用の書き込み機USB Blasterが必要になります。こちらはAmazonで安価な互換品を購入しました。

- [KOZEEY 【ノーブランド品】USB　ブラスター　ケーブル　CPLD　FPGA　JTAG　プログラマ　アルテラ](https://www.amazon.co.jp/gp/product/B008D8QSMU/ "KOZEEY 【ノーブランド品】USB　ブラスター　ケーブル　CPLD　FPGA　JTAG　プログラマ　アルテラ")

購入したUSB BlasterをWindowsPCに接続したのですが、なぜかデバイスとして認識されません。デバイスマネージャーで確認すると「不明なUSBデバイス（デバイス記述子要求の失敗）」となっています。

![sbc4004_usb_blaster_usb3x1.jpg](images/sbc4004_usb_blaster_usb3x1.jpg)

![sbc4004_usb_blaster_usb3x2.jpg](images/sbc4004_usb_blaster_usb3x2.jpg)

いろいろ試したところ、USB2.0接続だと「Altera USB-Blaster」と認識することを発見しました。

![sbc4004_usb_blaster_usb2x1.jpg](images/sbc4004_usb_blaster_usb2x1.jpg)

![sbc4004_usb_blaster_usb2x2.jpg](images/sbc4004_usb_blaster_usb2x2.jpg)

私が購入したものはUSB3.0と相性が良くなかったようです。そのためPC本体のUSB3.0端子にUSB2.0ハブを接続して、そこにUSB Blasterを接続した状態でQuartus Programmerを使ってFPGAにバイナリファイルを書き込みました。

![sbc4004_USB_Blaster2.jpg](images/sbc4004_USB_Blaster2.jpg)

無事FPGAに書き込みが完了したようです。

![sbc4004_fpga_program1.jpg](images/sbc4004_fpga_program1.jpg)

### Arduino Pro Microの準備

購入したArduino Pro Micro互換機です。

![sbc4004_arduino_1.jpg](images/sbc4004_arduino_1.jpg)

こちらはArduino IDEを使って準備されているスケッチを書き込めば完了です。

![sbc4004_arduino_2.jpg](images/sbc4004_arduino_2.jpg)

### パーツの取り付け

専用基板にパーツをはんだ付けをしていきます。

![sbc4004_pcb2.jpg](images/sbc4004_pcb2.jpg)

細かい手順は作者のサイトに書かれているのでその通りに進めれば問題なくできます。FPGAボードやArduino Pro Microを取り付けるコツも書かれていますので参考になります。

はんだ付けがほぼ完了した基板になります。

![sbc4004_pcb3.jpg](images/sbc4004_pcb3.jpg)

まだキートップをつけていませんが、これは最後に行うことにします。

[SBC4004を組み立ててみました（３）動作確認編](https://kanpapa.com/2023/07/sbc4004-part3.html "SBC4004を組み立ててみました（３）動作確認編")に続きます。
