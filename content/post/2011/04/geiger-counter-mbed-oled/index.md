---
title: "mbedガイガーカウンターの検出情報をOLEDに表示してみました"
date: 2011-04-10
slug: "geiger-counter-mbed-oled"
categories: 
  - "electronics"
image: "images/mbed_gm_oled2.jpg"
---

[mbedにMARYシステムのOB基板(OLED)が接続](https://kanpapa.com/2011/04/mbed-oled.html)できましたので、これに[先日製作した秋月のGM管を使用したmbedガイガーカウンター](https://kanpapa.com/2011/04/geiger-counter-mbed.html)の情報を出力してみました。  
最初はLCDに表示していた情報だけをOLEDに表示してみました。

![](images/mbed_gm_oled1.jpg)

  
これだとLCDとあまり変わらずに文字ばかりで面白くありません。  
そこで128×128ピクセルのフルカラーグラフィック表示を活用して、毎分の検出数をグラフ表示してみました。

![](images/mbed_gm_oled2.jpg)

プログラムなどはmbedの[Notebook](http://mbed.org/users/kanpapa/notebook/geiger-counter-mbed-oled/)にまとめておきました。  
実にわかりやすくなりました。  
使用している秋月のGM管 D3372では毎分２〜３回の自然放射線が検出されますが、このOLEDにより時系列で128分間の状況を一目で把握できるようになりました。
