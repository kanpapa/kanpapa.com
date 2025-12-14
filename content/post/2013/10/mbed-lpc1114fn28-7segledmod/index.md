---
title: "mbed LPC1114FN28で8桁7セグLEDモジュールを制御してみた"
date: 2013-10-06
slug: "mbed-lpc1114fn28-7segledmod"
categories: 
  - "electronics"
tags: 
  - "mbed"
image: "images/mbed_7degLEDMod.jpg"
---

mbed LPC1114FN28で[秋月電子の3-Wire 8桁7セグLEDモジュール](http://akizukidenshi.com/catalog/g/gM-06681/ "ＳＰＩ（３線式）　ＬＥＤ　Ｍｏｄｕｌｅ　８　Ｄｉｇｉｔａｌ　（Ａｒｄｕｉｎｏ Ｃｏｍｐａｔｉｂｌｅ）")を動かしてみました。

LEDモジュールとmbedとの接続は以下の３本のみです。

```
mbed      LEDモジュール
-------------------------
dp9         DATA
dp10       LATCH
dp11       CLOCK
```

LEDモジュールにはUSBからの5Vを供給しています。LEDモジュールの消費電力は最大300mAぐらいなので問題なさそうです。LPC1114FN28にはFT232RL内蔵の3.3Vレギュレータの出力を使っています。

本体はこんな感じです。

![](images/mbed_7degLEDMod.jpg)

制御プログラムは[DFROBOT社のサイト](http://www.dfrobot.com/wiki/index.php/3-Wire_LED_Module_\(SKU:DFR0090\) "3-Wire_LED_Module_(SKU:DFR0090)")にArduino用のサンプルプログラムがありましたのでそれを参考にしました。サンプルプログラムは[こちら](https://mbed.org/users/kanpapa/code/3wire_led_module_sample1/ "3wire_led_module_sample1")にPublishしておきました。

動作中の様子をYouTubeにアップしておきました。

今回はこのLEDモジュール１台で８桁の数字を表示していますが、表示データを用意すれば数字以外の表示もできますし、LEDモジュールにあるOUTPUT端子にさらにLEDモジュールを接続することで表示桁数を増やすこともできます。工夫次第で面白い使い方ができそうです。
