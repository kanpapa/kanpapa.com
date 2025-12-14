---
title: "ROSのPub/SubでLチカをしてみました"
date: 2022-05-14
categories: 
  - "robot"
coverImage: "ros_blink_led.jpg"
---

ROS MelodicをインストールしたRaspberry PiのGPIOを使ってLチカをやってみました。

![ros_blink_led.jpg](images/ros_blink_led.jpg)

### pigpioのインストール

GPIOを制御するライブラリとしてpigpioを使用します。このRaspberry Piはubuntu 18.04 LTSで動いているので、ソースからbuildを行います。

公式サイトの情報に従ってダウンロードとインストールを行います。

- [pigpio library Download & Install](http://abyz.me.uk/rpi/pigpio/download.html "pigpio library Download & Install")

```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

インストールが終わったら、公式サイトの手順にあるようにテストプログラムを実行して正常にインストールされたかを確認します。

<!--more-->

### pigpioの動作確認

GPIO17（ピン11）をHighにしてみます。

これはからあげさんの記事を参考にしています。

- [Raspberry PiのGPIO制御の決定版 pigpio を試す](https://karaage.hatenadiary.jp/entry/2017/02/10/073000 "Raspberry PiのGPIO制御の決定版 pigpio を試す")

掲載されているサンプルプログラムを動かしてピン11がHighになることを確認しました。

### ROSのPublisher/Subscriberの実装

ROS MelodicのPublisher/Subscriberの仕組みを使ってLチカを実装してみます。ここはツクレルさんの記事を参考にしています。

- [ROS Melodic Moreniaを使ってPub/Subでサーボモータを動かす](https://blog.tkrel.com/9301 "ROS Melodic Moreniaを使ってPub/Subでサーボモータを動かす")

SubscriberではGPIOを制御します。トピックに含まれる情報に従ってGPIOをHigh/Lowに設定します。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# gpio_test sub.py

import rospy
import pigpio
from std_msgs.msg import String

GPIO_PIN = 17

pi = pigpio.pi()
pi.set_mode(GPIO_PIN, pigpio.OUTPUT)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    pi.write(GPIO_PIN, p_out)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
```

Publisherは1Hzの周期で"0"と"1"の情報をトピックで送っています。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1) # 1hz

    i = 0

    while not rospy.is_shutdown():
        msg = str(i)
        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()

        if i == 0:
            i = 1
        else:
            i = 0

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
```

このPublisher/SubscriberによりGPIOが1Hzの周期でHigh/Lowが設定されます。

### ROSパッケージの作成

今回のパッケージはgpio\_testという名前にして以下の手順で作成しました。Publisherはpub.py、Subscriberはsub.pyとしました。

```
cd ~/catkin_ws/src
mkdir gpio_test
cd gpio_test
catkin_create_pkg gpio_test roscpp rospy std_msgs
cd gpio_test/src
vi pub.py
vi sub.py
chmod +x pub.py sub.py

source ~/.bashrc
```

### Lチカの動作確認

このサンプルを動作させてみます。

新たにターミナルを開き以下を実行します。

```
roscore
```

別のターミナルを開き以下を実行します。

```
rosrun gpio_test sub.py
```

別のターミナルを開き以下を実行します。

```
rosrun gpio_test pub.py
```

無事Lチカができました。
