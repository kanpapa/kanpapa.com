---
title: RCA CDP1802 COSMACを動かしてみた(9) LCDに文字を表示してみる
date: 2019-05-31
slug: rca-cdp1802-cosmac9-lcd
categories:
- cosmac
- retrocomputing
tags:
- cosmac-toy
image: images/cosmac_lcd_proto.jpg
---

[前回の記事](https://kanpapa.com/cosmac/blog/2019/02/rca-cdp1802-cosmac8.html "RCA CDP1802 COSMACを動かしてみた(8) 電子オルガンを作ってみる")ではCOSMACで音をだしてみましたが、次はCOSMACで文字を表示してみます。

今回製作したCPU基板には4bitのバスがでていますので、これをHD44780インターフェース準拠のLCDに接続してみました。

回路図は以下のようになります。ついでにユーザスイッチとリセットスイッチもつけました。

![](images/cosmac_lcd_sch.png)

オリジナルのCPU回路ではTPB信号がコネクタに出力されていないので、空きピンを使ってジャンパー線で接続することにします。

まずはブレッドボードでプロトタイプを製作しました。この写真ではすでに表示プログラムが動いています。

![](images/cosmac_lcd_proto.jpg)
<!--more-->

LCDの表示プログラムは次のようになりました。

```
0000- 1        *
0000- 2        * SC1602 LCD Display program 1 for COSMAC
0000- 3        * SB-Assembler
0000- 4        *
0000- 5                .CR     1802    ;To load the 1802 cross overlay
0000- 6                .OR     $0000
0000- 7        *
0000- 8        * CDP1802        SC1602LCD
0000- 9        * TPB---AND----> E(6)
0000- 10        * N2-----+
0000- 11        * Q -----------> RS(4)
0000- 12        * BUS0 --------> DB4(11)
0000- 13        * BUS1 --------> DB5(12)
0000- 14        * BUS2 --------> DB6(13)
0000- 15        * BUS3 --------> DB7(14)
0000- 16        *         GND--> R/W(5)
0000- 17        *         GND--> GND(2)
0000- 18        *         +5V--> VDD(1)
0000- 19        *
0000-30 16            20 (   2) START   BR      MAIN
0002- 21        *
0002- 22        *---------------------------
0002- 23        * LCD Initialize Data(4bit mode, RS=0)
0002- 24        *---------------------------
0002-03               25        INTDAT  .DB     $03             ;Function set (Interface is 8bits long.)
0003- 26        *                               ;wait 4.1ms
0003-03               27                .DB     $03             ;Function set (Interface is 8bits long.)
0004- 28        *                               ;wait 100us
0004-03               29                .DB     $03             ;Function set (Interface is 8bits long.)
0005- 30        *                               ;wait 40us
0005-02               31                .DB     $02             ;Function set (Set interface to be 4 bits long.)
0006- 32        *                               ;wait 40us
0006-02               33                .DB     $02             ;Function set (2Line mode)
0007-08               34                .DB     $08             ;
0008- 35        *                               ;wait 40us
0008-00               36                .DB     $00             ;Display OFF, Cursor OFF, Blink OFF
0009-08               37                .DB     $08             ;
000A- 38        *                               ;wait 40us
000A-00               39                .DB     $00             ;Clear Display
000B-01               40                .DB     $01             ;
000C- 41        *                               ;wait 1.64ms
000C-00               42                .DB     $00             ;Entry Mode Set(Cursor right, shift off)
000D-06               43                .DB     $06             ;
000E- 44        *                               ;wait 40us
000E-00               45                .DB     $00             ;Display ON, Cursor OFF, Blink OFF
000F-0C               46                .DB     $0C             ;
0010- 47        *                               ;wait 40us
0010- 48        *---------------------------
0010- 49        * LCD Display data(4bit mode, RS=1)
0010- 50        *---------------------------
0010-03               51                .DB     $03             ;"1"
0011-01               52                .DB     $01             ;
0012- 53        *                               ;wait 40us
0012-03               54                .DB     $03             ;"2"
0013-02               55                .DB     $02             ;
0014- 56        *                               ;wait 40us
0014-03               57                .DB     $03             ;"3"
0015-03               58                .DB     $03             ;
0016- 59        *                               ;wait 40us
0016- 60        *----------------------
0016- 61        * Main routine
0016- 62        *----------------------
0016-7A               63 (   2) MAIN    REQ                     ;RS=0
0017-F8 02            64 (   2)         LDI     #INTDAT         ;INTDAT -> D
0019-A3               65 (   2)         PLO     3               ;D -> R(3).0
001A-E3               66 (   2)         SEX     3               ;3 -> X
001B- 67        *
001B- 68        * LCD Initrize
001B- 69        *
001B- 70        * Function set (Interface is 8bits long.)
001B- 71        *
001B-64               72 (   2)         OUT     4               ;M(R(X))->BUS, R(X)++
001C- 73        *
001C- 74        * Wait 4.1ms
001C- 75        *
001C-F8 40            76 (   2)         LDI     #64             ;Load immediate value 170 into 0
001E-A5               77 (   2)         PLO     5               ;Put D in R5,0
001F-25               78 (   2) LOOP1   DEC     5               ;Decrement R5 by 1 over 8 bits
0020-85               79 (   2)         GLO     5               ;Get R5.0 to test
0021-3A 1F            80 (   2)         BNZ     LOOP1           ;If R5.0 != 0, branch to LOOP
0023- 81        *
0023- 82        * Function set (Interface is 8bits long.)
0023- 83        *
0023-64               84 (   2)         OUT     4               ;M(R(X))->BUS, R(X)++
0024- 85        *
0024- 86        * Wait 100us
0024- 87        *
0024-F8 02            88 (   2)         LDI     #2              ;Load immediate value 2 into 0
0026-A5               89 (   2)         PLO     5               ;Put D in R5,0
0027-25               90 (   2) LOOP2   DEC     5               ;Decrement R5 by 1 over 8 bits
0028-85               91 (   2)         GLO     5               ;Get R5.0 to test
0029-3A 27            92 (   2)         BNZ     LOOP2           ;If R5.0 != 0, branch to LOOP
002B- 93        *
002B- 94        *
002B- 95        *
002B-F8 08            96 (   2)         LDI     #8              ;Loop 8 count
002D-A5               97 (   2)         PLO     5               ;D -> R(5).0
002E-64               98 (   2) LOOP3   OUT     4               ;M(R(3))->BUS, R(3)++
002F-25               99 (   2)         DEC     5               ;R(5).0--
0030-85              100 (   2)         GLO     5               ;R(5).0 -> D
0031-3A 2E           101 (   2)         BNZ     LOOP3
0033- 102        *
0033- 103        * Wait 1.64ms
0033- 104        *
0033-F8 20           105 (   2)         LDI     #32             ;Load immediate value 32 into 0
0035-A5              106 (   2)         PLO     5               ;Put D in R5,0
0036-25              107 (   2) LOOP4   DEC     5               ;Decrement R5 by 1 over 8 bits
0037-85              108 (   2)         GLO     5               ;Get R5.0 to test
0038-3A 36           109 (   2)         BNZ     LOOP4           ;If R5.0 != 0, branch to LOOP
003A- 110        *
003A- 111        * Send Enrty Mode Set/Set Address
003A- 112        *
003A-F8 04           113 (   2)         LDI     #4              ;Loop 4 count
003C-A5              114 (   2)         PLO     5               ;D -> R(5).0
003D-64              115 (   2) LOOP5   OUT     4               ;M(R(3))->BUS, R(3)++
003E-25              116 (   2)         DEC     5               ;R(5).0--
003F-85              117 (   2)         GLO     5               ;R(5).0 -> D
0040-3A 3D           118 (   2)         BNZ     LOOP5
0042- 119        *
0042- 120        * SET Register Select
0042- 121        *
0042-7B              122 (   2)         SEQ                     ;RS=1
0043- 123        *
0043- 124        * Write data to RAM
0043- 125        *
0043-F8 06           126 (   2)         LDI     #6              ;Loop 6 count
0045-A5              127 (   2)         PLO     5               ;D -> R(5).0
0046-64              128 (   2) LOOP6   OUT     4               ;M(R(3)) -> BUS; R(3)++
0047-25              129 (   2)         DEC     5               ;R(5).0--
0048-85              130 (   2)         GLO     5               ;R(5).0 -> D
0049-3A 46           131 (   2)         BNZ     LOOP6
004B- 132        *
004B- 133        * RESET Register Select
004B- 134        *
004B-7A              135 (   2)         REQ                     ;RS=0
004C- 136        *
004C-30 4C           137 (   2) STOP    BR      STOP            ;HALT
004E- 138        *
004E- 139                .EN

```

プログラムは0000から004Dですので、77バイトしかないのですが、これをトグルスイッチで入力するのは結構疲れます。プログラムが間違っているのか、入力ミスなのかという問題切り分けにも一苦労です。

そこで、このプログラムには同じような処理がいくつもあるので、それをサブルーチンにすれば少しはコードが短くなるかなと試してみました。SEP命令でプログラムカウンタとなるレジスタをR7またはR8に切り替えることでそれぞれのサブルーチンにジャンプします。サブルーチンから戻る場合はジャンプ前に使っていたR3レジスタをプログラムカウンタに設定することで元にもどります。サブルーチンのエントリアドレスの直前にSEP 3を置いている理由は、R7やR8レジスタをサブルーチンのエントリアドレスに再設定するためのテクニックです。

サブルーチンを使ったプログラムは次のようになりました。

```
0000- 1        *
0000- 2        * SC1602 LCD Display program 1 for COSMAC
0000- 3        * SB-Assembler
0000- 4        *
0000- 5                .CR     1802    ;To load the 1802 cross overlay
0000- 6                .OR     $0000
0000- 7        *
0000- 8        * CDP1802        SC1602LCD
0000- 9        * TPB---AND----> E(6)
0000- 10        * N2-----+
0000- 11        * Q -----------> RS(4)
0000- 12        * BUS0 --------> DB4(11)
0000- 13        * BUS1 --------> DB5(12)
0000- 14        * BUS2 --------> DB6(13)
0000- 15        * BUS3 --------> DB7(14)
0000- 16        *         GND--> R/W(5)
0000- 17        *         GND--> GND(2)
0000- 18        *         +5V--> VDD(1)
0000- 19        *
0000-F8 1E            20 (   2) START   LDI     #MAIN
0002-A3               21 (   2)         PLO     3
0003-F8 3C            22 (   2)         LDI     #WAIT1
0005-A7               23 (   2)         PLO     7
0006-F8 44            24 (   2)         LDI     #SEND1
0008-A8               25 (   2)         PLO     8
0009- 26        *       LDI     #0
0009- 27        *       PHI     3
0009- 28        *       PHI     7
0009- 29        *       PHI     8
0009- 30        *
0009-D3               31 (   2)         SEP     3       ; Jump MAIN
000A- 32        *
000A- 33        *---------------------------
000A- 34        * LCD Initialize Data(4bit mode, RS=0)
000A- 35        *---------------------------
000A-03               36        INTDAT  .DB     $03             ;Function set (Interface is 8bits long.)
000B- 37        *                               ;wait 4.1ms
000B-03               38                .DB     $03             ;Function set (Interface is 8bits long.)
000C- 39        *                               ;wait 100us
000C-03               40                .DB     $03             ;Function set (Interface is 8bits long.)
000D- 41        *                               ;wait 40us
000D-02               42                .DB     $02             ;Function set (Set interface to be 4 bits long.)
000E- 43        *                               ;wait 40us
000E-02               44                .DB     $02             ;Function set (2Line mode)
000F-08               45                .DB     $08             ;
0010- 46        *                               ;wait 40us
0010-00               47                .DB     $00             ;Display OFF, Cursor OFF, Blink OFF
0011-08               48                .DB     $08             ;
0012- 49        *                               ;wait 40us
0012-00               50                .DB     $00             ;Clear Display
0013-01               51                .DB     $01             ;
0014- 52        *                               ;wait 1.64ms
0014-00               53                .DB     $00             ;Entry Mode Set(Cursor right, shift off)
0015-06               54                .DB     $06             ;
0016- 55        *                               ;wait 40us
0016-00               56                .DB     $00             ;Display ON, Cursor OFF, Blink OFF
0017-0C               57                .DB     $0C             ;
0018- 58        *                               ;wait 40us
0018- 59        *---------------------------
0018- 60        * LCD Display data(4bit mode, RS=1)
0018- 61        *---------------------------
0018-03               62                .DB     $03             ;"1"
0019-01               63                .DB     $01             ;
001A- 64        *                               ;wait 40us
001A-03               65                .DB     $03             ;"2"
001B-02               66                .DB     $02             ;
001C- 67        *                               ;wait 40us
001C-03               68                .DB     $03             ;"3"
001D-03               69                .DB     $03             ;
001E- 70        *                               ;wait 40us
001E- 71        *----------------------
001E- 72        * Main routine
001E- 73        *----------------------
001E-7A               74 (   2) MAIN    REQ                     ;RS=0
001F-F8 0A            75 (   2)         LDI     #INTDAT         ;INTDAT -> D
0021-A4               76 (   2)         PLO     4               ;D -> R(4).0
0022-E4               77 (   2)         SEX     4               ;4 -> X
0023- 78        *
0023- 79        * LCD Initrize
0023- 80        *
0023- 81        * Function set (Interface is 8bits long.)
0023- 82        *
0023-64               83 (   2)         OUT     4               ;M(R(X))->BUS, R(X)++
0024- 84        *
0024- 85        * Wait 4.1ms
0024- 86        *
0024-F8 40            87 (   2)         LDI     #64             ;Load immediate value 170 into 0
0026-D7               88 (   2)         SEP     7               ;Call WaitSub
0027- 89        *
0027- 90        * Function set (Interface is 8bits long.)
0027- 91        *
0027-64               92 (   2)         OUT     4               ;M(R(X))->BUS, R(X)++
0028- 93        *
0028- 94        * Wait 100us
0028- 95        *
0028-F8 02            96 (   2)         LDI     #2              ;Load immediate value 2 into 0
002A-D7               97 (   2)         SEP     7               ;Call WaitSub
002B- 98        *
002B- 99        * Send Initrize command (8byte)
002B- 100        *
002B-F8 08           101 (   2)         LDI     #8              ;Send 8 byte
002D-D8              102 (   2)         SEP     8               ;Call SEND
002E- 103        *
002E- 104        * Wait 1.64ms
002E- 105        *
002E-F8 20           106 (   2)         LDI     #32             ;Load immediate value 32 into 0
0030-D7              107 (   2)         SEP     7
0031- 108        *
0031- 109        * Send Enrty Mode Set/Set Address
0031- 110        *
0031-F8 04           111 (   2)         LDI     #4              ;Send 4 byte
0033-D8              112 (   2)         SEP     8               ;Call SEND
0034- 113        *
0034- 114        * SET Register Select
0034- 115        *
0034-7B              116 (   2)         SEQ                     ;RS=1
0035- 117        *
0035- 118        * Write data to RAM
0035- 119        *
0035-F8 06           120 (   2)         LDI     #6              ;Send 6 byte
0037-D8              121 (   2)         SEP     8               ;Call SEND
0038- 122        *
0038- 123        * RESET Register Select
0038- 124        *
0038-7A              125 (   2)         REQ                     ;RS=0
0039- 126        *
0039-30 39           127 (   2) STOP    BR      STOP            ;HALT
003B- 128        *
003B- 129        * WAIT SUB ROUTINE
003B- 130        *
003B-D3              131 (   2) EXIT1   SEP     3
003C-A5              132 (   2) WAIT1   PLO     5               ;Put D in R5,0
003D-25              133 (   2) LOOP2   DEC     5               ;Decrement R5 by 1 over 8 bits
003E-85              134 (   2)         GLO     5               ;Get R5.0 to test
003F-3A 3D           135 (   2)         BNZ     LOOP2           ;If R5.0 != 0, branch to LOOP
0041-30 3B           136 (   2)         BR      EXIT1
0043- 137        *
0043- 138        * SEND n byte SUB ROUTINE
0043- 139        *
0043-D3              140 (   2) EXIT2   SEP     3
0044-A5              141 (   2) SEND1   PLO     5               ;D -> R(5).0
0045-64              142 (   2) LOOP6   OUT     4               ;M(R(X)) -> BUS; R(X)++
0046-25              143 (   2)         DEC     5               ;R(5).0--
0047-85              144 (   2)         GLO     5               ;R(5).0 -> D
0048-3A 45           145 (   2)         BNZ     LOOP6
004A-30 43           146 (   2)         BR      EXIT2
004C- 147
004C- 148                .EN

```

プログラムの大きさは0000から004Bとなったので2バイトは短くできましたが、結局サブルーチン側である程度のコードが必要なためこの大きさでは効果がでませんでした。現在のCPUには実装されているスタックは便利だなと実感できました。

今回の実験でCDP1802 COSMACにLCDを接続することができました。せっかくですので、これまで製作したミニ電子オルガンとLCDの専用基板を作って、Arduinoのように積み重ねて利用できるようにしてみます。
