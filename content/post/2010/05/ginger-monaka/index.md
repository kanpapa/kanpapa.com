---
title: "Ginger-Monakaキットを組み立てました"
date: 2010-05-23
slug: "ginger-monaka"
categories: 
  - "electronics"
tags: 
  - "garageband"
  - "ginger"
  - "ginger-monaka"
  - "mac"
  - "make05"
  - "midi"
  - "monaka"
  - "mtm05"
image: "images/ginger_monaka_test01.jpg"
---

Make 05で購入したmorecat lab.さんのGinger-Monakaキットを組み立てました。  
パーツも多くなく基板もしっかりしたものなので、morecat lab.さんのサイトにある回路図を見ながら、そんなに時間もかからずハンダ付けできました。  
キットの内容はこんな感じです。

![ginger_monaka_parts.jpg](images/ginger_monaka_parts.jpg)

早速動作確認をするためにMacに接続し、システムプロファイラでUSB機器として認識していることは確認できました。  
GarageBandを立ち上げて、Ginger-Monakaのタクトスイッチを押すと、B2の音が出ました。Ginger-MonakaからのMIDI出力は問題なさそうです。  
次にGinger-MonakaのMIDI入力を確認しようと、とりあえずCONFIG\_1にして、8Poly Outputの端子（音でいうとC3からG3)に7セグメントのLEDを接続しました。LEDを鍵盤のように並べても良かったのですが、動作確認なので手元にあったもので代用です。  
この7セグメントLEDはアノードコモンだったので、NOTE OFFだとLレベルとなり全部のLEDが点灯します。NOTE ONだとHレベルとなり、その部分のLEDが消えることになります。  
早速GarageBandでMIDI出力をしようとしたのですが・・・・。これってできないのですね。出力はソフトウェア音源だけのようです。（知らなかった）  
手持ちのMIDIキーボードをつなげようかと思いましたが、USB変換コネクタが必要で断念。いろいろ調べたところ、MacにはAudio MIDI設定というユーティリティがあり、それでMIDI機器の管理ができるとのこと。早速動かしたところGinger-MonakaがMIDI入出力機器ということで認識されていました。  
このユーティリティにはMIDI設定のテスト機能もあり、装置のアイコンのポートの矢印をクリックすることで、Ginger-MonakaのLEDが点灯してくれました。また、ポートに対応したNOTE ONが偶然流れてきたら7セグメントのLEDが消えました。問題なく動いているようです。  
テスト中の風景はこちら

![](images/ginger_monaka_test01.jpg)

今度は変換ケーブルを準備して、手持ちのMIDIキーボードをつないでみたり、他のCONFIGも試してみたいと思います。

追記：midiOというプラグインでGarageBandからMIDI出力ができました。もちろんMonakaも動作確認できました！
