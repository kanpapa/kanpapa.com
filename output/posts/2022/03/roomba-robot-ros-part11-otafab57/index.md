---
title: "ルンバで自律走行を行ってみました （おおたfab 第57回 素人でもロボットをつくりたい）"
date: 2022-03-21
categories: 
  - "roomba"
tags: 
  - "roomba"
  - "otafab"
  - "otafab-robot"
coverImage: "roomba_otafab57_baseplate.jpg"
---

[おおたfab](https://ot-fb.com/ "おおたfab")さんでは、「[素人でもロボットをつくりたい](https://ot-fb.com/iot/6353/ "素人でもロボットをつくりたい")」という勉強会を定期的に行っています。前回は[LiDARを使って地図の作成](https://kanpapa.com/2022/03/Roomba-robot-ros-part8-otafab56.html "ルンバで地図をつくってみました　その３ （おおたfab 第56回 素人でもロボットをつくりたい）")を行いましたが、今回はNavigation（自律走行）にチャレンジします。

![roomba_otafab57_baseplate.jpg](images/roomba_otafab57_baseplate.jpg)

写真に写っていますが、現在LiDARやRaspberry Piやバッテリーを固定するためのベースプレートもおおたfabさんの[レーザーカッター](https://ot-fb.com/fablab "おおたFabのファブラボ")で製作中です。

<!--more-->

### 今回参考にした記事

- [hector\_slamと2D Navigationを組み合わせてRoombaを自律移動させる](https://daikimaekawa.github.io/ros/2014/04/20/Navigation2d "hector_slamと2D Navigationを組み合わせてRoombaを自律移動させる ") ([ゼロから始めるロボットプログラミング入門講座](https://daikimaekawa.github.io/) Daiki Maekawaさん）

### 前回から変更した点

- gmapping-slamからhector-slamに変更しました。 参考記事からgmapping-slamはルンバに不向きとのことなので、hector\_slamを試したところ、なかなか良い感じです。
- ルンバに接続するRaspberry Pi 3B＋(1GB RAM)をRaspberry Pi 4(4GB RAM)に変更しました。 前回やや動きが悪くなる時があったのでCPUとメモリに余裕があるようにしました。

### 実機で動かし方

手順はGithubを参照してください。あちこちのスクリプトを調整しています。

- [Roombaの実機環境でのhector-SLAMとNavigation](https://github.com/docofab/RoombaControlls/blob/main/ROS/instructions/slam-hector-real-roomba-ca_bringup.md "Roombaの実機環境でのhector-SLAMとNavigation")

### ナビゲーションの様子

[おおたfab](https://ot-fb.com/ "おおたfab")さんのオフィスで実験をしました。狭い通路を行先に指定してそこまで自律移動をしてみます。

RvizでのNavigationの様子です。

ルンバ実機の動画です。途中で少し止まりますが、何かを考えているようです。

rqt\_graphの結果

![rosgraph03191711.png](images/rosgraph03191711.png)

このようにRvizで指定した場所に移動することができました。

これを応用してウェイポイントナビゲーションを試してみようと思います。
