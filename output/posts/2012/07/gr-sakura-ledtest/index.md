---
title: "GR-SAKURAをiMacで動かしてみました"
date: 2012-07-29
categories: 
  - "electronics"
coverImage: "GR-SAKURA10.jpg"
---

GR-SAKURAボードをiMacに接続して動作確認をしてみました。

GR-SAKURAボードをUSBケーブルでiMacに接続したところ、４つのLEDが点灯しました。

![GR-SAKURA10.jpg](images/GR-SAKURA10.jpg)

次に茶色のプッシュスイッチを押したところ、ドライブとして認識されました。

![GR-SAKURA11.jpg](images/GR-SAKURA11.jpg)

mbedと同じようにドライブの中にはHTMLファイルがあってそれをクリックすると、[sakuraboard.net](http://sakuraboard.net) が表示されました。

Webコンパイラを使うためにはMyRenesasに登録しなければいけませんが、私の場合はすでに登録済みなのでそのまま説明書通りにWebコンパイラを起動。

sketch.binができたところで、mbedと同じようにGR-SAKURAのドライブにコピーしたところ、LEDの点灯パターンが変わりました。

このようにiMacでも特に問題なく動作しました。

まだ細かいところは触っていませんが、Arduino互換なので手持ちの各種ボードが使えることに期待しています。
