---
title: "ROS2 FoxyでルンバのLEDとサウンドを制御してみました"
date: 2022-08-12
slug: "roomba-ros2-led-song"
categories: 
  - "roomba"
tags: 
  - "roomba"
image: "images/roomba_all_led_on.jpg"
---

ルンバには各種状態表示を行うためのLEDと音を出す機能があります。[ルンバのROS2用のドライバ](https://github.com/AutonomyLab/create_robot/tree/foxy " AutonomyLab / create_robot")ではこの機能をサポートしているので、実際に試してみました。

![roomba_sub_test1.jpg](images/roomba_sub_test1.jpg)
<!--more-->

### ルンバのSubscribers

ルンバで扱えるtopicはcreate\_robotの[README.md](https://github.com/AutonomyLab/create_robot/blob/foxy/README.md "README.md")にまとまっています。これを試していきます。

まずはルンバにつながっているRaspberry PiでROS2ドライバを動かします。

```
$ ros2 launch create_bringup create_2.launch
```

この状態で、[ros2 topic pub](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html#ros2-topic-pub "ros2 topic pub") コマンドを使ってtopicを発行してみます。

### ルンバのLEDを点灯させる

以下のコマンドでCHECK LED（少し大きめの赤い！マーク）を点灯できます。

```
$ ros2 topic pub --once /check_led std_msgs/Bool "data: true"
```

消灯の場合は false を指定します。

```
$ ros2 topic pub --once /check_led std_msgs/Bool "data: false"
```

制御できるLEDをすべて点灯すると写真のような状態になります。

![roomba_all_led_on.jpg](images/roomba_all_led_on.jpg)

### ルンバで音をだしてみる

ルンバでは4種類の曲をあらかじめ登録できます。1曲は最大16個の音階と音長で構成されます。

まずdefile\_songというtopicを発行して、1曲分のデータを登録します。

```
$ ros2 topic pub --once /define_song create_msgs/DefineSong "{song: 0,length: 16,notes: [78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63],durations: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]}"
```

曲の登録を行ったあとにplay\_songというtopicを発行して、曲番号を指定します。

```
$ ros2 topic pub --once  /play_song create_msgs/PlaySong "song: 0"
```

登録した曲が流れてきました。

{{< youtube zADp_K8gzoM >}}

### まとめ

これらの機能をうまく使うと楽しいルンバロボットにできるのではないかと思います。

今回試したtopicはGitHubにまとめておきました。

- [RoombaControlls/roomba\_subscribers.md at main · docofab/RoombaControlls (github.com)](https://github.com/docofab/RoombaControlls/blob/main/ROS2/roomba_subscribers.md)
