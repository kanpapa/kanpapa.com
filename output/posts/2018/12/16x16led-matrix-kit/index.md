---
title: "クソマゾLEDマトリックス バッヂ を作ってみた"
date: 2018-12-22
categories: 
  - "electronics"
tags: 
  - "led-matrix"
coverImage: "16x16led_front.jpg"
---

@Ghz2000さんが[クソマゾLEDマトリックス バッヂ](http://ghz2000.com/wordpress/?p=1389 "クソマゾLEDマトリックス バッヂ") をTwitterで紹介されていたので、[Ogaki Mini Maker Faire 2018](https://www.iamas.ac.jp/ommf2018/ "Ogaki Mini Maker Faire 2018")でキットを買ってきました。

![16x16led_ommf2018.jpg](images/16x16led_ommf2018.jpg)

なかなか難易度が高そうですが、なぜかQFP版とQFN版の両方を買ってしまいました。

キットの中身はこんな感じです。

![16x16led_kit.jpg](images/16x16led_kit.jpg)

まずはQFP版の組み立て開始です。自宅でははんだ付け禁止なので[おおたfab](https://www.ota-fab.com/ "おおたfab")さんで作業させていただきました。

![16x16led_otafab.jpg](images/16x16led_otafab.jpg)

腰痛持ちなので長時間の作業はきつく、休憩をはさみながら少しづつ進めました。

![16x16led_makeing.jpg](images/16x16led_makeing.jpg)

ようやく表面のチップLED(0603)と抵抗の実装が完了しました。

![16x16led_front.jpg](images/16x16led_front.jpg)

裏面のATMega3209やFETなどはんだ付けして、ようやく実装が完了です。

![16x16led_back.jpg](images/16x16led_back.jpg)

AVRへの書き込みはGhz2000さんの[記事](http://ghz2000.com/wordpress/?p=1387 "AVR 0-Series UPDI書き込み ATMega3209/4809等")を参考にしましたが、RESET-DTRがジャンパーで切り離せるeJackinoと、書き込み端子に接触しやすくするためにL型のピンヘッダを使って書き込みました。

![16x16led_updi.jpg](images/16x16led_updi.jpg)

テストプログラムを書き込んだところ、やはり点灯しないLEDが存在します。

![](images/16x16led_debug.jpg)

これを１つずつ確認したところ、逆接続が２か所見つかりました。他ははんだ付けをしっかりやることで点灯するようになりました。少し浮いてしまって接触不良だったようです。

テストプログラムで全点灯することと、１ドットずつ制御ができるかの確認も完了です。

サンプルデモプログラムも無事動きました。

サンプルプログラムを見ながら次は何を表示させてみようか考え中です。

@Ghz2000さん、いつも楽しめるキットをありがとうございます。
