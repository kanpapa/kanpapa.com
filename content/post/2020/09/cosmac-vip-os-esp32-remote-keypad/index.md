---
title: COSMAC VIP OSをスマートフォンで操作してみました
date: 2020-09-06
slug: cosmac-vip-os-esp32-remote-keypad
categories:
- cosmac
- retrocomputing
tags:
- cosmac-mbc
- esp32
image: images/esp32_relay_controller_3d.jpg
---

[Maker Faire Tokyo 2020](https://makezine.jp/event/makers-mft2020/m0029/ "Maker Faire Tokyo 2020 - COSMAC研究会")の出展に向けて、COVID-19対策を行わなければなりません。出展者マニュアルには感染防止対策として以下の項目があげられています。

- 会場内では必ずマスクを着⽤する
- 来場者が直接出展作品・製品などに触れるような展⽰は原則として⾏わない
- サイン、POP などを準備し、できるだけ出展者との会話時間を短くするように⼯夫する
- 来場者とは最低でも1メートル以上の距離を保ち、⼤きな声での会話を控える

COSMAC研究会の展示物はタクトスイッチやトグルスイッチなどどうしても触れるものになってしまいます。そこでタクトスイッチをスマートフォンで操作できるようにしました。ある程度の準備は[こちら](https://kanpapa.com/cosmac/blog/2020/08/mftokyo2020-covid-19-cosmac-vip-keyboard.html "Maker Faire Tokyo 2020の出展にむけてCOVID-19対策準備中です。")ですすめていましたが、パーツがそろったのでいよいよCOSMACに接続してみます。

ESP32でWiFi-APとローカルWebサーバを動かして、ESP32のGPIOで16チャンネルのリレーモジュールを動かし、スマートフォンの画面をタクトスイッチの代わりにします。これで展示物に触れることなく、COSMAC VIP OSでメモリの読み書きを行うことができます。

COSMAC MBCのタクトスイッチの配線の引き出しですが、ちょうどユニバーサルエリアを作ってあったのでここにピンヘッダを取り付けて引き出しました。

![cosmac_tact_sw2.jpg](images/cosmac_tact_sw2.jpg)

<!--more-->

製作したシステムは以下のようになりました。

![cosmac_vip_remote_keypad1.jpg](images/cosmac_vip_remote_keypad1.jpg)

テスト中の様子をYouTubeにアップしておきました。

現時点ではESP32とリレーモジュールを接続する回路はブレッドボードで組んでいますが、回路図をまとめていたらいつの間にかガーバーデータまで作ってしまいました。

![esp32_relay_controller_3d.jpg](images/esp32_relay_controller_3d.jpg)

間に合えばMaker Faire Tokyo 2020ではプリント基板化できているかもしれません。
