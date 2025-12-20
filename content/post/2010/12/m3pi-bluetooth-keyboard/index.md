---
title: "mbed robot (m3pi)をBluetooth keyboardでコントロールしてみました"
date: 2010-12-11
slug: "m3pi-bluetooth-keyboard"
categories: 
  - "electronics"
image: "images/m3pi-bluetooth-keyboard-1.jpg"
---

mbed robot (m3pi)をBluetooth keyboardでコントロールするようにしてみました。

![](images/m3pi-bluetooth-keyboard-1-1024x768.jpg)

ベースのプログラムは[mbed](http://mbed.org/)の[Cookbook](http://mbed.org/cookbook/Homepage)にリンクされていたPeter Barrett さんの[BlueUSB](http://mbed.org/users/peterbarrett1967/programs/BlueUSB/)です。  
このプログラムではUSBに接続したBluetoothドングルを使って、キーボードやマウスやWiiリモコンなどのデータを受信して表示することができます。  
すでに手持ちのBluetoothキーボードでの動作は確認していましたので、あとはm3piのライブラリを組み込むだけです。  
BlueUSBの中の[TestShell.cpp](http://mbed.org/users/peterbarrett1967/programs/BlueUSB/5yn1q/docs/TestShell_8cpp_source.html)を改造して、m3piのクラスライブラリを組み込んで、キーボードの値によって、m3piに与えるコマンドを決めました。  
まずはスピードは控えめに0.1ぐらいにしてみました。  
動画はYouTubeにアップしましたが、キーボードで思ったようにコントロールできます。

{{< youtube rTww8PiBqTA >}}

コントローラがキーボードですので、他にもいろんな機能や動きを組み込むことができそうです。  
詳しくはmbed.orgの[Notebook](http://mbed.org/users/kanpapa/notebook/m3pi_bluetooth_keyboard/)にまとめましたので、そちらをご覧ください。
