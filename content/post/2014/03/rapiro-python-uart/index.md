---
title: "RAPIROをpythonで動かしてみました"
date: 2014-03-08
slug: "rapiro-python-uart"
categories: 
  - "robot"
tags: 
  - "rapiro"
image: "images/rapiro_uart.jpg"
---

RAPIROと遊ぶ時間がなかなか取れなかったのですが、少し遊んでみました。

先日RAPIROに取り付けたRaspberry Piにログインして、pythonでRAPIROを動かしてみました。

サンプルプログラムを参考にしてテストプログラムを作りました。単純にUARTにコマンドを投げるだけのシンプルなものです。

```
import sys
import serial
import os
import time
import datetime

com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
sys.stdout.write('write #M0\n')
com.write("#M0")
time.sleep(5)
sys.stdout.write('write #M1\n')
com.write("#M1")
time.sleep(5)
sys.stdout.write('write #M2\n')
com.write("#M2")
time.sleep(5)
sys.stdout.write('write #M7\n')
com.write("#M7")
time.sleep(5)
sys.stdout.write('write #M0\n')
com.write("#M0")
```

これを実行してみました。

```
$ sudo python rapiro_test.py
write #M0
write #M1
write #M2
Traceback (most recent call last):
File "rapiro_test.py", line 19, in
com.write("#M2")
File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 485, in write
raise SerialException('write failed: %s' % (v,))
serial.serialutil.SerialException: write failed: [Errno 5] Input/output error
$
```

なぜかエラーがでます。  
調べたところUARTはOSのコンソールになっているということがわかりました。  
psコマンドで確認すると

```
$ ps ax | fgrep AMA
2039 ?        Ss+    0:00 /sbin/getty -L ttyAMA0 115200 vt100
2055 pts/0    S+     0:00 fgrep --color=auto AMA
```

確かにgettyがttyAMA0を使っています。  
とりあえずコンソールから切り離します。まずはcmdline.txtの修正。  
`       $ sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt      $ sudo vi /boot/cmdline.txt       `  
これを  
`       dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait       `  
こうしました。  
`       dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait       `  
次にinittabの修正  
`       $ sudo vi /etc/inittab       `  
これを  
`       #Spawn a getty on Raspberry Pi serial line      T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100       `  
コメントアウトしました。  
`       #Spawn a getty on Raspberry Pi serial line      #T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100       `  
rebootして確認  
`       $ ps ax | fgrep AMA      2069 pts/0 S+ 0:00 fgrep --color=auto AMA       `  
これで大丈夫。pythonで正常に動くようになりました。

![](images/rapiro_uart.jpg)
