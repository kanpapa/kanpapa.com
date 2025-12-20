---
title: "mbed robot (m3pi)に距離センサーをつけてみました"
date: 2011-11-23
slug: "mbed-m3pi-distance"
categories: 
  - "electronics"
image: "images/m3pi_distance_sensor.jpg"
---

[m3pi](http://mbed.org/cookbook/m3pi)に秋月電子で売っている赤外線距離センサーユニット(GP2Y0A21)を搭載してみました。  
![m3pi_distance_sensor.jpg](images/m3pi_distance_sensor.jpg)  
このセンサーユニットは電源が4.5V-5.5Vですので、m3piのVccがそのまま使えます。データシートにVcc-GND間で10μFのコンデンサをいれるように書いてあったのでそれも追加しました。  
センサーからの出力はmbedのAnaloginで読んでいますが、3.3Vまでとのことなので、10KΩの抵抗を間にいれて大体範囲内に収まるようにしてmbedに接続しています。  
センサーユニットは両面テープで基板に固定していますが、重心が前に寄ってしまったので、後ろにクリップでおもりをつけています。  
前方にある障害物との距離を計測し、距離が近づく­につれて、mbedの4つのLEDの点灯数を増やしています。  
10cm未満になったら後退して、方向転換を行い再び前進するようにプログラムしました。  
プログラムはまだ荒削りですが、[こちら](http://mbed.org/users/kanpapa/programs/m3pi_ledpsd/m12w8i)にあります。本当に簡単で短時間で動作確認ができました。

{{< youtube LqP9Cs3XdtY >}}
