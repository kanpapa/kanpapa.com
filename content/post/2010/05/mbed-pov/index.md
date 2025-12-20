---
title: "mbedに大人の科学の光残像キット(POV)を接続してみた"
date: 2010-05-29
slug: "mbed-pov"
categories: 
  - "research"
image: "images/mbed_pov.jpg"
---

大人の科学のJapaninoについてきたPOVをmbedに接続してみました。  
POVはJapaninoに接続するために、コネクタの部分がArduino仕様になっていて2.54mmピッチではうまく収まりません。そのため基板の途中をニッパでカットして二分割して、ブレッドボードに挿すことで解決しました。でも、基板のパターンにヒビが入ってしまったようで、その部分はハンダ付けで補強しました。  
POVのプログラムは[大人の科学.net](http://otonanokagaku.net/japanino/)で公開されていますので、それをmbed用に書き換えましたが、移植はそんなに難しくはありませんでした。wait値を微調整してうまく表示できるようになりました。

![](images/mbed_pov.jpg)

写真だけだといまいちなので、動画も載せておきます。

{{< youtube pE_U7iWvY9w >}}

mbedのプログラムは[こちら](http://mbed.org/users/kanpapa/programs/pov)にあります。もっと効率よい書き方ができそうな気もしますが、とりあえずこんな感じで。
