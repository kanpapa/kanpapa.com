---
title: "COSMACで割り込み許可にしたい場合はどうするか？"
date: 
2020-08-23
slug: "cosmac-interrupt-enable-tips"
categories:
  - "Retro Computing"
tags:
  - "cosmac"
  - "tips"
image: "images/cosmac_cdp1802ace.jpg"
---

Maker Faire Tokyo 2020の準備でお試しデモのシナリオを考えています。

最終的には[COSMAC VIP OS](https://kanpapa.com/2020/05/cosmac-vip-os-rom-reloc.html "COSMAC VIP OSをROMの空きエリアに移動しました")を起動し、16進キーボードで[CHIP-8](https://en.wikipedia.org/wiki/CHIP-8 "CHIP-8 - Wikipedia")の小さいプログラムを入力するわけですが、その前に[CHIP-8インタプリタを先にロード](https://kanpapa.com/2020/06/CHIP-8-with-VIP-ROM-D000.html "リロケートしたVIP OS ROMでCHIP-8が動くようにしました")しておく必要があります。

手順としては以下のようになります。

1. RESETする
1. RUN-UでMCSMP20を動かす
1. USBシリアルからCHIP-8インタプリタ($0000-)をロードする。
1. MCSMP20からCOSMAC VIP OSを起動する。
1. COSMAC VIP OSでCHIP-8のアプリケーションプログラムを$200から書き込む。
1. RESETする
1. RUN-PでCHIP-8インタプリタを起動し、CHIP-8アプリケーションが動く。
1. 入力ミスの場合は、RESET、RUN-Uで4.からやり直し

4.のステップでMCSMP20からVIP OSを動かしたところうまく動きません。なぜか画面が流れ続ける状態です。しかし、$0000にLong branchでVIP OSにジャンプするように書き込んで、RUN-Pで起動するとVIP OSは問題なく動きます。リセット直後の状態とMCSMP20のRコマンド実行の状態と何かが異なるようです。

[COSMAC CPUのデータシート](https://www.renesas.com/us/en/www/doc/datasheet/cdp1802ac-3.pdf "CDP1802AC/3 Datasheet")をみたところリセット後には以下の状態になるとあります。

- レジスタl,N,Qがリセットされる。
- lEがセットされる。（Interrupt-Enable：割り込み許可になる）
- データバスは0(Vss)になる。
- レジスタ X, P, R(0) がリセットされる。

また、MCSMP20のRコマンドでは

```
Raaaa Jump to aaaa with PC=0 X=0
```

となっているので、ジャンプ先のアドレスをR0に設定したあとに、X, Pをいずれも0とすることで指定アドレスから実行されるものと思われます。X, Pがいずれも0になるところはRESET後と同じです。そうなると違いはIEがセットされているかいないかです。MCSMP20では割り込みは使っているでしょうから、Rコマンドの前に割り込みを禁止にしている可能性が高いです。

また、リセットの項目には以下の記述がありました。

「メモリの0000番地に71, 0001番地に00 と書くとリセット直後に割り込み禁止にできる」

71はDlS命令です。機能としては、M(R(X))→ (X, P); R(X) + 1→R(X), 0→lE になります。

リセット直後の状態はXもPも0となり、R0が$0000となります。0000番地に書かれた71命令を実行すると、R0は命令の次のアドレスになりますので、$0001になります。0001番地には00が書かれているので、M(R(X))は0となり、0→X、0→Pとなります。もともとX=P=0なので何も影響はありません。その後R(X)がインクリメントされ、$0002となり次の命令を正常に読み込めます。同時にIEが0になるので割り込みを禁止にできます。

この使い方から考えて、割り込みを許可する場合は70のRET命令を同様に使えばよいはずです。

RET命令の機能は、M(R(X))→ (X, P); R(X) + 1→R(X), 1→lE です。70, 00と書けば割り込みを許可できます。

アセンブルすると以下のようになります。とりあえずテストなので$7000に置きました。

```
0000-            2             .TF   ie_enable.hex,int
0000-            3      *
0000-            4      * COSMAC IE enable program
0000-            5      * SB-Assembler
0000-            6      *
0000-            7             .CR   1802
7000-            8             .OR   $7000
7000-            9      *
7000-70         10 ( 2) START: RET         ; M(R(X))->(X,P); R(X)+1->R(X); 1->IE
7001-00         11             .DB   0
7002-C0 D0 00   12 ( 3)        LBR   $d000 ; Jump to COSMAC VIP OS
7005-           13      *
7005-           14             .EN
```

このプログラムをMCSMP20のRコマンドで実行したところ、VIP OSが正常に起動できるようになりました。

本来はDIS命令とRET命令は割り込みハンドラの中で使用されるものなのですが、リセット直後はXとPが両方0なのでこのような使いかたもできるわけです。よく考えられていると思います。
