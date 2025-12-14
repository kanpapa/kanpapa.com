---
title: "COSMAC VIP互換のHEX Keyboardをユニバーサル基板に実装してみました"
date: 2020-04-05
slug: "cosmac-mbc-vip-proto2"
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
image: "images/cosmac_vip_hexkey3.jpg"
---

[ブレッドボードでDIPスイッチを使ったCOSMAC VIPの16進キーボードを製作](https://kanpapa.com/cosmac/blog/2020/04/cosmac-mbc-vip-proto1.html "COSMAC VIPをCOSMAC MBCで動かしてみました")しましたが、やはりプッシュスイッチでないと使い勝手がよくありません。そこで、先日作成した[TVディスプレイボード](https://kanpapa.com/cosmac/blog/2020/01/cosmac-mbc-tv-rev02-finished.html "TVディスプレイボード")のユニバーサル領域に実装してみることにしました。

はんだ付けが完了したCOSMAC VIPの16進キーボードはこのようになりました。

![cosmac_vip_hexkey1.jpg](images/cosmac_vip_hexkey1.jpg)

<!--more-->

裏面はこのような感じです。

![cosmac_vip_hexkey2.jpg](images/cosmac_vip_hexkey2.jpg)

実際にCOSMAC MBCに接続して動作確認を行いました。DIPスイッチにくらべて格段に操作性はよくなりました。

![cosmac_vip_hexkey3.jpg](images/cosmac_vip_hexkey3.jpg)

動くには動くのですが、COSMAC VIPのOSが起動しないことや、使っているといつの間にか動かなくなるなど、やや不安定な状態です。

うまく動いている場合は、VRAMへの書き込みもできるので、回路には問題ないようですが、実装上の問題がありそうなので原因を調べてみます。

![cosmac_vip_hexkey4.jpg](images/cosmac_vip_hexkey4.jpg)
