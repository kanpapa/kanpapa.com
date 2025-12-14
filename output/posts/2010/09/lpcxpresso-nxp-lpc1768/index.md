---
title: "LPCXpresso NXP LPC1768評価キットをいじってみる"
date: 2010-09-19
categories: 
  - "electronics"
tags: 
  - "mbed"
coverImage: "lpcxpresso-lpc1768.jpg"
---

秋月で[LPCXpresso NXP LPC1768評価キット](http://akizukidenshi.com/catalog/g/gM-04117/)を買ってきました。mbedで開発したバイナリがそのまま動くという話なので。  
ボードはこんな感じ。写真にも写っていますが、小さい水晶発振子が飛び出ているので注意しましょう。

![](images/lpcxpresso-lpc1768.jpg)

開発環境はWindows用なので、MacのParallels Desktopで動いているWindows XPにインストールして無事動きました。サンプルのLEDチカチカも問題なく動作。  
とりあえず添付のヘッダピンをハンダ付けしてブレッドボードに差して遊んでみたいと思います。  
ちなみにmbedで開発したバイナリを動かす方法は、@nxpfanさんが詳しくまとめています。

- [mbed (LED blink) code on LPCXpresso-LPC1768](http://mbed.org/users/nxpfan/notebook/mbed-led-blink-code-on-lpcxpresso-lpc1768/)

開発はmbedで、応用はこのボードでと使い分けができそうです。  
追記：mbedとLPCXpresso NXP LPC1768では、EthernetのPHYチップが異なるのでその部分の互換性はないそうです。ちなみにmbedはNS社のDP83848J、LPCXpresso NXP LPC1768はSMSC社のLAN8720を使っています。
