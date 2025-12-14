---
title: "Wio NODEでIoTセキュリティを考えさせられた"
date: 2018-01-02
categories: 
  - "retrocomputing"
tags: 
  - "wio-node"
coverImage: "wio_node.jpg"
---

年末年始に遊ぼうかと秋月電子でSeeed Studioの[Grove Wio NODE](http://akizukidenshi.com/catalog/g/gM-10631/ "Grove Wio NODE")を買ってきました。ESP8266が搭載されていてWi-Fiに接続でき、各種Groveモジュールを接続することができます。価格も1100円とお手頃です。

![wio_node.jpg](images/wio_node.jpg)

ちゃんとくさんの記事[「Wio Node」で半田付けなしの電子工作！温度計作りでIoTはじめの一歩](https://dotstud.io/blog/seeed-wionode-hands-on/ "「Wio Node」で半田付けなしの電子工作！温度計作りでIoTはじめの一歩")を参考にしながらセットアップして、Seeed StudioのWio NODEのAPIをたたくと温度センサーの値が取得できたり、７セグメントLEDに好きな数字を表示することができました。

![](images/wio_node_led.jpg)

７セグメントLEDに数値を表示するAPIはこんな感じで簡単に使えます。

> $ curl -k -X POST https://us.wio.seeed.io/v1/node/Grove4DigitUART0/display\_digits/表示開始桁位置/表示したい数字4桁?access\_token=登録したWio NODEにアクセスするための文字列

例えば、このAPIを私のVPSで動かして、VPSのロードアベレージの数値を自宅の７セグメントLEDに表示するということもできてしまいます。

このとき、APIの仕様を見ながら、いろいろ試してみたのですが、うっかりAPIのドメインを間違えてしまいました。タイムアウトでエラーとなったのですが、タイムアウトで返ってきたということは、ドメインが存在して接続までできたということになります。

間違えたドメインは以下の通りです。

- 正しいドメイン　us.wio.seeed.io

- 間違ってアクセスしたドメイン　us.wio.seed.io

このように非常にドメインが似ており、このus.wio.seed.ioは実際に存在しました。もし、私のようにうっかりタイプミスをしてしまった場合、このサイトのWWWサーバのログに呼び出したAPIのURLやWio NODEに割り当てられたアクセストークンが記録されてしまいます。APIのURLからどんなGroveデバイスが接続されているのかもわかるでしょう。

このため、今登録したアクセストークンは漏洩した可能性があると判断し、一度Wioデバイスの登録を削除したあとに、再度登録して新しいアクセストークンを作成しました。

このサイトはそのような目的は無いのかもしれませんが、悪意があれば、IoTデバイスのアクセストークンを入手し、意図しないWio NODEの制御が行われてしまう可能性があります。アクセストークンによる認証だけでは危険だなと再認識しました。
