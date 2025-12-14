---
title: "ルンバの簡易シリアルケーブルを作りました"
date: 2022-09-19
slug: "roomba-serial-cable"
categories: 
  - "roomba"
tags: 
  - "roomba"
image: "images/roomba_serial_connect1.jpg"
---

これまでルンバのシリアル接続は、USBシリアル変換ボードのコネクタとルンバのシリアルコネクタにブレッドボード用のワイヤーを刺して行っていました。

![roomba_serial_wire1.jpg](images/roomba_serial_wire1.jpg)

先日このワイヤーが切れてしまったので、もう少し使い勝手の良いものを作ってみました。これまでは単純にワイヤーを刺しているだけなので、抜けやすかったり、取り外したときにTX-RXがどっちだっけと悩むことも多かったのです。

USBシリアル変換ボードはそのまま使うとして、しっかりしたコネクタで接続するようにしてみました。秋月電子にある[FTDI USBシリアル変換ケーブル(5V)](https://akizukidenshi.com/catalog/g/gM-05841/ "FTDI USBシリアル変換ケーブル(5V)")を流用するとかっこよくできるのですが、やや高いですし、実験用なのでこのくらいで十分かと。

材料はシンプルです。ルンバのシリアルコネクタに適合する[ミニDINプラグ 7P](https://www.marutsu.co.jp/pc/i/41258/ "ミニDINプラグ 7P")はマルツさんで買いました。

![roomba_serial_parts1.jpg](images/roomba_serial_parts1.jpg)

これを組み合わせてUSB変換コネクタができました。

![roomba_serial_cable1.jpg](images/roomba_serial_cable1.jpg)

ルンバのシリアルコネクタに取り付けます。

![roomba_serial_connect1.jpg](images/roomba_serial_connect1.jpg)

PCでターミナルソフトを動かして、ルンバの電源をいれると無事情報が出力されました。

![roomba_serial_output1.jpg](images/roomba_serial_output1.jpg)

これで安定したシリアル接続ができそうです。
