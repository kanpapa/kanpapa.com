---
title: "ArduinoでWebサーバを動かす"
date: 2009-06-27
slug: "arduinoweb"
categories: 
  - "electronics"
tags: 
  - "arduino"
  - "web"
image: "images/arduino_ether1.jpg"
---

[Arduinoのイーサーネットシールド](http://www.switch-science.com/products/detail.php?product_id=69)を[スイッチサイエンス](http://www.switch-science.com/)さんで購入しました。  
[スイッチサイエンス](http://www.switch-science.com/)さんは価格も安くいつも迅速に発送していただけるので感謝しています。  
早速、Arduinoに接続してみました。写真のように親亀の上に子亀が乗るようなスタック構造になります。

![](images/arduino_ether1.jpg)

スケッチはサンプルにあるLibrary-EthernetのWebServerを修正して使います。  
このサンプルスケッチの行数はコメント込みで60行程度しかありません。削ればもっと短くできます。かなりコンパクトなものですが、十分実用的に使えるものです。  
自分のArduinoで動かすためにはスケッチを２箇所修正する必要があります。

1. MACアドレスを指定する。（スイッチサイエンスさんではMACアドレスがついてきます。）
2. IPアドレスを指定する。（これは自宅ネットワークに合わせます。）

あとは、Arduinoにアップロードして、指定したIPアドレスをWebブラウザで表示すると、アナログポートの値が表示されます。

![](images/arduino_ether2.jpg)

このようにWebサーバとしての骨組みがすでにできているので、あとは表示したい情報をお好みで変えるだけです。  
サンプルにはChatServerとかもありましたので、あとで実験してみたいと思います。
