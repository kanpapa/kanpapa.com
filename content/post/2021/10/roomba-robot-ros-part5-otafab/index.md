---
title: "オドメトリ情報を使ってルンバ実機を動かしてみました （おおたfab 第48回 素人でもロボットをつくりたい）"
date: 2021-10-10
slug: "roomba-robot-ros-part5-otafab"
categories: 
  - "robot"
  - "roomba"
tags: 
  - "roomba"
  - "otafab"
  - "otafab-robot"
image: "images/Roomba-robot-ros-part5-turtlesim.jpg"
---

[おおたfab](https://ot-fb.com/ "おおたfab")さんでは、「[素人でもロボットをつくりたい](https://ot-fb.com/iot/6353/ "素人でもロボットをつくりたい")」という勉強会を定期的に行っています。前回は[ルンバ実機とGazeboシミュレーターのオドメトリ情報を比較してみました](https://kanpapa.com/2021/09/Roomba-robot-ros-part4-otafab.html "ルンバ実機とGazeboシミュレーターのオドメトリ情報を比較してみました （おおたfab 第47回 素人でもロボットをつくりたい）")が、今回はオドメトリ(Odometry)情報を使用して正確な正方形の動きにチャレンジしてみます。

### まずはトラブルシューティングから

少し前から新たなメンバーが加わり、[Raspberry Pi 4にROSとGazeboシミュレーターのインストール](https://github.com/docofab/RoombaControlls/blob/main/ROS/instructions/setup-gazebo-rasppi.md "Roombaのシミュレーション環境のセットアップ(Raspberry Pi 4)")にチャレンジしています。メンバーで作成した手順に基づき作業を進めていましたが、どうしても亀が出てこないそうです。確認したところ肝心のROSがインストールできていませんでした。再度確認しながら途中のエラーを解決していき、ようやく亀が動くようになりました。その瞬間みんなで拍手です。

![Roomba-robot-ros-part5-turtlesim.jpg](images/Roomba-robot-ros-part5-turtlesim.jpg) <!--more-->

### オドメトリ情報を使って正方形に動かすには

オドメトリ情報を使ってROSで正方形で動かす記事を検索したところ以下のサイトがみつかりました。

- [毎日がロボット勉強会](http://dailyrobottechnology.blogspot.com/2014/12/793-navsquarepy.html "毎日がロボット勉強会")　四角形に沿って移動する nav\_square.py を見てみる

nav\_square.pyのソース解説を行っていますが、どうもソース全体は掲載されていないようです。GitHubで検索したところ、オリジナルと思われるものがみつかりました。こちらpi\_robotのプロジェクトの成果物のようです。

- [nav\_square.py](https://github.com/pirobot/ros-by-example/blob/master/rbx_vol_1/rbx1_nav/nodes/nav_square.py "nav_square.py")

このソースを眺めているとロジックが見えてきました。今使用しているプログラムと大きく構造がちがうので、アルゴリズムを流用させていただき、これまでのプログラムに組み込みました。

- [move4k3.py](https://github.com/docofab/RoombaControlls/blob/kanpapa/ROS/move_tutorial/move4k3.py "move4k3.py")

これをGazeboシミュレータで確認するとかなり正確な正方形を描いてくれました。

### ルンバ実機で正方形に動かす

ルンバ実機で同じプログラムを動かしましたが、なぜか回転が180度になってしまい、往復運動の動きになってしまいました。

![Roomba-robot-ros-part5-roomba.jpg](images/Roomba-robot-ros-part5-roomba.jpg)

そのためプログラム中のパラメタで90度の回転角度を半分の45度にして調整しました。これである程度正確に動くようになりました。

なぜ倍の動きをするのかはいまのところ不明です。このため、流れているROSトピックをrosbagで記録をしておき、後で解析してみることにしました。

### LIDIRのデモ

そろそろ次のことに取り組みたく、以前から気になっていたRPLIDAR A1M8を購入して動かしてみました。これを使うと周囲の物体までの距離や方向の情報が取得できます。

以下の記事を参考にして実験しました。

- [HARD2021：とってもリーズナブルなLIDAR。RPLIDAR A1M8を使おう！（第２回補講）](https://demura.net/robot/hard/20444.html "HARD2021：とってもリーズナブルなLIDAR。RPLIDAR A1M8を使おう！（第２回補講）") (demura.net)

この画面キャプチャは自宅で撮ったものですが、物の位置や動きがみえます。これをルンバに搭載して自律走行をしてみたいと考えています。

### ルンバ実装フレームの検討

LIDIRの記事をみていたところ、ルンバに実装するためのフレームの記事を見つけました。これを使えば便利そうです。

- [Roomblock(5)： 3Dプリンタで出力可能なフレーム構造](https://opensource-robotics.tokyo.jp/?p=2189 "Roomblock(5)： 3Dプリンタで出力可能なフレーム構造")　(Tokyo Opensource Robotics Kyokai）

こちらはおおたfabさんの3Dプリンタで試作をしてみることになりました。こちらも楽しみです。

### まとめ

課題は残るものの基本的な動きはPythonで書けるようになってきました。デバック情報で課題の原因をさぐりながら、LIDARとの組み合わせや3Dプリンタでのフレーム製作など新たな方面にも取り組んでいきます。
