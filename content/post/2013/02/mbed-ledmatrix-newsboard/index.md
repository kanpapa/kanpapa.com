---
title: "mbedとLEDマトリクス基板でニュース掲示板を作ってみました"
date: 2013-02-08
slug: "mbed-ledmatrix-newsboard"
categories: 
  - "electronics"
image: "images/mbed-ledmatrix-newsboard-4-1.jpg"
---

以前[VFDによる電光掲示板](https://kanpapa.com/2011/11/mbedvfd-1.html "mbedとVFDでお天気情報を表示してみました")を作りましたが、このVFDはもう入手が厳しいようなので、今回は[秋月電子のLEDマトリクスユニッ](http://akizukidenshi.com/catalog/g/gK-03735/ "３２×１６ドットＬＥＤ電光掲示板用拡張表示ユニット")[­ト](http://akizukidenshi.com/catalog/g/gK-03735/ "３２×１６ドットＬＥＤ電光掲示板用拡張表示ユニット")を接続してみました。

mbedとの接続は簡単で、ダイナミック表示も容易に行うことができました。

ダイナミック表示テスト中の動画をYouTubeにアップしておきました。

https://youtu.be/L9M7tOVgrpI

この仕組みを使い、前回同様にmbedを直接インターネットに接続し、Yahoo!ニュースWebAPIでニュースのヘッドラ­インを表示しました。

https://youtu.be/CoNVTb788VE

この動画では３セットのLEDマトリクス基板を使っています。もう１セット増設できるのでそこまで拡張してみました。

![](images/mbed-ledmatrix-newsboard-4-1-1024x768.jpg)

また、今回は新しいネットワークライブラリとmbedのサイトに公開されている[spxml](http://mbed.org/users/hlipka/notebook/xml-parsing/ "XML parsing")や[expat](http://mbed.org/users/andrewbonney/code/expatlib/ "expatlib")などのXMLパーサを使ってみましたが、少しデータが多いとハングアップするので表示件数を絞っています。このあたりは試行錯誤中です。もし、使い勝手の良いXMLパーサーがあったらぜひ教えてください。
