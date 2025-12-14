---
title: "m3piにUSBコネクタを取り付けました"
date: 2010-12-05
slug: "m3pi-usb"
categories: 
  - "robot"
tags: 
  - "m3pi"
image: "images/m3pi_Bluetooth_1.jpg"
---

m3piにUSBコネクタを取り付けてみました。といってもmbedにUSBコネクタを接続するだけですが。  
ついでにmbedから直接信号が取れるように1列×20Pのピンソケットもハンダ付けしました。  
3piの拡張基板ですが、mbedを実装するとそんなに空きスペースはありません。  
とりあえずこのあたりかなということで、手持ちのUSB Aコネクタをハンダ付けしてmbedに接続しました。  
もし縦型のUSB Aコネクタが手に入るようであれば、それに付け替えたいと思います。

![](images/m3pi_Bluetooth_1.jpg)

まずは手持ちのPLANEX(PCI) Bluetooth USBアダプタ BT-MicroEDR2Xを接続してみました。  
Vccは3piから取っているので、3piの電源をいれるとBluetoothアダプタのLEDが点灯しました。ここまでは問題ないようです。  
次に [Bluetoothのテストプログラム](http://mbed.org/users/peterbarrett1967/notebook/blueusb---bluetooth-and-usb-host-controller-for-mb/)がCookbookにありましたので、まずはそれを書き込んでみました。  
手持ちのBluetoothキーボードとの通信も無事できているようです。

https://youtu.be/JFBtjI7e8I8?si=taHIA8lUIVJ72esq

あとはBluetoothの情報で、m3piが動くようにプログラムを書けばリモコン制御できそうです。
