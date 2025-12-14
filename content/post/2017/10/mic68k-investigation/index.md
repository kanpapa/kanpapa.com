---
title: "MIC68Kワンボードコンピュータで遊んでみた（１）調査編"
date: 2017-10-22
slug: "mic68k-investigation"
categories: 
  - "68000"
  - "retrocomputing"
tags: 
  - "mic68k"
image: "images/mic68k_board1.jpg"
---

ヤフオクで68000CPUが搭載されたレガシーなワンボードコンピュータが出品されていたので落札しました。出品情報によると「MIC68K」という名称のようです。まずはどんなワンボードコンピュータなのか基板を観察してみます。

![mic68k_board1.jpg](images/mic68k_board1.jpg)

基板の中央に68HC000P8が構えています。今ではこんな巨大なICは見る機会はないでしょう。あとは256KbitのSRAMが２つ。8bit×2個で16bitバスに接続されているのでしょう。２つの空きソケットがありますが、ここにはROMを実装するものと思われます。SRAM同様に256KbitのROMが搭載できるでしょう。

<!--more-->

あとは63B40P(PTM: Programmble Timer Module)、63B50P(ACIA:Asynchronous Communications Interface Adapter)が２つ、63B21P (PIA:Peripheral Interface Adapter)と8bit系の周辺デバイスが並んでいます。接続端子はRS232CとRS485ですので、63B50Pがそれぞれ接続されているはずです。

ここでの特徴としてはすべて68系の8bit周辺デバイスを使っていて、68000系の16bit周辺デバイスは使われていないことです。これは学習用としてシンプルかつ安価にするためと思われます。

電源端子は+5Vの単一電源です。RS232CまわりはMAX232を使って単一電源化しています。クロックはEXO-3が２つ使われています。１つは16MHz。これは1/2分周で8MHzのCPUクロックでしょう。もう１つは19.660MHz。この周波数は1024分周するとほぼ19.200KHzになります。これはシリアル通信のクロックとして使われているはずです。

他は一般的なロジックICが並んでいます。74HC138, 74HC139あたりはアドレスデコーダまわりでしょう。見た限りだと68000CPUを除けば現在でも入手できるICが多く、万が一故障しても保守性は良いと思われます。

次にWeb検索でMIC68Kを検索したところ、情報は少ないのですが、1983年6月のCHINA COMPUTERWORLDにMIC-68Kという名前のワンボードコンピュータを取り上げた記事がありました。

```
JIAOTONG UNIVERSITY'S 16-BIT SINGLE-BOARD MICROCOMPUTERS INTRODUCED
Beijing JISUANJI SHIJIE [CHINA COMPUTERWORLD] in Chinese No 11,  5 Jun 83 p 1
[Article: "Shanghai Jiaotong University Has Assembled Two Types of
 16-Bit Single-BoardMicrocomputers"]
[Text] The Microcomputer Laboratory of Shanghai Jiaotong University recently
introduced the MIC-68K and the MIC-8K2 16-bit single-board microcomputers.
The MIC-68K is built around a 68000 microprocessor with 32K RAM and
16K-32K EPROM, and has high numeric and real-time processing capabilities.
One feature is that all the supporting circuits for the 16-bit CPU
are 8-bit I/O chips.
Its peripherals include a CRT terminal, a line printer, a cassette recorder
and an EPROM programmer. The entire single-board is 305 mm x 200 mm x 15 mm,
uses +5volts (800 milliamperes), +12 volts (50 milliamperes), -12 volts
 (50 milliamperes).
As an OEM product, the MIC-68K can be applied to process control,
real-time processing, education, etc.
The MIC-68K can be used as a development tool for the 16-bit microcomputers.
```

今回の基板はこの記事のワンボードマイコンではないかと考えられますが、電源が単一電源となっていることから若干異なります。また、当時主流だったTTLデバイスではなく、CMOSデバイスが使われていたり、1987年に発表されたMAX232が使われていることから、改良版なのではないかと思われます。

目視による簡単な調査はここまでです。このあとこの基板を動かすために詳細な調査を行っていきます。

続きは[解析編](https://kanpapa.com/2017/10/mic68k-schematic.html "MKC68K解析編")で。
