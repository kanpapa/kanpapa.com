---
title: "ガイガーカウンタをmbedにつないでみた"
date: 2011-04-03
slug: "geiger-counter-mbed"
categories: 
  - "electronics"
image: "images/geiger-counter-mbed-1.jpg"
---

昨日[動くことを確認したガイガーカウンター(秋月のGM管 D3372)](https://kanpapa.com/2011/04/geiger-counter-1st.html)を[mbed](http://mbed.org/)に接続してみました。  
これでカウントすることもできますし、ネットワークに発信することも可能です。  
もちろん、[StarBoard Orange](http://mbed.org/cookbook/StarBoard-Orange)を使用しています。

![](images/geiger-counter-mbed-1-1024x765.jpg)

https://youtu.be/IREz5TelWbM

この映像は約１分間ですが、その間に４回検出があったことがわかります。D3372ではB.Gの検出はこれくらいになります。  
現在のプログラムはただカウントするだけなので、数字は増えるばかりですが、  
もう少しいじれば１分間あたり何回検出ということもできると思いますし、音を付けるのも良いかなと思います。
