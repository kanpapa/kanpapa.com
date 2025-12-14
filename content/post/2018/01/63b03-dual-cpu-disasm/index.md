---
title: "63B03デュアルCPUマイコンボードで遊んでみた（２）解析編"
date: 2018-01-17
slug: "63b03-dual-cpu-disasm"
categories: 
  - "retrocomputing"
tags: 
  - "63b03"
image: "images/63b03_intelhex_binary.png"
---

[前回](https://kanpapa.com/2018/01/63b03-dual-cpu-board-1.html "63B03デュアルCPUマイコンボードで遊んでみた（１）調査編")はROMデータの読み込みまでを行いました。このROMデータの解析を行ってこのマイコンボードの仕様を探ります。しかし、63B03の開発環境は持っていませんので、インターネットにある情報から開発環境の整備を行います。今回はWindows10 Home 64bitのPCで作業をおこなっています。

ROMから読みだしたデータはIntel HEX形式のフォーマットになっているので、これをバイナリファイルに変換します。

プログラムはVectorのサイトで見つけた以下のプログラムを使用しました。

- [Binary data<->Intel Hex data Converter](http://www.vector.co.jp/soft/dl/win95/util/se057995.html "Binary data<->Intel Hex data Converter")

こちらにROMから読みだしたデータを与えて、バイナリファイルに変換します。

![63b03_intelhex_binary.png](images/63b03_intelhex_binary.png)

これでバイナリファイルができました。

<!--more-->

次にこのバイナリファイルを解析するために逆アセンブラが必要です。63B03と逆アセンブラというキーワードで検索したところ以下のプログラムが見つかりました。

- [DASMx Version 1.40](http://myweb.tiscali.co.uk/pclare/DASMx/ "DASMx Version 1.40")

早速バイナリファイルを逆アセンブラにかけてみます。

![63b03_dasmx.png](images/63b03_dasmx.png)

ここで生成されたソースをのぞいてみますが、逆アセンブラとはいっても万能ではありません。コード部分とデータ部分は意識されていない解析結果になります。ただし、ここで知りたいのはプログラムの動きというよりは、このマイコンボードがどのように初期化されるか、メモリマップがどうなっているのかがポイントになります。

63B03の場合、ROMの$FFF0からが割り込みベクタですので、そこから見ていきましょう。

この逆アセンブラはCPUアーキテクチャを意識して、$FFF0からは割り込みベクタとして解析してくれました。

```
 6022 FFF0                         org      $FFF0
 6023                   ;
 6024 FFF0              sci_vector
 6025 FFF0 A84C                    FDB      sci_entry
 6026 FFF2              tof_vector
 6027 FFF2 A84C                    FDB      sci_entry
 6028 FFF4              ocf_vector
 6029 FFF4 A84C                    FDB      sci_entry
 6030 FFF6              icf_vector
 6031 FFF6 A53D                    FDB      icf_entry
 6032 FFF8              irq_vector
 6033 FFF8 A3FA                    FDB      int_entry
 6034 FFFA              swi_vector
 6035 FFFA A84C                    FDB      sci_entry
 6036 FFFC              nmi_vector
 6037 FFFC A84C                    FDB      sci_entry
 6038 FFFE              res_vector
 6039 FFFE 849A                    FDB      reset
```

resetのラベルがついていますが、RESETが行われた時に実行されるアドレスは$849Aですので、そこから追ってみます。

```
  411 849A              reset:
  412 849A 01                      nop
  413 849B 01                      nop
  414 849C 01                      nop
  415 849D 8E013F                  lds      #$013F      ; Internal RAM 256 Byte
  416 84A0 01                      nop
  417 84A1 01                      nop
  418 84A2 01                      nop
  419 84A3 BD8573                  jsr      L8573
```

RESET直後にスタックポインタを設定しています。CPU内蔵の256byte RAMを使っていることがわかります。 jsrで実行されるL8573のルーチンを見ると、

```
  536 8573              L8573:
  537 8573 CE0040                  ldx      #$0040      ; fill zero $0040-$013f
  538 8576 4F                      clra
  539 8577              L8577:
  540 8577 A700                    staa     $00,x
  541 8579 08                      inx
  542 857A 8C013D                  cpx      #$013D
  543 857D 26F8                    bne      L8577
  544 857F CE4000                  ldx      #$4000      ; fill zero $4000-$47ff
  545 8582 4F                      clra
  546 8583              L8583:
  547 8583 A700                    staa     $00,x
  548 8585 08                      inx
  549 8586 8C47FF                  cpx      #$47FF
  550 8589 26F8                    bne      L8583
```

CPU内蔵のRAMをゼロクリアしていることがわかります。続いて$4000-$47FFの領域もゼロクリアしています。 このマイコンボードにはMB8422という16Kbit(2048x8bit)RAMが実装されていますので、このメモリは$4000から配置されていると予想できます。ゼロクリアされている2Kbyteのサイズも合致しています。

これでこのマイコンボードの仕様がおよそわかりました。 メモリマップは以下のようになっていると思われます。

```
$0000 -----------------------
       Internal Register
$0027 -----------------------
              :
$0040 -----------------------
       Internal RAM 256byte
$013F -----------------------
              :
$4000 -----------------------
       External RAM (MB8422)
$47FF -----------------------
              :
$8000 -----------------------
       External ROM (27C256)
$FFFF -----------------------

```

63B03は統合型のマイコンですので、GPIOやシリアルインターフェース、タイマーなどの機能を内蔵していて、Internal Registerを操作するだけで使えます。使い方はデータシートに書かれているので、そちらを読み込むことにしましょう。 次はこのマイコンボードにモニタを実装して、自由に動かせるマイコンボードにしてみます。（[続く](https://kanpapa.com/2018/01/63b03-dual-cpu-lilbug.html "63B03デュアルCPUマイコンボードで遊んでみた（３）モニタ実装編")）
