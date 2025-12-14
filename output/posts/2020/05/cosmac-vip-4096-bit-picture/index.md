---
title: "COSMAC VIP 4096-Bit Pictureを動かしてみました"
date: 2020-05-01
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
coverImage: "VIP_4096bit_picture.jpg"
---

[COSMAC VIP のマニュアル](http://bitsavers.trailing-edge.com/components/rca/cosmac/COSMAC_VIP_Instruction_Manual_1978.pdf "http://bitsavers.trailing-edge.com/components/rca/cosmac/COSMAC_VIP_Instruction_Manual_1978")に掲載されている VIP 4096-Bit Pictureを動かしてみました。

どのような画面が表示されるのは全く分からなかったのですが、この画面が表示されたときは感動ものでした。

![VIP_4096bit_picture.jpg](images/VIP_4096bit_picture.jpg)

このプログラムは$0000-$002Fの表示プログラム本体と$0100-$02FFの表示データにわかれています。なかなかの入力量です。これをCOSMAC VIPのモニタと16進キーパッドで入力するのは、かなりの精神力が必要だったのだろうと想像します。

<!--more-->

マニュアルにはダンプリストで掲載されているのですが、うれしいことにPDFデータに文字情報が含まれているので、それを利用してダンプリストを再現しました。しかし、OCRでの読み取りのため、たまに1がIになったり、5がSになったり、0がDになったりとデータは完全ではありません。このあたりは目視で全部のデータが一致していることを確認します。昔のI/O誌やASCII誌のようなチェックサムが欲しいところですが。

70年代といえば、STARTREKとSNOOPYが人気だったんでしょうね。

大量のダンプリストを打ち込んで、うまく動いたときの喜びは昔も今でも変わらずです。
