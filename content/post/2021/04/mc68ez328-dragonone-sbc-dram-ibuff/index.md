---
title: "MC68EZ328 DragonOne SBCで8バイトのプログラムを動かしてみる"
date: 2021-04-30
slug: "mc68ez328-dragonone-sbc-dram-ibuff"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/dragonone_dram_analyze_readrep1.png"
---

DRAMへのアクセスの様子をロジアナで確認できるように8バイトのIBUFFで動かすことができるプログラムを書きました。bレコードにしてブートローダに読み込ませ実行できます。アセンブラは[EASy68K](http://www.easy68k.com/ "EASy68K")を使用しました。

ここでは$00000000番地にD0レジスタの内容を連続してREAD/WRITEするようにしました。繰り返すことでロジアナでも状態が確認しやすくなります。本来なら固定値を書き込みたいところですが、8バイトに納めるためにこのようにしています。

### WRITEプログラム

```
FFFFFFAA              7          ORG     $FFFFFFAA    ; instruction buffer locationFFFFFFAA              8  START:FFFFFFAA  11C0 0000   9          move.b  d0,$000000FFFFFFAE  60FA       10          bra     STARTFFFFFFB0             11  FFFFFFB0             12          END     START        ; last line of source
```

これをbレコードにすると次のようになります。

```
FFFFFFAA0811C0000060FAFFFFFFAA00
```

bレコードを読み込ませたあとにロジアナで見てみます。DWEがLのところが書き込み動作です。上位バイトのアクセスなので、CASHがLになります。D0はデータバスのbit0ですが、Lが繰り返し書き込まれていることがわかります。

![dragonone_dram_analyze_writerep1.png](images/dragonone_dram_analyze_writerep1.png)

### READプログラム

```
FFFFFFAA              7          ORG     $FFFFFFAA    ; instruction buffer locationFFFFFFAA              8  START:FFFFFFAA  1038 0000   9          move.b  $000000,d0FFFFFFAE  60FA       10          bra     STARTFFFFFFB0             11  FFFFFFB0             12          END     START        ; last line of source
```

これをbレコードにすると次のようになります。

```
FFFFFFAA081038000060FAFFFFFFAA00
```

bレコードを読み込ませたあとにロジアナで見てみます。RASがLになり、CASHがLになっているところがREADです。WRITEと同じように繰り返されています。読み出された(?)データバスのbit0はHになっているようです。

![dragonone_dram_analyze_readrep1.png](images/dragonone_dram_analyze_readrep1.png)

これでタイミングも計りやすくなったので、仕様に沿っているか確認してみます。
