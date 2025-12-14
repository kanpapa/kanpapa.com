---
title: "TurtleBot3がやってきた #5（Navigationで自律走行編）"
date: 2022-02-06
categories: 
  - "turtlebot3"
tags: 
  - "melodic"
  - "navigation"
  - "ros1"
  - "turtlebot3"
coverImage: "turtlebot3-burger-navigation-rviz3.png"
---

[SLAMで作成した地図データ](https://kanpapa.com/2022/02/turtlebot3-burger-slam1.html "TurtleBot3がやってきた（SLAMで地図を作る編）")を使って自律走行を行います。

### Navigationノードの実行

以下の手順でNavigationノードを実行します。Ubuntu PCで新しくターミナルを開き、ROSマスターを動かします。

```
$ roscore
```

次に新しくターミナルを開き、TurtleBot3のRaspberry PiにログインしてBringupを動かします。

```
$ ssh ubuntu@192.168.100.59
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

新しいターミナルを開きNavigationノードを起動します。ここでSLAMで生成した地図を指定します。

```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```

正常に動作するとRvizの画面が表示されます。緑色の小さな矢印が散らばっていることがわかります。

![turtlebot3-burger-navigation-rviz1.png](images/turtlebot3-burger-navigation-rviz1.png) <!--more-->

### 初期位置の設定

Navigationを実行する前にTurtleBot3の初期位置を設定する必要があります。地図の位置と同じになるように正しく位置決めをしないといけません。これは以下の手順で行います。

1\. RVizメニューの2D Pose Estimateボタンをクリックします。

2\. 実際のTurtleBot3がいる地図上をクリックし、大きな緑色の矢印をロボットが向いている方向へドラッグします。

![turtlebot3-burger-navigation-rviz3.png](images/turtlebot3-burger-navigation-rviz3.png)

3\. 地図のデータとLiDARセンサーのデータが重なるまで、手順1、2を繰り返します。うまく重なると地図の線とLiDARセンサーの線がほぼ一致します。

![turtlebot3-burger-navigation-rviz4.png](images/turtlebot3-burger-navigation-rviz4.png)

4\. DualShock4のコントローラーノードを起動します。新しいターミナルを開き次のコマンドを入力します。

```
$ rosrun joy joy_node
```

5\. 新しいターミナルを開き次のコマンドを入力します。

```
$ roslaunch teleop_twist_joy teleop.launch
```

6\. DualShock4のコントローラーでTurtleBot3を少し前後に移動したり回転をすると周囲の情報を収集し、地図上の推定位置を絞り込んでいきます。この結果、緑色の矢印が集束してきます。

![turtlebot3-burger-navigation-rviz5.png](images/turtlebot3-burger-navigation-rviz5.png)

7\. 初期位置の設定作業が終わったら、DualShock4のコントローラノードのターミナルでCtrl + Cを入力してノードを終了し、Navigator以外のcmd\_velのトピックが発生しないようにします。

### 目的地の設定と移動

地図上のどの地点に移動するかを以下の手順で指定します。

1\. RVizメニューの2D Nav Goalボタンをクリックします。

2\. TurtleBot3の目的地を地図上でクリックします。

3\. 目的地が設定されると、TurtleBot3は経路を決めて目的地に向かって移動を開始します。

Rvizの画面で目的地まで移動する様子をYouTubeにアップしておきました。

こちらは実際のTurtleBot3の動画です。

このように目的地に移動することができます。地図に無い障害物を認識した場合はそれにぶつからないような経路を選ぶことがわかります。

TurtleBot3は安定した動作で再現性が高くできていてマニュアルに沿って動かせば期待した動作をしてくれます。ROSのリファレンスロボットとして活躍してくれそうです。
