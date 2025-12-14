---
title: "ubuntuのadbでModule LLMに接続してみました"
date: 2025-01-30
categories: 
  - "electronics"
  - "m5stack"
tags: 
  - "ax620"
  - "llm"
  - "m5stack"
  - "ubuntu"
  - "udev"
coverImage: "m5stack-module-llm1.jpg"
---

[M5Stack Module LLM](https://docs.m5stack.com/ja/module/Module-LLM)にWiFiドングルを接続するために、ubuntuの[Android Debug Bridge（adb）](https://developer.android.com/tools/adb?hl=ja)で接続しようとしたところ、少し設定が必要でしたのでまとめました。

## adbのインストール

私のubuntuにはadbがインストールされていなかったのでaptでインストールを行いました。

```
$ adb
コマンド 'adb' が見つかりません。次の方法でインストールできます:
sudo apt install adb
$ sudo apt install adb
```

このようにコマンド１つでインストールされます。

## adb接続時のエラー

ubuntu PCとModule LLMをUSBケーブルで接続して、adb devicesでデバイスを確認したところattachができず以下のエラーが表示されました。

```
$ adb devices
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached
axera-ax620e	no permissions (user in plugdev group; are your udev rules wrong?); see [http://developer.android.com/tools/device.html]
```

エラーメッセージにもあるように権限の問題でattachできないので、ユーザがplugdevグループに登録されているかとudevの設定を確認していきます。

## plugdevグループへの登録

groupsコマンドで現在使用しているユーザが所属するグループが表示されます。

```
$ groups
ocha adm dialout cdrom sudo dip plugdev lpadmin lxd sambashare docker ollama
$ 
```

このようにplugdevが表示されれば問題ありません。もし、表示されない場合は以下のコマンドでplugdevグループに登録します。

```
$ sudo usermod -aG plugdev $LOGNAME
```

## udevの設定

ubuntu PCにModule LLMをUSBケーブルで接続して、USBの状態を確認します。ここではax620eという文字列を探します。

```
$ lsusb 
Bus 002 Device 002: ID 174c:3074 ASMedia Technology Inc. ASM1074 SuperSpeed hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 007: ID 32c9:2003 axera ax620e-adb
Bus 001 Device 003: ID 174c:2074 ASMedia Technology Inc. ASM1074 High-Speed hub
Bus 001 Device 006: ID 2357:0115 TP-Link Archer T4U ver.3
Bus 001 Device 004: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
Bus 001 Device 002: ID 058f:6254 Alcor Micro Corp. USB Hub
Bus 001 Device 005: ID 0b05:19af ASUSTek Computer, Inc. AURA LED Controller
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
$ 
```

これでModule LLMのベンダーIDは32c9だとわかります。

この情報を元にして、/etc/udev/rules.d/51-android.rulesというファイルを作成し、以下の１行を書きます。

```
SUBSYSTEM=="usb", ATTR{idVendor}=="32c9", MODE="0666", GROUP="plugdev"
```

これにより、USBデバイスでベンダーIDが32c9のものが接続されたら、アクセス権限を666にし、plugdevのグループに設定されます。

なお、このファイルは全ユーザから読めるようにread権限を与えておきます。

```
$ cat /etc/udev/rules.d/51-android.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="32c9", MODE="0666", GROUP="plugdev"
$ sudo chmod a+r /etc/udev/rules.d/51-android.rules
```

次にudevをリスタートします。

```
$ sudo service udev restart
```

これでudevの設定は完了です。

## Module LLMにadbで接続してみる

一度Module LLMのUSBケーブルを外します。そしてもう一度USBケーブルを接続し、adb devicesコマンドで以下のように表示されれば接続できています。

```
$ adb devices
List of devices attached
axera-ax620e	device 
```

あとはadb shellでModule LLMにログインすることができます。

```
$ adb shell
sh-5.1# pwd
/
sh-5.1# ls
8188eu.ko  dev	 lib	     mnt    proc	     run   srv	usr
bin	   etc	 lost+found  opt    root	     sbin  sys	var
boot	   home  media	     param  rtl8188eufw.bin  soc   tmp
sh-5.1# 
```

## 終わりに

今回かModule LLMについてまとめましたが、他のUSBデバイスでも同様な流れになりますので参考にしてください。
