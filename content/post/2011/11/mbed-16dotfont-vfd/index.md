---
title: "mbedで16ドットフォントをVFDに表示してみました"
date: 2011-11-03
slug: "mbed-16dotfont-vfd"
categories: 
  - "electronics"
tags: 
  - "mbed"
  - "vfd"
image: "images/vfd_fontx2_2.jpg"
---

FONTX2を使ってLCDに漢字を表示しているというツイートを見かけました。 FONTX2は様々なフォントが揃っていて、16ドットやそれ以上の大きさのフォントもあるので大画面(?)のVFDにはもってこいではと思いました。 またフォントファイルを差し替えることで、いろんなフォントに変えることもできるはずです。 さっそく、@gingaxxさんのツイートにあった[液晶の部屋](http://www31.atwiki.jp/gingax/pages/63.html)にリンクされている[mbedでのプログラム](http://mbed.org/users/akira/libraries/AD128160/lzhrax)を参考にさせていただき、VFDでも表示できるようにしました。 縦書きはこんな感じ。 ![vfd_fontx2_1.jpg](images/vfd_fontx2_1.jpg) 横書きはこんな感じ。 ![vfd_fontx2_2.jpg](images/vfd_fontx2_2.jpg) さすがに16ドットフォントなので読みやすいのですが、フォントデータはmicroSDカードに入っているので、若干表示に時間がかかります。 でも、掲示板などの用途であればこれで十分でしょう。 ただし、指定したコードと違う漢字が表示されているので、もう少し調整が必要です。 あくまでもテストプログラムですが、ソースは[こちら](http://mbed.org/users/kanpapa/programs/VFD_fontx2_test1/m03gnm)にpublishしておきました。 これをネットワークにつないで何かの情報を表示するようなものに仕上げてMTM07に持っていきたいと思います。
