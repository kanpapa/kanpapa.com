---
title: "mbed NXP LPC11U24でm3piを動かしてみました。"
date: 2012-01-30
slug: "mbed-m0-m3pi"
categories: 
  - "electronics"
---

mbed NXP LPC11U24でm3piを動かしてみました。  
最初にプログラムがコンパイルできなくてびっくりしましたが、mbedのライブラリを最新版にしたら問題なくコンパイルできました。  
早速バイナリを転送して動かしてみましたが、黄mbedでも青mbedと同じように動きました。

https://youtu.be/VDU5uLKLbyU?si=JtveTW4jXg-IKHpB

ただし、黄mbedにはUSBホストの機能はなく、１つしかないシリアルも3piとの通信で使ってしまいますのでその点は青mbedに見劣りします。  
でも消費電力は黄mbedが有利なので、このようなバッテリで動かすものには適しているのではと思います。
