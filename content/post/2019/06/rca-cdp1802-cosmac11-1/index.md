---
title: RCA CDP1802 COSMACを動かしてみた(11) モーターを制御してみた
date: 2019-06-22
slug: rca-cdp1802-cosmac11-1
categories:
- cosmac
- retrocomputing
tags:
- cosmac-toy
image: images/cosmac_motor_bread.jpg
---

COSMACでDCモーターを制御してみました。モータードライバは各社から出ていますが、ブレッドボードでも手軽に実験ができそうな秋月電子の[TB6612使用 Dual DCモータードライブキット\[AE-TB6612\]](http://akizukidenshi.com/catalog/g/gK-11219/ "TB6612使用 Dual DCモータードライブキット[AE-TB6612]")を使うことにしました。いつものようにブレッドボードで試作し、動作確認をしたところで基板化します。

COSMAC CPU基板に接続するモータードライバの回路図は以下のようになります。

![](images/cosmac_motor_sch.png)

これをブレッドボードで試作し、COSMAC CPUボードに接続しました。

![](images/cosmac_motor_bread.jpg)

次にCOSMACに書き込むプログラムを考えます。このモータードライバは１つのモーターあたり２ビットのデジタル信号を与えることで正転、逆転、停止を制御します。さらにPWMで速度調整もできるようですが、こちらはQ信号に接続しておいて後から制御方法を考えます。

COSMACのプログラムローダー基板にあるトグルスイッチの値を読み取り、その値をモータードライバに伝えることにします。これで４つのトグルスイッチで２つのモーターを自在に制御できるはずです。

プログラムは以下のようになります。今回はQはHIGH固定にしています。11バイトならトグルスイッチでのプログラム入力も簡単です。

```
0000- 1        *
0000- 2        * Motor driver program 1 for COSMAC
0000- 3        * SB-Assembler
0000- 4        *
0000- 5        * SW input -> motor (forward <->reverse)
0000- 6        *
0000- 7        * BUS0 --- AIN1
0000- 8        * BUS1 --- AIN2
0000- 9        * BUS2 --- BIN1
0000- 10        * BUS3 --- BIN2
0000- 11        * Q    --- PWMA/B
0000- 12        *
0000- 13                .CR     1802    ;To load the 1802 cross overlay
0000- 14                .OR     $0000
0000- 15        *
0000-F8 0A            16 (   2) START   LDI     #IOR    ;D <- #IOR
0002-A5               17 (   2)         PLO     5       ;R(5).0 <- D
0003-E5               18 (   2)         SEX     5       ;X <- 5
0004-7B               19 (   2)         SEQ
0005-6A               20 (   2) LOOP1   INP     2       ;M(R(5)) <- BUS; D <- BUS
0006-64               21 (   2)         OUT     4       ;BUS <- M(R(5)); R(5)++
0007-25               22 (   2)         DEC     5       ;R(5)--
0008-30 05            23 (   2)         BR      LOOP1   ;Branch to LOOP1
000A- 24        *
000A-00               25        IOR     .DB     0       ;IO Register
000B- 26
000B- 27                .EN

```

トグルスイッチをON-OFFしたところ、無事モーターが動くことを確認しました。正転、逆転も自由自在です。

YouTubeにもアップしておきました。

https://youtu.be/E1psAAdL30w?si=q\_SOc8v8gCRncG\_-

これで動作確認もできましたので、シールド基板を発注しました。

![](images/cosmac_motor_gerber.jpg)

Maker Faire Tokyo 2019では、これらのシールド基板を使って、何か作る予定ですのでお楽しみに。
