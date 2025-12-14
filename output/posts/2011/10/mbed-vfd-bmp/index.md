---
title: "mbedでBMPファイルを読み込んでVFDに表示してみました"
date: 2011-10-18
categories: 
  - "electronics"
tags: 
  - "mbed"
  - "vfd"
coverImage: "mbed-vfd-bmp-sample1.jpg"
---

最近はまっているジャンク品のVFDいじりですが、もう少し汎用的に使うために標準的な画像データを表示できないかと考えました。  
たとえば、Windowsのペイントで書いたものが、そのままVFDに表示できればいろんな使い道ができそうです。  
BMPフォーマットを扱っているプログラムがないかなとmbedサイトで探したところ、@tedd\_okanoさんの、[bmp\_8bit\_per\_pixel\_format](http://mbed.org/users/okano/programs/bmp_8bit_per_pixel_format/ll6blp/docs/main_8cpp_source.html)というテストプログラムがみつかりました。これだと8bit color用なので、このソースとBMPフォーマットの資料を見ながら、1bit color用に書き換えました。  
試しにモノクロBMPファイルを作成して、mbedのローカルストレージにコピーし、読み込ませて数字の「０」、「１」として画面に表示したところ、上下が反転したイメージデータを確認できました。この上下が反転しているのはBMPフォーマットの仕様のようです。  
これをVFDに転送すればいいのですが、ドットの並びがBMPは横方向、VFDは縦方向になっている点と、上下反転の仕様がありますので、ちょっとした変換ロジックをかませてからVFDに転送することで表示することができました。  
電車が好きな息子が電車の方向幕を表示してみたいということなので、Windowsのペイントで書いてもらいデータ化しました。それを表示したところ本物の電車の方向幕の雰囲気です。うまくできたので他にもいろいろな方向幕を作っているようです。

![](images/mbed-vfd-bmp-sample1-1024x765.jpg)

https://youtu.be/IOvl0Jce5NA

  
今回はお手軽にUSB経由でストレージにBMPデータを置きましたが、今使っているmbedのベースボードStarBoard☆Orangeには、microSDカードのスロットもありますので、そちらからデータを取り込むのも良いかなと思います。
