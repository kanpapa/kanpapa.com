---
title: "mbed LPC1114FN28を使ってみた"
date: 2013-09-16
slug: "mbed-lpc1114fn28"
categories: 
  - "electronics"
tags: 
  - "mbed"
image: "images/mbed_LPC1114FN28.jpg"
---

LPC1114FN28がmbedになるという@ytsuboiさんの[mbed LPC1114での遊び方](http://mbed.org/users/ytsuboi/notebook/getting-started-with-mbed-lpc1114-ja/ "mbed LPC1114での遊び方")の記事は拝見していましたが、なかなか時間が無くて試せませんでした。

これではいかんと、[mbed祭り2013 in Yokohama](http://atnd.org/events/41584 "mbed祭り2013 in Yokohama")の当日の朝に手持ちのパーツを集めてブレッドボードで組んでみました。

ISPには秋月電子の[FT232RL USBシリアル変換モジュール](http://akizukidenshi.com/catalog/g/gK-01977/ "FT232RL USBシリアル変換モジュール")を使いました。

ブレッドボード１枚にまとめたかったので、少し横長のブレッドボードを使い、LPC1114FN28の右側はフリースペースとしました。今回はこのスペースに[LEDアレイ](http://akizukidenshi.com/catalog/g/gI-04761/ "高輝度10ポイントRGBLEDアレイOSX10201-LRPB2　フルカラー")と抵抗を実装し動作確認用としました。

USBシリアル変換モジュールはJ1でVCCIOを内蔵レギュレーターの3.3Vにするか、VCCにするかを切り替えることができます。LPC1114FN28は3.3V電源ですので、1-2間のジャンパーをショートして、VCCIOは3.3Vにしました。J2はUSBの電源を使いますのでショートしておきます。3.3Vレギュレーターの出力がモジュールの19番ピンにありますので、これをLPC1114FN28のVIN(3.3V)に接続します。

本来ですと、リセットスイッチとかもつけたかったのですが、スペースが無かったのでケーブルでGNDに落とすという適当な作りです。ISPモードに切り替えるための330Ωもその都度ブレッドボードに取り付けるという適当さです。

完成したブレッドボードの写真です。

![](images/mbed_LPC1114FN28.jpg)

MacOS Xでmbedのオンラインコンパイラを使って生成されたバイナリをFlashMagicとbin2hexを使ってLPC1114FN28に書き込みました。リセットすると問題なくLチカができました。このLEDアレイはカラーLEDなので適当に制御して遊んでみたいと思います。
