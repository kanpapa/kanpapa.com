---
title: "KitKatベースのFirefox OS 2.1 Flameに日本語IMEをいれてみた"
date: 2014-10-13
slug: "firefox-os-21-kitkat-flame-ime-jp"
categories: 
  - "mobile"
tags: 
  - "firefox-os"
---

FlameのベースイメージがBase image v180.zipに変わっていたので、これを使ってリカバリしてみたら、どうもKitKatベースのシステムになったようです。  
そういえば、Flameのページに載っているnightly buildも2.0、2.1、2.2といつの間にか変わっていました。しかも、このnightly buildは最初から日本語表示ができるようになっています。これを使えば簡単に日本語IMEの組み込みまでできるのではと考えました。

以下の手順で進めました。（作業環境はubuntuを使っています。）

**1\. Base image v180.zipをインストールして、FlameをKitKatの環境にする。**

```
$ ls
Flame_2.0_v180_1.zip
$ unzip Flame_2.0_v180_1.zip
Archive: Flame_2.0_v180_1.zip
creating: Flame_2.0_v180_1/
inflating: Flame_2.0_v180_1/#flash.sh#
inflating: Flame_2.0_v180_1/boot.img
:
$ chmod +x flash.sh
$ ./flash.sh

```

  
KitKatベースのFirefox OS 2.0で、Flameが立ち上がります。この時点では日本語は表示されません。

**2\. Engineering buildsのLatest aurora builds (currentry 2.1)をFlameに入れる。**

最初はcurrentry 2.2で試していたのですが、たまに落ちたりしてまだ不安定に見えましたので、今回はcurrentry 2.1を使いました。また、2.1だとAPNパッチがなくても動作しました。

```
$ ls
b2g-34.0a2.en-US.android-arm.tar.gz gaia.zip shallow_flash.sh
$ ./shallow_flash.sh -ggaia.zip -Gb2g-34.0a2.en-US.android-arm.tar.gz
Are you sure you want to flash
Gaia: gaia.zip
Gecko: b2g-34.0a2.en-US.android-arm.tar.gz
to your Device? [y/N]y
### Waiting for device... please ensure it is connected, switched on and remote debugging is enabled in Gaia
### Restarting adb with root permissions...
　　：（省略）
24 files pushed. 0 files skipped.
3135 KB/s (39144521 bytes in 12.193s)
### Push Done.
### Shallow Flash Successful!
$

```

これで、Firefox OS 2.1になります。何もしなくても日本語表示が可能です。でも、日本語IMEは使えないです。

**3\. Firefox OS 2.1のソースを落としてきて、gaiaだけbuildし、日本語キーボードを組み込む。**

```
$ cd ~$ git clone git://github.com/mozilla-b2g/B2G.git
$ cd ~/B2G
$ BRANCH=v2.1 ./config.sh flame-kk
$ cd gaia/locales/
$ hg clone http://hg.mozilla.org/gaia-l10n/ja
$ cp languages_dev.json languages_ja.json
$ vi languages_ja.json
{
"en-US" : "English (US)",
"ja" : "日本語"
}
$ cd ~/B2G
$ vi .userconfig
## Gaia
export LOCALE_BASEDIR=$PWD/gaia/locales
export LOCALES_FILE=$PWD/gaia/locales/languages_ja.json
export GAIA_DEFAULT_LOCALE=ja
export GAIA_KEYBOARD_LAYOUTS=en,jp-kanji
$ ./build.sh gaia
including device/qcom/common/vendorsetup.sh
including device/generic/armv7-a-neon/vendorsetup.sh
　：（省略）
real 0m43.356s
user 0m38.001s
sys 0m6.989s
Run |./flash.sh| to flash all partitions of your device
$

```

**4\. gaiaだけFlameに書き込む。**

```
$ ./flash.sh gaiaDetect GAIA_INSTALL_PARENT ...　：（省略）Push to /system/b2g ...$
```

これで、日本語IMEが組み込まれたFirefox OS 2.1 Flameができあがります。

gaiaのビルドはそんなに時間がかからないので、この方法で行うと短時間で日本語IMEが動くようになります。
