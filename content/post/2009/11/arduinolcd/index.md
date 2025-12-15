---
title: "Arduino用のLCDシールドを作る"
date: 2009-11-23
slug: "arduinolcd"
categories: 
  - "electronics"
image: "images/lcd_shield.jpg"
---

Make: Tokyo Meeting 04で、スイッチサイエンスさんから購入した[Proto sheld v.4](http://www.switch-science.com/products/detail.php?product_id=12)と[Arduinoシールド用ピンソケットのセット](http://www.switch-science.com/products/detail.php?product_id=246)を使って、ArduinoのLCDシールドを作ってみました。  
これまでは、ブレッドボード上に組んでいましたが、今後もよく使うと思うのできちんとしたものにしました。LCDは秋月の小型LCDです。

![](images/lcd_shield.jpg)

LCDシールドは表示が見えるように一番上に載せることになるので、リセットスイッチがあるのは便利です。  
バックライトはショートピンで点灯／消灯が選択できるようにしました。  
Arduinoとの接続はピンヘッダからジャンパピンでD2からD7に接続していますが、必要があればジャンパピンを外して、メスーオスのケーブルで他のデジタルポートに接続できるようにしています。  
とりあえずLM73をつないで温度計にしました。快調に稼働しています。
