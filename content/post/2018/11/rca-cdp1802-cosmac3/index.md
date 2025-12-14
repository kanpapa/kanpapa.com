---
title: "RCA CDP1802 COSMACを動かしてみた(3) アセンブラ編"
date: 2018-11-23
slug: "rca-cdp1802-cosmac3"
categories: 
  - "cosmac"
  - "cosmac-toy"
tags: 
  - "cosmac-toy"
---

[ブレッドボードに組み上げたCOSMACマイコンの動作確認](https://kanpapa.com/cosmac/blog/2018/11/rca-cdp1802-cosmac2.html "COSMAC 動作確認")ができましたので、参考にしている書籍「トラ技別冊　つくるシリーズ７　手作りコンピュータ入門」にあるサンプルプログラムを動かしていこうと思います。

前回の記事で動作確認に使用したパルス信号を作るプログラムも書籍に掲載されているものです。ただし掲載されているプログラムリストには命令コードと命令が行う処理の概要は書かれていますが、二ーモニックコードが書かれていません。どうせならアセンブラを使っていきたいので、[データシート](http://www.intersil.com/data/fn/fn1441.pdf "CDP1802A datasheet")からニーモニックコードを調べてアセンブラのソースコードを作成しました。

```
START SEQ      REQ      BR START
```

SEQ は SET Q、REQ は RESET Q、BRはBRANCHと想像がつきますね。

次にCOSMACをサポートしているアセンブラを探してみましたが、私がよく利用している[SB-Assembler](https://kanpapa.com/2018/08/sb-assembler-v3.html "SB-Assembler v3")がサポートしているようです。早速SB-Assemblerのソース形式でアセンブルしてみました。今回はWSL環境上で行いました。

```
$ sbasm osc1.asm
SB-Cross Assembler version 3.03.01
Please visit www.sbprojects.net for a complete description.
Assembling....
Pass one
Loaded 1802 overlay version 3.01.00
Pass two
0000- 1       *
0000- 2       * Oscillator program 1 for COSMAC
0000- 3       * SB-Assembler
0000- 4       *
0000- 5             .CR 1802     To load the 1802 cross overlay
0000- 6             .OR $0000
0000- 7 *
0000-7B         8 ( 2)  START SEQ          1->Q
0001-7A         9 ( 2)        REQ          0->Q
0002-30 00     10 ( 2)        BR START     M(R(P))->R(P).0
0004- 11
0004- 12            .EN
0 Errors found during assembly.
0 Warnings found during assembly.
$
```

正常にアセンブルできているようです。このソースファイルは[github](https://github.com/kanpapa/cosmac/blob/master/osc1.asm "osc1.asm")においておきました。

この[アセンブラ開発環境でプログラミング](https://kanpapa.com/cosmac/blog/2018/12/rca-cdp1802-cosmac4.html "RCA CDP1802 COSMACを動かしてみた(4) プログラミング編")を進めてみます。
