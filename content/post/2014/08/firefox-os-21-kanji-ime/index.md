---
title: "日本語IMEを組み込んだFirefox OS 2.1をFlameに書き込んでみた"
date: 2014-08-16
slug: "firefox-os-21-kanji-ime"
categories: 
  - "mobile"
tags: 
  - "firefox-os"
image: "images/fxos21_kanji_ime.jpg"
---

Firefox OS 2.1をビルドして日本語IMEを組み込みFlameに書き込んでみました。  
ビルド環境はubuntu 14.04 LTS (64bit) です。  
以下手順の抜粋です。抜け漏れあるかもしれません。  
思考錯誤で行いましたので、手順でおかしなところがあるかもしれませんが、そこは自己責任でお願いします。

まずは、Firefox OS 2.1のNightlyをBuildする環境をつくります。

```
$ sudo apt-get install --no-install-recommends autoconf2.13 bison bzip2 ccache curl flex gawk gcc g++ g++-multilib gcc-4.6 g++-4.6 g++-4.6-multilib git lib32ncurses5-dev lib32z1-dev zlib1g:amd64 zlib1g-dev:amd64 zlib1g:i386 zlib1g-dev:i386 libgl1-mesa-dev libx11-dev make zip libxml2-utils
$ cd
$ git clone git://github.com/mozilla-b2g/B2G.git
$ cd B2G
$ ./config.sh flame
$ ./build.sh
```

ここでビルドしたFirefox OS 2.1をFlameに書き込んで動作することを確認します。

次に日本語辞書を入手します。  
http://sourceforge.jp/projects/naist-jdic/releases/  
naist-jdic-0.4.3.tar.gzをダウンロード

ダウンロードした日本語辞書を適当なところに展開します。

```
$ cd ~
$ zcat naist-jdic-0.4.3.tar.gz | tar xvf -
$ cd naist-jdic-0.4.3
$ ls -l *.dic
```

dicファイルをコピーして辞書を作ります。

```
$ cd ~/B2G/gaia/apps/keyboard/js/imes/jskanji
$ cat README
$ cd dict
$ mkdir ipadic
$ cp ~/naist-jdic-0.4.3/*.dic ipadic/.
$ make
```

dict.jsonができているはずです。

Makefileに日本語キーボードを指定する。

```
$ cd ~/B2G/gaia
$ cp Makefile Makefile.org
$ vi Makefile
$ diff Makefile.org Makefile
*** Makefile.org	2014-08-12 01:19:13.466204000 +0900
--- Makefile	2014-08-12 02:18:46.746204000 +0900
***************
*** 395,401 ****
GAIA_CONCAT_LOCALES?=1
# This variable is for customizing the keyboard layouts in a build.
! GAIA_KEYBOARD_LAYOUTS?=en,pt-BR,es,de,fr,pl,zh-Hans-Pinyin,en-Dvorak
ifeq ($(SYS),Darwin)
MD5SUM = md5 -r
--- 395,402 ----
GAIA_CONCAT_LOCALES?=1
# This variable is for customizing the keyboard layouts in a build.
! #GAIA_KEYBOARD_LAYOUTS?=en,pt-BR,es,de,fr,pl,zh-Hans-Pinyin,en-Dvorak,jp-kanji
! GAIA_KEYBOARD_LAYOUTS?=en,jp-kanji
ifeq ($(SYS),Darwin)
MD5SUM = md5 -r
```

日本語リソースの組み込み  
https://hg.mozilla.org/releases/gaia-l10n/v2\_0から日本語リソースをダウンロード  
ダウンロードした日本語リソースをホームディレクトリに展開

```
$ cd
$ unzip ja-7222e75b66ca.zip
$ ls -l ja-7222e75b66ca/
$ cd
$ mv ja-7222e75b66ca ~/B2G/gaia/locales/ja
$ cd ~/B2G/gaia/locales/
$ cp languages_dev.json languages_own.json
$ vi languages_own.json
$ diff -rc languages_dev.json languages_own.json
*** languages_dev.json	2014-08-11 07:51:24.924547000 +0900
--- languages_own.json	2014-08-12 02:24:28.094204000 +0900
***************
*** 1,39 ****
{
- "ar" : "عربي",
- "bg" : "български",
- "bn-BD" : "বাংলা (বাংলাদেশ)",
- "ca" : "Català",
- "cs" : "Čeština",
- "da" : "Dansk",
- "de" : "Deutsch",
- "el" : "Ελληνικά",
"en-US" : "English (US)",
! "es" : "Español",
! "eu" : "Euskara",
! "fr" : "Français",
! "gl" : "Galego",
! "hr" : "Hrvatski",
! "hu" : "Magyar",
! "it" : "Italiano",
! "ja" : "日本語",
! "km" : "ខ្មែរ",
! "ko" : "한국어",
! "lt" : "Lietuvių",
! "mk" : "Македонски",
! "ms" : "Melayu",
! "ne-NP" : "नेपाली",
! "nl" : "Nederlands",
! "pa" : "ਪੰਜਾਬੀ",
! "pl" : "Polski",
! "pt-BR" : "Português (do Brasil)",
! "ro" : "Română",
! "ru" : "Русский",
! "sk" : "Slovenčina",
! "sq" : "Shqip",
! "sr-Cyrl" : "Српски",
! "sr-Latn" : "Srpski",
! "sv-SE" : "Svenska",
! "tr" : "Türkçe",
! "zh-CN" : "中文 (简体)",
! "zh-TW" : "正體中文 (繁體)"
}
--- 1,4 ----
{
"en-US" : "English (US)",
! "ja" : "日本語"
}
```

環境変数を設定

```
$ export LOCALE_BASEDIR=$PWD/gaia/locales
$ export GAIA_DEFAULT_LOCALE=ja
$ export LOCALES_FILE=$PWD/gaia/locales/languages_own.json
```

APNのパッチを行う。

$ cd $ unzip firefoxos-patch-master.zip $ cd ~/B2G/gaia/shared/resources $ patch apn.json ~/firefoxos-patch-master/apn.json.diff

gaiaを再ビルドする。

```
$ cd ~/B2G
$ ./build.sh gaia
```

Flameに書き込み

```
$ cd ~/B2G
$ ./flash.sh
```

これで日本語入力ができるようになります。  
ここではまだFMラジオパッチを組み込んでいませんが、このビルドツリーに反映してしまえば毎回パッチも不要です。

![fxos21_kanji_ime.jpg](images/fxos21_kanji_ime.jpg)
