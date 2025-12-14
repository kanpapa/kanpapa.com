---
title: "COSMAC VIP OSをRAMエリアで起動させてみました"
date: 2020-04-27
slug: "cosmac-vip-os-ram1"
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
image: "images/cosmac_vip_os_ram1.jpg"
---

COSMAC MBC+STG1861+HEXKEYボードで、COSMAC VIP OSが動くようになりました。しかし、COSMAC MBCボードだと、なぜかCOSMAC VIP OSの起動に失敗することが多いのです。COSMAC MBCボードではプッシュスイッチで0000番地のユーザプログラムか、8000番地のユーティリティROM（モニタ）の起動を選択できますが、このあたりのタイミングがCOSMAC VIP OSと相性が良くないのではと思われます。

モニタ機能はMCSMP20（[The 1802 Membership Card](http://www.sunrise-ev.com/1802.htm "The 1802 Membership Card")のモニタプログラム）が高機能なので、こちらをメインに使いたいのですが、COSMAC VIP OSと同じ8000番地に配置されていますので、COSMAC VIP OSとの共存はできません。しかし、COSMAC VIP OSのレトロモニタもいつでも動かせるようにしておきたいところです。

そこでCOSMAC VIP OSを7000番地のRAMエリアにリロケートしてみることにしました。これがうまくいけばROMの空きエリアにもリロケートできるでしょう。想定しているメモリマップは以下のようになります。

![](images/cosmac_vip_os_ram_memorymap.jpg)

さらにMCSMP20のシリアル入力とHEXキーボード入力が衝突しないように、HEXキーボードをEF4接続に変更しました。これを想定してSTG1861+HEXKEY基板でもキーボードの信号をEF1～4から選択できるようにしておいたので、J2のジャンパをEF3からEF4に変更すれば、ハードウェアの対応は完了です。

![](images/cosmac_vip_hexsw_efn.jpg)

8000番地のROMエリアにあるCOSMAC VIP OSを7000番地のRAMエリアに移動するために、COSMAC VIP OSの解析をある程度行い、解析結果から以下の手順でパッチをあてました。

(1) COSMAC VIP OSのバイナリをMCSMP20モニタで7000-71FFにロードします。

(2) 以下の番地のデータをMCSMP20モニタで修正します。

- $7001 $80 → $70 (モニタの上位アドレスを設定）

- $7022 $36 → $30 ("C"キーをチェックせずにモニタにJUMP)

- $7056 $81 → $71 (モニタの上位アドレスを設定)

- $719F $3E → $3F (キーボード入力をEF3 から EF4に変更)

- $71AA $36 → $37 (キーボード入力をEF3 から EF4に変更）

MCSMP20のコマンドだと以下のようになります。

- W7001 70

- W7022 30

- W7056 71

- W719F 3F

- W71AA 37

(3) RAMの0000番地に、7000番地にJUMPする命令を書きます。MCSMP20のコマンドだと以下のようになります。

- W0000 C0 70 00

(4) RESETスイッチを押したあとにRUN Pスイッチを押すと、COSMAC VIP OSが起動します。

このような少し複雑な手順を踏むのは、MCSMP20モニタから直接起動するとレジスタがCPUリセット直後の状態でないので、COSMAC VIP OSが誤作動するためです。0000番地からCOSMAC VIP OSにジャンプすることでリセット直後の状態のままCOSMAC VIP OSを起動させます。

起動後はCOSMAC VIP OSが7000番地のRAMの上で動作します。

![cosmac_vip_os_ram1.jpg](images/cosmac_vip_os_ram1.jpg)

なお、MCSMP20のSave機能を使ってパッチを当てた直後のバイナリをIntelHEXフォーマットにしておくと次の起動時に便利です。
