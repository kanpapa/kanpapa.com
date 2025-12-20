---
title: "mbed FRDM-KL25Zで遊んでみた"
date: 2013-03-10
slug: "mbed-frdm-kl25z"
categories: 
  - "electronics"
image: "images/frdm-kl25z.jpg"
---

[freescale社のFRDM-KL25Z](http://www.chip1stop.com/dispDetail.do?partId=FREE-0028314)という評価ボードがmbedになるとのことなので試してみました。今回は２枚購入しました。

![frdm-kl25z.jpg](images/frdm-kl25z.jpg)

[mbedのサイト](https://mbed.org/handbook/mbed-FRDM-KL25Z-Getting-Started)にあるようにFRDM-KL25Zのファームウェアを書き換える必要がありますが、最初にMacのParallels DesktopにあるWindows7の環境で書き換えようとしたのですが、どうも不安定で書き込めたとおもっても書き込めていなかったりしてしまいました。

しかたないので、ThinkPadのWindows8でファームウェアを書き込んだところ、一発で書き込めてmbedに変身しました。

mbed.orgのコンパイラには「Freescale KL25Z」という選択肢が増えているので、それを選び[Lチカのプログラム](https://mbed.org/handbook/Creating-a-program)を動かしたところ、LEDが点滅をはじめました。

この評価ボードはArduinoのピン配置を意識したものになっていて、mbedコンパイラでもArduinoのD0〜D13とA0〜A5の名前を使うことができます。

DigitalOut d0(D0);  
DigitalOut d1(D1);

折角ですので、ピンソケットをハンダ付けして、先日ハンダ付けした[Decoシールド](http://dev.tetrastyle.net/2012/08/deco.html)を取りつけて点滅するプログラムを書きました。

{{< youtube WBrRLDG2JWI >}}

ついでにKL25Zに搭載されているタッチセンサーの値を読み取って、点滅速度が変化するようにしてみました。他にもKL25Zのデバイスが利用できる[サンプルプログラム](https://mbed.org/handbook/mbed-FRDM-KL25Z-Examples)がすでに準備されているので参考になります。

{{< youtube GEPzYs1QkFo >}}

今回作成したプログラムは[http://mbed.org/users/kanpapa/code/FRDM\_Deco/](http://mbed.org/users/kanpapa/code/FRDM_Deco/)においておきます。

このようにArduinoのシールドを活用して楽しむことができそうです。
