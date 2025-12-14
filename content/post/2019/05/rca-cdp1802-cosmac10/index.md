---
title: RCA CDP1802 COSMACを動かしてみた(10) シールド基板を作ってみた
date: 2019-05-31
slug: rca-cdp1802-cosmac10
categories:
- cosmac
- retrocomputing
tags:
- cosmac-toy
image: images/cosmac_shield_organ_lcd.jpg
---

これまで製作してきた実験回路をコンパクトなシールド基板にしてみました。ArduinoのようにCPU基板に重ねる形です。プログラムローダー基板も同様に重ねる形にしました。こうすることでより操作しやすくなりますし、カッコいいです。

CPU基板はコネクタ位置の微調整とQ信号とTPB信号を直接出力できるように変更したものを製作しました。

![](images/cosmac_cpu_new.jpg)
<!--more-->

また、シールド基板と干渉しないようにバッテリとメモリスタンバイスイッチを裏面に実装しています。コネクタもメス型のヘッダピンにしました。

![](images/cosmac_cpu_front.jpg)
![](images/cosmac_cpu_back.jpg)

シールド基板は秋月電子のC基板のサイズでガーバーデータを作成しました。もちろんV-CUTで2つの基板を一度に作ります。

![](images/cosmac_sheld_gerber.jpg)

完成した基板はこんな感じになりました。基板の色は白を使ってみました。白もなかなかかっこいいです。

![](images/cosmac_sheld_pcb1.jpg)

部品を実装した基板を並べてみました。最初のプロトタイプからだんだん形になってきたと思います。

![](images/cosmac_pcb_all.jpg)

完成したシールド基板です。

![](images/cosmac_shield_organ_lcd.jpg)

ハードウェアは形になりましたので、これらのシールドを使って、もう少しアプリケーションを作ってみようと思います。
