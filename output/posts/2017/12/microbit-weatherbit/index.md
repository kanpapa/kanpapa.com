---
title: "weather:bitを使ってみた"
date: 2017-12-13
categories: 
  - "electronics"
tags: 
  - "micro-bit"
coverImage: "weather_bit1.jpg"
---

この記事は[microbit Advent Calendar 2017](https://qiita.com/advent-calendar/2017/microbit "microbit Advent Calendar 2017")の14日目の記事です。

[weather:bit](https://www.switch-science.com/catalog/3383/ "weather:bit")はmicro:bitのシールドで、気圧、湿度、温度などを測ることができるものです。

![weather_bit1.jpg](images/weather_bit1.jpg) <!--more-->

micro:bitのI2Cに非常に小さな気象センサーであるBME280が接続されるようになっています。

![weather_bit2.jpg](images/weather_bit2.jpg)

BME280は秋月電子の[BME280使用　温湿度・気圧センサモジュールキット](http://akizukidenshi.com/catalog/g/gK-09421/ "BME280センサーキット")にも使われています。

weather:bitには他にも各種気象センサーを接続することができるようですが、私はそこまで詳しくありませんので、今回はBME280だけ使ってみました。

プログラムは以下のようになりました。気圧、湿度、温度の値を簡単に取得することができます。このプログラムでは気温、湿度、気圧を順番に表示します。

![weatherbit.PNG](images/weatherbit.png)

この気象センサーをうまく使って気象データを収集することで、天気予報とかもできるかもしれませんね。
