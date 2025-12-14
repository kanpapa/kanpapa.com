---
title: PDP-11をARTY FPGAボードで動かしてみた(2) OpenCores開発環境の準備
date: 2016-06-05
slug: pdp-11-arty-fpga-2-opencores
categories:
- retrocomputing
tags:
- arty
- fpga
- pdp-11
---

[Vivadoの開発環境](https://kanpapa.com/2016/06/pdp-11-arty-fpga-1-vivado.html "Vivadoの開発環境整備")がインストールできたところで、次はOpenCoresの開発環境を準備します。

## OpenCoresのアカウントを取得する。

OpenCoresのページからアカウントを登録します。このアカウントでOpenCoresのsvnからソースツリーを取得することができます。  
[http://opencores.org/](http://opencores.org/ "http://opencores.org/")

## 必要なパッケージのインストール

開発環境に必要なパッケージをLinux環境にインストールします。

- build-essential
- libboost-dev
- libboost-date-time-dev
- libboost-thread-dev
- libboost-regex-dev
- libusb-1.0-0-dev
- tcl
- tcl-dev
- tcllib
- tclreadline
- subversion

<!--more-->

## PDP-11のソースツリーをチェックアウト

OpenCoresのPDP-11のソースツリーをsvnでチェックアウトします。作業用のディレクトリはoc\_w11としましたが、任意の名前で構いません。

```
$ cd$ mkdir oc_w11$ cd oc_w11$ svn --username OCアカウント co http://opencores.org/ocsvn/w11/w11/trunkパスワードを聞いてくるのでOpenCoresのパスワードを入力する。   :A    trunk/.cvsignoreA    trunk/MakefileU   trunkリビジョン 35 をチェックアウトしました。$
```

## 環境変数を設定する

ドキュメントにあるように環境変数を設定します。Vivadoで必要な環境変数もここで設定してしまいました。

```
export RETROBASE=/home/ocha/oc_w11/trunkexport PATH=$PATH:$RETROBASE/tools/binexport LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RETROBASE/tools/libexport MANPATH=$MANPATH:$RETROBASE/doc/man#export TCLINC=/usr/include/tcl8.6export TCLLIBNAME=tcl8.6#export XTWV_PATH=/opt/Xilinx/Vivado/2016.1# for Vivado 2016.1export XILINX_VIVADO=/opt/Xilinx/Vivado/2016.1export PATH=$PATH:/opt/Xilinx/Vivado/2016.1/binexport LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/Xilinx/Vivado/2016.1/lib/lnx64.o 
```

## TCLの環境設定を行う

OpenCoresの開発環境ではTCLが使用されているので、TCLの環境設定を行います。

```
$ cd $RETROBASE/tools/tcl$ ./setup_packages　：$ cp .tclshrc ~/.$ cp .wishrc ~/.
```

## ツールをコンパイルする。

後の作業で必要となるツールプログラムをmakeします。

```
$ cd $RETOROBASE/tools/src$ makemake -C librtools　　：$ 
```

これでOpenCoresの開発環境の整備は完了です。

続いて[ARTY FPGAボードのコンフィグレーション](https://kanpapa.com/2016/06/pdp-11-arty-fpga-3-fpgaconfig.html "FPGAのコンフィグレーション")を行います。
