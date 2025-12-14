---
title: "Qwiic OLEDを作ってみました"
date: 2021-07-05
categories: 
  - "electronics"
coverImage: "qwiic_oled3.jpg"
---

あるプロジェクトで[Qwiic](https://www.mouser.jp/new/sparkfun/sparkfun-qwiic-connect-system/ "Qwiic")が使われていました。プロジェクトでは[Qwiic Micro OLED](https://www.sparkfun.com/products/14532 "SparkFun Micro OLED Breakout (Qwiic)")が使われているのですが、[手持ちのOLED \[P-15870\]](https://akizukidenshi.com/ "0.96インチ 128x64ドット有機ELディスプレイ(OLED)")をこのQwiic対応にできればお安くできるのではと思いつきました。

都合の良いことに[Qwiic対応用の小さなコネクタ付き基板](https://www.sparkfun.com/products/14495 "SparkFun Qwiic Adapter")も売られていましたので、これをOLEDにはんだ付けすれば良いだろうと思ったのですが・・・

![qwiic_oled1.jpg](images/qwiic_oled1.jpg)

なぜか、SCAとSCLのピン配置が違います。なかなかうまくいかないものです。

<!--more-->

とりあえず、OLEDに最初からはんだ付けされていたピンヘッダを外します。

![qwiic_oled2.jpg](images/qwiic_oled2.jpg)

ここにQwiicのケーブルをはんだ付けするのが一番簡単な解決方法なのですが、そうするとQwiicのモジュールの途中にOLEDを取り付けることができなくなります。

少し試行錯誤したところで、2x4ピンのピンヘッダを使用してはんだ付けしてみました。

![qwiic_oled3.jpg](images/qwiic_oled3.jpg)

裏側はこのような感じです。しっかり固定はできています。

![qwiic_oled4.jpg](images/qwiic_oled4.jpg)

Raspberry Pi にqwiic pHatを取り付けて、製作したOLEDをQwiicケーブルで接続しサンプルプログラムを動かしたところ無事動作しました。

![qwiic_oled5.jpg](images/qwiic_oled5.jpg)

これで問題なくQwiic OLEDとして使えるでしょう。
