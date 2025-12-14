---
title: "COSMAC MBC 拡張ボードRev. 0.2を製作しました。"
date: 2019-10-27
slug: "cosmac-mbc-ext-board-rev02"
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
image: "images/cosmac_mbc_ext_rev02_prod.jpg"
---

COSMAC MBC 拡張ボードのRev. 0.2試作基板が到着しましたので組み立てました。

![cosmac_mbc_ext_rev02_prod.jpg](images/cosmac_mbc_ext_rev02_prod.jpg)

IDCコネクタの向きも修正しましたので、CPUボードとまっすぐ接続することができるようになりました。

<!--more-->

早速動作確認をおこなったところ、LEDが眩しすぎる問題がありました。今回は秋月電子の[100本入りLED](http://akizukidenshi.com/catalog/g/gI-00562/ "３ｍｍ赤色ＬＥＤ　ＯＳＤＲ３１３３Ａ　３０度　（１００個入）")を使用したのですが、前回使用した手持ちのLEDより輝度が高いようです。

Rev. 0.2基板では、LED点灯が不要な場合を考え、LEDへの電源を切れるようジャンパーピン(JP1)を作ってあったので、応急措置としてここに1KΩの抵抗を入れてLEDの輝度を落としました。本来であれば各LEDごとに抵抗を入れるべきなのでこれは次回の修正事項とします。

この状態で、LEDの表示確認と、LCDの接続確認、入力ポートの確認まで行いました。LEDの輝度以外は問題は無さそうです。

![cosmac_mbc_ext_rev02_check.jpg](images/cosmac_mbc_ext_rev02_check.jpg)

次はCPUボードの修正版 Rev. 0.2の製作に入りますが、現時点でひとまず動作していますので、Rev. 0.2はじっくり製作していきます。
