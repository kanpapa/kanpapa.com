---
title: "ルンバで地図をつくってみました #1 （おおたfab 第49回 素人でもロボットをつくりたい）"
date: 2021-10-24
categories: 
  - "robot"
  - "roomba"
tags: 
  - "roomba"
  - "otafab"
  - "otafab-robot"
coverImage: "real_roomba_rplidar_photo1.jpg"
---

[おおたfab](https://ot-fb.com/ "おおたfab")さんでは、「[素人でもロボットをつくりたい](https://ot-fb.com/iot/6353/ "素人でもロボットをつくりたい")」という勉強会を定期的に行っています。前回は[オドメトリ情報を使ってルンバ実機を動かしてみました](https://kanpapa.com/2021/10/Roomba-robot-ros-part5-otafab.html "ルンバ実機とGazeboシミュレーターのオドメトリ情報を比較してみました （おおたfab 第47回 素人でもロボットをつくりたい）")が、今回は新たに[LiDAR](https://ja.wikipedia.org/wiki/LIDAR "LiDAR")を使って地図の作成にチャレンジしてみます。

![real_roomba_rplidar_photo1.jpg](images/real_roomba_rplidar_photo1.jpg)

今回も[demura.net](https://demura.net/ "demura.net")さんの記事を参考にして進めています。

- [HARD2021：シミュレータで地図作成からナビゲーションまでしよう！](https://demura.net/robot/hard/20061.html "HARD2021：シミュレータで地図作成からナビゲーションまでしよう！")

<!--more-->

### Gazeboシミュレーターで地図を作ってみる

みなさんGazeboシミュレータにも慣れてきて、参考サイトの手順通りに操作を行うことができました。

地図の作成はキーボードでGazeboシミュレーターのルンバを動かすことで、シミュレーター搭載のLiDARの情報をもとに地図を作っていきます。ルンバを壁にぶつけてしまうと地図が乱れてしまうので、慎重に動かしていきます。

![gazebo_map_rviz_image1.png](images/gazebo_map_rviz_image1.png)

大体まわったところで、地図情報を保存します。モノクロ画像の形式であるpgmファイルと情報が含まれているyamlファイルが出力されます。pgmファイルを画像ビューアーで開くとこのような表示になりました。

![gazebo_map_sample1.png](images/gazebo_map_sample1.png)

きれいに地図ができました。

### Gazeboシミュレーターで自律走行をしてみる

次はシミュレーターで自律走行をしてみます。先ほど作成した地図を使うこともできるのですが、参考サイトの手順通りに操作を行い、ゴールの地点までルンバが自動的に動くことを確認しました。

### ルンバ実機で地図を作ってみる

シミュレーターで地図を作ることができたので、ルンバ実機と手持ちのLiDAR（RPLiDAR A1M8）で同様のことができないか実験をしてみました。探してみたところ[demura.net](https://demura.net/ "demura.net")さんの以下の記事を見つけました。

- [ROS: Roomba 800 地図生成](https://demura.net/robot/athome/15161.html "ROS: Roomba 800 地図生成")

しかし、この記事はROS Melodicではなく、ROS kineticで、LiDARもHokuyo Lidar(UTM-30 LX)という異なる構成です。しかし、流れは同じと考えて手順を起こしました。

またROSのオフィシャルサイトでも同様の手順が掲載されています。

- [How to Build a Map Using Logged Data](https://wiki.ros.org/slam_gmapping/Tutorials/MappingFromLoggedData "How to Build a Map Using Logged Data")

1. 以下を参考にROSとcreate\_autonomyをインストールしたRaspberry Pi 4(4GB)環境を準備する。 [https://github.com/docofab/RoombaControlls/blob/main/ROS/instructions/setup-gazebo-rasppi.md](https://github.com/docofab/RoombaControlls/blob/main/ROS/instructions/setup-gazebo-rasppi.md "setup-gazebo-rasppi.md")
2. Navigation & SLAM のインストール（もう入っているかも） $ sudo apt install ros-melodic-navigation $ sudo apt install ros-melodic-slam-gmapping
3. 新しいRPLIDAR ROS パッケージに置き換えたいので ros-melodic-rplidar-ros がインストールされていたらアンインストールする。 $ sudo apt remove ros-melodic-rplidar-ros
4. RPLIDAR ROS パッケージ rplidar\_rosをクローンする。 $ cd ~/catkin\_ws/src $ git clone https://github.com/Slamtec/rplidar\_ros.git $ catkin build rplidar\_ros $ source ~/.bashrc
5. 新しいターミナルを開き、ルンバ実機のドライバを実行する $ roslaunch ca\_driver create\_2.launch
6. 新しいターミナルを開き、ルンバをキーボードで操作できるようにする。 $ roslaunch ca\_tools keyboard\_teleop.launch
7. 新しいターミナルを開き、RPLiDARのノードを起動する。 $ roslaunch rplidar\_ros rplidar.launch
8. 新しいターミナルを開き、全Topicデータを記録する $ mkdir -p ~/bag $ cd ~/bag $ rosbag record -a
9. 6.のターミナルでキーボードを操作してロボットを動かし地図生成のためのデータを取得する。
10. 取得が終わったら、忘れずに、Ctrl-Cでrosbagを止める。
11. bagファイルを使って地図生成するための設定をする。 $ rosparam set use\_sim\_time true
12. SLAMを実行します。 $ rosrun gmapping slam\_gmapping
13. 取得したtopicの再生 $ rosbag play --clock "bagファイル名"
14. topicの再生が終了してから以下のコマンドを実行する。 $ mkdir -p ~/map $ cd ~/map $ rosrun map\_server map\_saver
15. ~/mapディレクトリにmap.pgmとmap.yamlが生成される。

ルンバ実機＋LiDARで地図データを取得している様子です。

実際に取得できた地図はこのようなものになりました。

![real_roomba_slam_map1.png](images/real_roomba_slam_map1.png)

思ったような地図は取れておらずもう少し確認が必要のようです。今回の実験では全Topicデータを取得しているので、LiDARのデータをRvizで確認したところ、scanトピックスはきちんととれているようにみえます。ルンバが回転するとレーザーが反射している赤い点も回転しているのがわかります。（少し見にくいですが）

他の部分で問題ないか、Topicsデータの内容の確認を進めてみます。

### 次回の予定

ルンバ実機での地図作成に再チャレンジしてみます。地図作成がうまくできれば自律走行にも少し近づきます。お楽しみに。
