---
title: "LPCXpresso LPC1768にVFDを接続してみました"
date: 2011-10-31
slug: "vfd-lpcxpresso-lpc1768"
categories: 
  - "electronics"
image: "images/VFD_LPCXpresso.jpg"
---

[mbed](http://akizukidenshi.com/catalog/g/gM-03596/)にVFDを接続して遊んでいましたが、mbedと同じマイコンが載っている[LPCXpresso LPC1768](http://akizukidenshi.com/catalog/g/gM-04117/) にVFDを接続してみました。 プログラムはmbedサイトでコンパイルしたバイナリをLPCXpresso-IDEを使って、LPCXpresso LPC1768に書き込みました。 microSDカードは[SparkFunのマイクロSDカードスロット・ピッチ変換基板](http://www.switch-science.com/products/detail.php?product_id=36)を使って接続しています。 LPCXpressoは基板に少し幅があるので、[少し大きめのブレッドボード](http://akizukidenshi.com/catalog/g/gP-00284/)を使うしかありません。もう少し小さいと良いのですが。 とりあえずVFDとの接続はmbedと同様にして、内蔵LEDのポートだけLPCXpressoに合わせたところ問題なく動作しました。 microSDカードからBMPを読み込んで表示するだけであればこれで十分ですし、ブレッドホードの空きスペースには+70VのDC-DCコンバータを組むことができそうです。 mbed + StarBoard Orangeはネットワークに接続して使うことにしましょう。 ![VFD_LPCXpresso.jpg](images/VFD_LPCXpresso.jpg) これでMTM07のネタが１つできました。
