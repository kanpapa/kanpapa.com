---
title: "COSMAC MicroBoard Computerが動き始めました"
date: 2019-10-03
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
coverImage: "cosmac_mbc1.jpg"
---

新たなプロジェクトである[COSMAC MicroBoard Computer](https://kanpapa.com/cosmac/blog/2019/09/cosmac-mbc-1.html "COSMAC MicroBoard Computer")のプリント基板が届きました。

![cosmac_mbc_pcb1.jpg](images/cosmac_mbc_pcb1.jpg)

早速実装しました。EEPROMに[UT4](http://www.retrotechnology.com/memship/UT4_rom.html "UT4")モニタを書き込んだものを載せています。

![cosmac_mbc1.jpg](images/cosmac_mbc1.jpg)

UT4モニタはソフトウェアでシリアル通信を行い、ターミナルを接続できます。今回はUSB-シリアル変換でPCに接続しました。

![cosmac_mbc2.jpg](images/cosmac_mbc2.jpg)

UT4のマニュアルによると、最初にCRを入力すると＊のプロンプトが表示され、UT4のコマンドが入力できるとのことでした。試作なので一発では動かないと思ったのですが・・・

![](images/cosmac_mbc_prompt.png)

300bpsでCRを入力したところ、プロンプトが表示されました。でもこの先コマンドを入力しても反応がありません。UT4自体は動いているようですが、何か問題があるようです。

これからトラブルシューティングを始めますのでお楽しみに。
