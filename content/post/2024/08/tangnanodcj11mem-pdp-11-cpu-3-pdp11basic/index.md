---
title: "TangNanoDCJ11MEMとPDP11GUIでPDP-11 BASICを動かしてみました"
date: 2024-08-02
slug: "tangnanodcj11mem-pdp-11-cpu-3-pdp11basic"
categories: 
  - "pdp-11"
  - "retrocomputing"
tags: 
  - "dcj11"
  - "fpga"
  - "pdp-11"
  - "tang-nano"
  - "tangnanodcj11mem"
image: "images/tangnanodcj11mem-ptapebasic-running1.jpg"
---

[前回のbaremetal編](https://kanpapa.com/2024/07/tangnanodcj11mem-pdp-11-cpu-2-bare-metal.html)では[TangNanoDCJ11MEM](https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main)に搭載したDCJ11 CPUがbare metal環境で動作することを確認しました。同時に[PDP11GUI](https://www.retrocmp.com/tools/pdp11gui)というツールでODTを活用できそうだということを紹介しました。今回はPDP11GUIを使ってPDP-11 BASICを動かしてみました。なお、TangNanoDCJ11MEMのapplicationでは[tapebasic](https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/tapebasic)をSDカードからロードする方法が公開されています。

この実験を行う場合はTangNanoDCJ11MEMのbare metal環境で行ってください。unix-v1環境だと動作しません

## PDP-11とPaper tape software

PDP-11でプログラムを実行させる際にデータが記録されている紙テープを紙テープリーダーで読み込んでメモリにプログラムをロードすることを行っていました。当時の紙テープのデータをまとめたアーカイブが存在します。

https://www.vaxhaven.com/Paper\_Tape\_Archive

この紙テープデータを読み込む機能がPDP11GUIにありますので、それを使ってみます。

## PDP11GUIでの紙テープデータの読み込み

今回読み込む紙テープソフトウェアはBASICにします。先ほどのアーカイブサイトではPDP-11 BASIC V007A SA=16104 RA=0と書かれているものになります。ファイル名は[DEC-11-AJPB-PB.ptap](https://www.vaxhaven.com/images/c/c2/DEC-11-AJPB-PB.ptap)ですのでこれをダウンロードします。

次にPDP11GUIのメニューにあるMemoryからMemory Loaderを選択すると次のような画面が表示されます。

![](images/pdp11basic_tape_image1.png)

ここでFile formatでファイル形式を指定します。様々な形式のファイルフォーマットが使えますが、紙テープデータの場合は「Stansard Absolute Paper Tape image」を選択します。そのあと紙テープのイメージファイル名を指定して、Loadボタンを押すと紙テープイメージデータが読み込まれ、読み込まれたデータが表示されます。

![](images/pdp11basic_tape_image2.png)

このイメージデータをメモリ上にロードするためにDeposit allボタンを押すと、Terminal画面でODTを使って1ワードずつメモリに書き込みが行われます。

![](images/pdp11basic_tape_image3.png)

データの読み込みに時間がかかってしまいますが、紙テープを読み込んでいる時間と思えば良いかもしれません。私の場合は115200bpsで約４分かかりました。

## PDP-11 BASICの起動

ロードが完了したら、Memory Loader画面のEntry addr:に表示されている値が実行開始アドレスです。PDP-11 BASICは016104でした。

![](images/pdp11basic_entry_addr1.png)

Terminalから実行開始アドレスを指定してGコマンドを入力します。うまく読み込めていれば以下のような表示になります。

```
@016104G
PDP-11 BASIC, VERSION 007A
*O 
```

そのままEnterを押してもREADYとなりますが、以下のように?を入力することでオプションを指定できます。オプションについては後述のマニュアルを参照してください。

```
*O ?
DO YOU NEED THE EXTENDED FUNCTIONS? N
DO YOU REQUIRE EXP OR LOG (FLOATING ^)? N
HIGH-SPEED READER/PUNCH? N
SET UP THE EXTERNAL FUNCTION? N
MEMORY? 16
READY
```

これでBASICが使える状態になりました。テストプログラムを入力して実行してみます。

```
10 PRINT "HELLO WORLD"
RUN
HELLO WORLD

STOP AT LINE   10
READY
```

HELLO WORLDと表示することができました。

## PDP-11 BASICを使ってみる

PDP-11 BASICのマニュアルは以下にあります。実数も使えるBASICです。

[https://retrocmp.com/attachments/article/254/DEC-11-AJPB-D\_PDP-11\_BASIC\_Programming\_Manual\_Dec70.pdf](https://retrocmp.com/attachments/article/254/DEC-11-AJPB-D_PDP-11_BASIC_Programming_Manual_Dec70.pdf)

PDP-11 BASICでいつもの[ASCIIART(マンデルブロ集合)ベンチマーク](http://haserin09.la.coocan.jp/asciiart.html)を実行してみようとしたのですが、PDP-11 BASICにおいて以下の制約があるためやむなくプログラムを改変して実行しています。このため実行時間はあくまでも参考値としてください。

- 変数名は英字一文字もしくは英字一文字の後に一桁の数字
- 変数の代入には必ずLET文が必要
- CHR$()は存在しない
- PRINT文で表示する際に72文字目で強制的に改行されてしまうのでX軸を少し短くしました（ラインプリンタの仕様？）

上記の条件を考慮したプログラムです。オリジナルからは大きく変更しています。

```
10 FOR Y=-12 TO 12
20 FOR X=-39 TO 32           ←出力文字列が72文字を超えないように変更
30 LET C1=X*0.0458
40 LET C2=Y*0.08333
50 LET A=C1
60 LET B=C2
70 FOR I=0 TO 15
80 LET T=A*A-B*B+C1
90 LET B=2*A*B+C2
100 LET A=T
110 IF (A*A+B*B)>4 THEN GOTO 200
120 NEXT I
130 PRINT " ";
140 GOTO 210
200 GOSUB 300
210 NEXT X
220 PRINT
230 NEXT Y
240 END
300 IF I=0 THEN PRINT "0";　←CHR$()の代用ルーチン
310 IF I=1 THEN PRINT "1";
320 IF I=2 THEN PRINT "2";
330 IF I=3 THEN PRINT "3";
340 IF I=4 THEN PRINT "4";
350 IF I=5 THEN PRINT "5";
360 IF I=6 THEN PRINT "6";
370 IF I=7 THEN PRINT "7";
380 IF I=8 THEN PRINT "8";
390 IF I=9 THEN PRINT "9";
400 IF I=10 THEN PRINT "A";
410 IF I=11 THEN PRINT "B";
420 IF I=12 THEN PRINT "C";
430 IF I=13 THEN PRINT "D";
440 IF I=14 THEN PRINT "E";
450 IF I=15 THEN PRINT "F";
460 RETURN
```

こちらを実行すると以下のような結果になりました。CPUクロックが18MHzのときは、実行時間は8分14秒でした。

![](images/pdp11basic_asciiart1.png)

## まとめ

今回はPDP-11 BASICを動かしてみましたが、PDP11GUIのMemory Loader機能は紙テープデータだけでなくテキストで書かれた８進数のリストファイルなど様々な形式のファイルを扱うことができます。PDP-11のいろいろな資産を手軽に活用できそうです。
