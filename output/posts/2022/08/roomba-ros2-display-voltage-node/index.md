---
title: "ROS2 Foxyでルンバのバッテリー電圧を表示するノードを作ってみました。"
date: 2022-08-13
categories: 
  - "roomba"
tags: 
  - "roomba"
coverImage: "roomba_dispvolv_led.jpg"
---

[ルンバのLEDの制御](https://kanpapa.com/2022/08/roomba-ros2-led-song.html "ROS2 FoxyでルンバのLEDとサウンドを制御してみました")ができたので、ルンバのバッテリー電圧を表示するノードを作ってみました。

具体的には以下の処理を行います。

1. ルンバからはバッテリー電圧の情報(battery/voltage)が配信されていますので、これをSubscribeします。
2. 受け取ったバッテリー電圧の情報を使って、LEDを表示する指令(set\_ascii)をPublishします。
3. ルンバではLEDを表示する指令をSubscribeして、LEDを点灯させます。

これを繰り返せばバッテリ電圧がリアルタイムで表示されるはずです。

<!--more-->

### ROS2のノードを書いてみる

今回は[demura.net](https://demura.net/ "demura.net")さんの以下の記事を参考にしています。

- [ROS2演習5-2021:トピック通信しよう！(Python)](https://demura.net/robot/ros2/20748.html "ROS2演習5-2021:トピック通信しよう！(Python)") demura.net

こちらの記事ではPublisherとSubscriberをそれぞれ作成するものですが、PublisherとSubscriberを一つにすれば実現できるだろうとの目論見です。PublisherとSubscriberのソースコードを参考にさせていただき、丁寧なコメントもこのプログラムに合わせてそのままとしました。

完成したソースコードはGitHubに置きました。

- [https://github.com/kanpapa/roomba/tree/main/dispvolt](https://github.com/kanpapa/roomba/tree/main/dispvolt "dispvolt")

### ノードを動かしてみる

ルンバのROS2ドライバを動かしておき、今回作成したノード(dispvolt\_node)を動かしてみます。

![roomba_dispvolv_node_run.png](images/roomba_dispvolv_node_run.png)

画面に表示されているようにバッテリー電圧は正常に取得できているようです。

ルンバのLEDを確認すると、同じ数字が表示されています。ルンバを動かすと少しずつ数字が減っていくのがわかります。

![roomba_dispvolv_led.jpg](images/roomba_dispvolv_led.jpg)

rqt\_graphでも確認してみました。意図した構造になっています。

![roomba_dispvolv_rqtgraph1.png](images/roomba_dispvolv_rqtgraph1.png)

### まとめ

ルンバから配信される情報を受信して、それに応じた結果をルンバに返すという簡単なノードを作ることができました。

今回はシンプルなものですが、もう少し拡張してバッテリー電圧が低下してきたら、CHECK LEDを点灯させたり、play\_songでアラート音を出したりといったこともできそうです。
