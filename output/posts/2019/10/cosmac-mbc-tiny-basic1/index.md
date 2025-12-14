---
title: "COSMAC MBCでTINY BASICが動きました"
date: 2019-10-13
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
coverImage: "tinybasic_checklist.jpg"
---

なんとか[COSMAC MBC](https://kanpapa.com/cosmac/blog/2019/10/cosmac-mbc-sample1-run.html "COSMAC MBC")が動き出したところで[Evaluation Kit Manual for the RCA CDP1802 COSMAC Microprocessor](http://bitsavers.trailing-edge.com/components/rca/cosmac/MPM-203_CDP1802_Evaluation_Kit_Manual_Sep76.pdf "Evaluation Kit Manual for the RCA CDP1802 COSMAC Microprocessor")に掲載されているCOSMAC TINY BASICを動かしてみました。マニュアルには16進数がならんでいるダンプリストが提供されています。

![](images/cosmac_tiny_basic_dumplist.jpg)

参照しているPDFマニュアルにはOCRで文字データが含まれているので、まずはOCRの読み取りを信用してテキストファイルにしましたが、読み取りミスが必ずあるはずです。このため、昔のようにリストをにらめっこして誤りを修正しました。やはり数バイトの読み取りミスがみつかりました。

![tinybasic_checklist.jpg](images/tinybasic_checklist.jpg)

これを修正して、UT4が書き込める形式にしてメモリに書き込みます。書き込みは600bpsで行いましたが2K byteでも数分かかります。

```
*!M0000 0130B0C000EDC0066FC00676C006665F*!M0010 188280203022302058D5068108C80008*!M0020 483897BA48D5C00651D3BFE286739673*!M0030 83A693B646B346A39F3029D3BFE296B3*!M0040 86A31242B602A69F303BD343ADF808BD
```

読み込みが完了したところで、UT4モニタから起動したところ、TINY BASICのプロンプトの「 : 」が無事表示されました。

```
*$P0:
```

早速Hello Worldです。

```
:10 PRINT "HELLO WORLD":LIST10 PRINT "HELLO WORLD":RUNHELLO WORLD!85 AT #0:20 END:LIST10 PRINT "HELLO WORLD"20 END:RUNHELLO WORLD:
```

暴走することもなくとりあえず動いたようです。TINY BASICですので、最低限のことしかできませんが、一応動いたということで。

他にも面白いアプリケーションがないか探してみようと思います。
