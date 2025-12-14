---
title: 'TurtleBot3がやってきた #4（SLAMで地図を作る編）'
date: 2022-02-06
slug: turtlebot3-burger-slam1
categories:
- robot
tags:
- melodic
- ros1
- slam
- turtlebot3
image: images/turtlebot3-burger-slam-map1.png
---

[TurtleBot3のROS環境が整いました](https://kanpapa.com/2022/02/turtlebot3-burger-assembly3.html "TurtleBot3がやってきた（ROSセットアップ編）")ので実際に走行させてみることにします。

### PS4のDualShock4でTurtleBot3を動かす

これまではキーボードでTurtleBot3の移動方向や速度を指示していましたが、これだと少し扱いにくいです。そこでPS4のワイヤレスコントローラー DualShock4で操縦するように設定します。

![turtlebot3-burger-ps4-dualshock4.jpg](images/turtlebot3-burger-ps4-dualshock4.jpg) <!--more-->

以下の記事を参考にしました。

- [Turtlebot3をPS4コントローラーDUALSHOCK 4で動かしてみた(有線接続)](https://www.sato-susumu.com/entry/tb3-ds4 "Turtlebot3をPS4コントローラーDUALSHOCK 4で動かしてみた(有線接続)")　佐藤百貨店

Bluetoothでの無線接続もできるようなのですが、VMWareを使っているためかUbuntuでのBluetooth接続がうまくできません。これはまた別の機会に試してみます。

必要なパッケージのインストールを行った後に、/dev/input/js0にDualShock4が接続されていることを確認して以下のコマンドを入力します。

```
$ rosrun joy joy_node
```

新しいターミナルを開き次のコマンドを入力します。

```
$ roslaunch teleop_twist_joy teleop.launch
```

あとは、PSボタンかSHAREボタンを押したままで、左スティックをゆっくり操作するとその方向にTurtleBot3が動きました。時々赤い文字でエラーが表示されますが、特に問題無く動くようです。

少し慣れが必要ですが、これでTurttleBot3の操縦がしやすくなりました。

### SLAMで地図を作る

SLAM（Simultaneous Localization and Mapping）は現在の位置を推定して地図を作る技術です。TurtleBot3にはLiDARやエンコーダーといったセンサーが搭載されており、これらの情報を使って地図が作れます。この地図を使って、目的の場所まで自律走行が実現できます。

以下の手順でSLAMノードを実行します。

Ubuntu PCで新しくターミナルを開き、ROSマスターを動かします。

```
$ roscore
```

次に新しくターミナルを開き、TurtleBot3のRaspberry PiにログインしてBringupを動かします。

```
$ ssh ubuntu@192.168.100.59
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

さらに新しいターミナルを開き、Ubuntu PCでSLAMノードを動かします。

```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch
```

SLAMノードを動かすと、Rvizが表示されます。

さらに新しいターミナルを開き、先ほどのDualShock4のコントローラーが使えるようにします。この状態でDualShock4を操作して少しづつ空間を移動して地図を作っていきます。

一通り地図ができたところで、新しいターミナルを開き、次のコマンドを入力して地図を保存します。

```
$ rosrun map_server map_saver -f ~/map
```

### 生成された地図の確認

ホームディレクトリを見ると以下の２つのファイルが生成されています。

![turtlebot3-burger-slam-mapfiles.png](images/turtlebot3-burger-slam-mapfiles.png)

map.pgmは画像データなのでGIMPといった画像表示ツールですることができます。これが今回SLAMで生成された地図になります。

![turtlebot3-burger-slam-map1.png](images/turtlebot3-burger-slam-map1.png)

次はこの地図を使って[目的の場所までの自律走行にチャレンジ](https://kanpapa.com/2022/02/turtlebot3-burger-navigation1.html "TurtleBot3がやってきた（Navigationで自律走行編）")します。
