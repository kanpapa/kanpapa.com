---
title: ROS2とM5Stackをmicro-ROSで通信してみました (1) publisher編
date: 2022-09-29
slug: ros2-m5stack-microros
categories:
  - "Electronics"
  - "Robot"
tags:
  - "electronics"
  - "m5stack"
  - "robot"
  - "ros2"
image: images/ros2-m5stack-microros_sample.jpg
---

ESP32をつかってmicro-ROS for ArduinoでROS2と通信できるという記事を見かけました。

- [\[ROS2 foxy\] ESP32を使ってmicro-ROS for Arduinoで遊ぼう](https://qiita.com/ousagi_sama/items/b4eb3d9c6b337cbe1b05 "[ROS2 foxy] ESP32を使ってmicro-ROS for Arduinoで遊ぼう")

ESP32でできるならM5Stackでも同じことができそうだと試してみました。

手順は先ほどのQiitaの記事を参考にしています。

![ros2-m5stack-microros_sample.jpg](images/ros2-m5stack-microros_sample.jpg)

今回はM5Stack Fireを使いました。ROS2 Foxyの環境はVMWare Workstaion Player上のUbuntu 20.04 LTSです。



## マイコン(M5Stack）側の設定

M5StackにおけるArduinoIDEの使い方は一般的なので簡単にまとめます。検索すれば詳細に説明されているホームページが多数見つかりますのでそれらも参考にしてください。

### ArduinoIDEにM5Stackの開発環境を導入

これは[M5Stack公式マニュアル](https://docs.m5stack.com/en/arduino/arduino_development "M5Stack Arduino IDE Development")通りにすすめます。すでにM5Stackの開発環境がセットアップされていれば不要です。

1. 「ファイル」→「環境設定」→「追加のボードマネージャーのURLを設定」で https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/arduino/package_m5stack_index.json を指定。
1. 「ツール」→「ボード」→「ボードマネージャー」→「M5Stack」を検索してインストール
1. 「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理...」から「M5Stack」ライブラリをインストール

これでM5Stackの開発環境ができました。「ファイル」→「スケッチ例」→「M5Stack」にM5Stackのサンプルプログラムがあるので適当なものをM5Stackに書き込んで動作することを確認してください。

### ArduinoIDEにmicro-ROS for Arduinoのライブラリを導入

GitHubにある[micro-ROS for Arduino公式マニュアル](https://github.com/micro-ROS/micro_ros_arduino "micro-ROS library for Arduino ")の通りにすすめます。今回はROS2 foxyですので、[v2.0.5-foxyリリース](https://github.com/micro-ROS/micro_ros_arduino/releases/tag/v2.0.5-foxy "v2.0.5-foxy")を使用しました。

GitHubに登録されているZIPファイルをダウンロードし、Arduino IDEの「ライブラリの管理...」の「.Zip形式のライブラリをインストール」で読み込みます。

正常に読み込めればライブラリの一覧に「micro_ros_arduino」が追加されます。

### micro-ROSのサンプルプログラムのビルドとM5Stackへの書き込み

micro-ROSのサンプルプログラム([micro-ros_publisher_wifi.ino](https://github.com/micro-ROS/micro_ros_arduino/blob/foxy/examples/micro-ros_publisher_wifi/micro-ros_publisher_wifi.ino "micro-ros_publisher_wifi.ino"))をM5Stack用に修正したものを使います。

今回はM5Stackのバッテリーレベルをtopicとして配信するようにしました。WiFiの設定のところはWiFiのSSIDとパスフレーズとmicro-ROS-Agentが動作するPCのIPアドレスに書き換える必要があります。

ソースコードは[GitHub](https://github.com/kanpapa/micro_ros_arduino/blob/main/micro-ros_m5stack_publisher_wifi/micro-ros_m5stack_publisher_wifi.ino "micro-ros_m5stack_publisher_wifi.ino")に登録しておきました。

## PC側の設定

これも[micro-ROS-Agentの公式マニュアル](https://github.com/micro-ROS/micro_ros_setup "micro_ros_setup")に沿って設定します。なお、環境変数 ROS_DOMAIN_IDを設定していると動作しませんので、unset ROS_DOMAIN_ID で環境変数を削除してください。

### micro-ROS-Agentのセットアップ

```
source /opt/ros/$ROS_DISTRO/setup.bash
mkdir uros_ws && cd uros_ws
git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup
rosdep update && rosdep install --from-paths src --ignore-src -y
colcon build
source install/local_setup.bash
```

### micro-ROS-Agentをビルドして実行します。

```
cd ~/uros_ws  
ros2 run micro_ros_setup create_agent_ws.sh
ros2 run micro_ros_setup build_agent.sh
source install/local_setup.sh
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```
micro-ROSが動いているM5StackとAgentがつながると以下のような画面になります。

![ros2-m5stack-microros_agent.png](images/ros2-m5stack-microros_agent.png)

### トピックの確認

この状態で正常に動いていればtopicが流れてくるはずです。

```
ros2 topic listros2 topic echo /battery_level
```

![ros2-m5stack-microros_topic.png](images/ros2-m5stack-microros_topic.png)

## 今後の応用

M5Stackには表示画面と操作ボタンがついていてそれらを制御するための豊富なM5Stackライブラリが使えます。

うまく応用できれば簡単なコントローラーとしてROS2のトピックを流して、ロボット本体に指示を与えることもできそうです。

続いて、subscriberも試してみました。

- [ROS2とM5Stackをmicro-ROSで通信してみました (2) subscriber編](https://kanpapa.com/2022/10/ros2-m5stack-microros-subscriber.html "ROS2とM5Stackをmicro-ROSで通信してみました (2) subscriber編")