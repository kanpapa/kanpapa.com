---
title: "KURO-SHEEVA (玄柴) その後"
date: 2010-02-05
slug: "kuro-sheeva-4"
categories: 
  - "server"
---

KURO-SHEEVAのその後です。 とりあえず、apt-get update, apt-get upgradeを行って最新の環境にしました。 あとはNTPでの時刻の同期や一般ユーザなど作成しました。これから必要なソフトウェアをインストールしていくことになりますが、さて、何をしましょうか。 eSATAのインターフェースにHDDをつないでNASとして使うのは当たり前すぎて面白くありません。NASならhackkitが入ったLinkStationがすでにあるのでそちらを使います。 ここはUSBとSDカードとNetworkをだけ使って何かするとしたら考えてみると・・・

1. 昔、玄箱でやっていたようにSETI@homeに参加してみる。久々にboincを動かしますか。
2. USBの入力とかNetworkからの入力でSDカードにデータを溜め込むようなロガーを作る。
3. USBにPepperとかGainerを接続して、外部機器をコントロールする。
4. 玄柴をたくさん集めてHadoopクラスタを動かす・・・。

とりあえずいろんなデバイスを使うためにも、まずはカーネルを最新にしたほうが良さそうかも。
