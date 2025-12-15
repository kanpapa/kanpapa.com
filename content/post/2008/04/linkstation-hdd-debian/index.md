---
title: "LinkStation LS-H250GLのHDDをDebian PCにつなぐ"
date: 2008-04-30
slug: "linkstation-hdd-debian"
categories: 
  - "server"
---

LS-H250GLから外したHDDを実験用PCに接続します。

以降の作業は、山下さんの [LinkStation／玄箱 をハックしよう](http://www.yamasita.jp/linkstation/index.html)を参考にさせていただいております。

もちろん、作業は自己責任でお願いします。

実はS-ATAなるHDDを触るのはこれが初めてだったりします。これまではずっとIDEだけでした・・・。

とりあえず、PCのブートディスクをDebian 4.0がインストールされているものにします。うちのデスクトップPCは実験用なのでブートディスクを簡単に交換できるようにしているのです。

うちのAthlon64デスクトップPCです。

![](images/linkstation_hdd_debian_20080429072136.jpg)

材料はこれだけ。HDDはLinkStationから取り外したもの。ケーブル類はマザーボードの付属品です。

![](images/linkstation_hdd_debian_20080429072414.jpg)

こんな感じでS-ATA HDDを接続しました。

![](images/linkstation_hdd_debian_20080429072628.jpg)

この状態で、PCのブートディスクからDebianを起動します。果たしてS-ATA HDDを無事認識してくれるのか？

![linkstation_hdd_debian_20080501000833.jpg](images/linkstation_hdd_debian_20080501000833.jpg)

キター！！
