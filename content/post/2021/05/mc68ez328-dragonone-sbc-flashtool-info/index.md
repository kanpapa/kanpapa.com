---
title: "MC68EZ328 DragonOne SBC用にフラッシュメモリ操作ツールを開発中"
date: 2021-05-04
slug: "mc68ez328-dragonone-sbc-flashtool-info"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/dragonone_flashtools_info1.png"
---

[無事モニタプログラムが動き始めた](https://kanpapa.com/2021/05/mc68ez328-dragonone-sbc-monitor-worked.html "MC68EZ328 DragonOne SBCでモニタプログラムが動きました") MC68EZ328 DragonOne SBCですが、次はフラッシュメモリへの書きこみテストが必要です。これがうまくできればスイッチONでモニタが動き、ゆくゆくはμCLinuxが動くようになるはずです。

### 公式サイトのフラッシュツールが動かない

まずは公式サイトに掲載されている[2flash-kh](https://github.com/kanpapa/MC68EZ328/tree/main/2flash-kh "2flash-kh")を動かしてみたのですが、残念ながらメニューが表示されずにハングアップして動きませんでした。私のgccのクロスコンパイル環境に問題があるのかもしれません。

gccの環境を見直すのは原因の切り分けに時間がかかると思われたので、フラッシュツールをシンプルな68000アセンブラで書くことにしました。ゼロから書くのは大変ですので、現在動作している[ChartreuseK/68k-Monitor](https://github.com/ChartreuseK/68k-Monitor)をベースとして、フラッシュメモリ操作機能を追加していきます。こうすると基本的なコマンドメニュー、文字列や16進数の表示などユーティリティがそのままつかえますし、将来的に68k-Monitorに組み込むこともできます。

### フラッシュメモリの情報を取得

2flash-khのソースとフラッシュメモリのデータシートを照らし合わせながら、実装を進めて、フラッシュメモリの情報が取得できるようになりました。

![dragonone_flashtools_info1.png](images/dragonone_flashtools_info1.png)

このDragonOne SBCでは、4Mbitx8のフラッシュメモリを２つ使い、上位バイトと下位バイトでチップが分かれているので、Manufactures Codeも上位と下位で２個のメモリの情報が取得できます。Manufacturers Codeの01はAMD、Device CodeのA3はAm29LV033Cを示します。また、The Common Flash Interface (CFI)の情報から"QRY"の文字列や、Device Sizeの情報から4MBと確認できました。

実は私はNORフラッシュメモリを直接操作するのは初めてでして、どのように書き込みや消去を行うのかという流れを理解する良い機会となっています。

ここまで動けば２個のフラッシュメモリは正常に接続できているでしょう。この調子で、Erase機能、Program機能をこのツールに追加していきます。
