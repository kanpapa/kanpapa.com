---
title: 'TurtleBot2 kobukiがやってきた #9（ROS2 NAV2編）'
date: 2024-09-07
slug: turtlebot2-kobuki-9-ros2-nav2
categories:
- robot
tags:
- humble
- kobuki
- nav2
- ros2
- slam
- turtlebot2
image: images/turtlebot2-kobuki-9-ros2-nav2-09051753.jpg
---

前々回に[机の上という狭い範囲でSLAM](https://kanpapa.com/2024/05/turtlebot2-kobuki-6-ros2-slam.html)を行ってみましたが、電源ケーブルも取り外して広々と動けるようになったので広い範囲でSLAMを行い、環境地図情報を作成したのちにNAV2で目的地までの自律走行を行ってみます。

## SLAMで環境地図を作成する

[前々回に行った手順](https://kanpapa.com/2024/05/turtlebot2-kobuki-6-ros2-slam.html)とほぼ同様ですが、最後に作成した環境地図の情報を保存する作業が必要です。

### SBCでの操作

kobuki のRaspberry Pi 4にsshでログインして各ノードを起動します。ここではまとめて記載していますが、個々にターミナルを開いて実行します。

```
ros2 launch kobuki_node kobuki_node-launch.py
ros2 launch kobuki_description robot_description.launch.py
ros2 launch ydlidar_ros2_driver ydlidar_launch.py
```

### デスクトップPCでの操作

デスクトップPCのターミナルから各ノードを起動します。ここではまとめて記載していますが、個々にターミナルを開いて実行します。

```
ros2 launch slam_toolbox online_async_launch.py
rviz2
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=commands/velocity
```

### 環境地図の作成

kobukiをキーボードで動かして、環境地図を作成していきます。

![](images/turtlebot2-kobuki-9-ros2-nav2-rviz1.png)

十分な環境地図ができたら別のターミナルで以下のコマンドを実行して環境地図を保存します。

```
ros2 run nav2_map_server map_saver_cli -f ~/map
```

この結果、ホームディレクトリに以下の２つのファイルが保存されます。

```
ocha@ocha-ubuntu:~$ ls -l map*
-rw-rw-r-- 1 ocha ocha 105687  5月 11 11:40 map.pgm
-rw-rw-r-- 1 ocha ocha    121  5月 11 11:40 map.yaml
```

この環境地図をもとにしてNAV2で自律走行を行います。地図の2D情報はmap.pgmに保存されており、画像ビューワーでも確認できます。今回はこのような地図が作成できました。

![](images/turtlebot2-kobuki-9-ros2-nav2-map-pgm.png)

## Nav2で自律走行してみる

### SBCでの操作

Raspberry Pi 4側ではSLAMで使用したノードをそのまま使用します。

```
ros2 launch kobuki_node kobuki_node-launch.py
ros2 launch kobuki_description robot_description.launch.py
ros2 launch ydlidar_ros2_driver ydlidar_launch.py
```

### Desktop PCでの操作

Navigation2は公式サイトのtutorialにある[Navigating with a Physical Turtlebot 3](https://docs.nav2.org/tutorials/docs/navigation2_on_real_turtlebot3.html)を参考にして動かしました。

https://docs.nav2.org/tutorials/docs/navigation2\_on\_real\_turtlebot3.html

ドキュメントに従ってターミナルからNav2を起動します。

```
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False map:=$HOME/map.yaml
```

別のターミナルからRviz2を起動します。

```
ros2 run rviz2 rviz2 -d $(ros2 pkg prefix nav2_bringup)/share/nav2_bringup/rviz/nav2_default_view.rviz
```

この状態で再度Nav2を立ち上げたところ、Rviz2に地図が表示されました。

![](images/turtlebot2-kobuki-9-ros2-nav2-rviz2-1.png)

### トピック名を変換するノードの作成

Nav2からロボットに対して送信される移動のためのトピック名は/cmd\_velですが、kobukiではこのトピック名が/commands/velocityのため、kobukiでトピックが受信できません。これを解決するにはトピック名の書き換えが必要となります。トピック名をremapしてみたのですが、書き換えてはいけないトピック名まで書き換わってしまったので、トピック名の書き換えをするノードを新たに作りました。

今回作成したkobuki\_cmdvelパッケージです。ノードのソースはシンプルなものになります。

https://github.com/kanpapa/kobuki\_cmdvel/blob/main/kobuki\_cmdvel/kobuki\_cmdvel\_function.py

ノードの実行は以下のように行います。

```
ros2 run kobuki_cmdvel kobuki_cmdvel
```

このノードで正しくトピック名が置換されるかテストしてみました。rqt\_graphで確認すると動作は一目瞭然です。購読している/cmd\_velが/commands/velocityに書き換わっています。

![](images/turtlebot2-kobuki-9-ros2-kobuki-cmdvel1.png)

NAV2を実行する際はこのノードを動かしておけば大丈夫なはずです。

再度、Nav2を動かしてrqt\_graphで確認したところ、/cmd\_velトピックがkobuki\_cmdvel\_subscriberノードによって/commands/velocityトピックに変換されkobukiノードが購読していることが確認できました。

![](images/turtlebot2-kobuki-9-ros2-kobuki-cmdvel3.png)

## 自律走行の確認

この状態で再度自律走行を確認してみます。細かい手順は[Navigating with a Physical Turtlebot 3](https://docs.nav2.org/tutorials/docs/navigation2_on_real_turtlebot3.html)のページにも掲載されていますのでそちらも参考にしてください。

SLAMの時と同様にteleop\_twist\_keyboardを別のターミナルから起動します。

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=commands/velocity
```

まずKobukiの位置と向きを2D Pose Estimateで調整します。そのあとにteleop\_twist\_keyboardで本体を少しずつ回転させると地図上のkobukiの位置が調整されます。ある程度収束したところでNav2 Goalで目的地を指定するとその場所にkobukiが移動することが確認できました。

![](images/turtlebot2-kobuki-9-ros2-nav2-rviz2.png)

実際にNav2で移動している動画を載せておきました。Rviz2のNav2 Goalで指定したポイントと方向に動くことが確認できました。

https://youtu.be/\_I1T2YvwBOo

## まとめ

ROS2 humbleを使用してKobukiで自律走行ができることが確認できました。まだしばらくはROS2の実験用として活用できそうです。Kobukiの筐体には様々な機器が取り付けられるテーブルやネジ穴もありますのでRealSenseカメラなども取り付けてみようと思います。
