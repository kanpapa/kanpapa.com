---
title: PDP-11をARTY FPGAボードで動かしてみた
date: 2016-06-05
slug: pdp-11-arty-fpga
categories:
- retrocomputing
tags:
- arty
- fpga
- pdp-11
image: images/arty_fpga_board.jpg
---

OpenCoresというサイトに[FPGAでPDP-11を動かすプロジェクト](http://opencores.org/project,w11 "PDP-11/70 CPU core and SoC")があったので、Xilinx Artix-7が載ったDIGILENTの[ARTY](http://akizukidenshi.com/catalog/g/gM-10034/ "ARTY")というFPGA評価ボードでPDP-11を動かしてみました。

2024/8現在 プロジェクトページは[GitHub](https://wfjm.github.io/home/w11/)に移動したようです。

https://wfjm.github.io/home/w11

![arty_fpga_board.jpg](images/arty_fpga_board.jpg)

開発環境の設定でかなり試行錯誤しましたが、なんとかUNIX V5まで動かすことができました。

![pdp11_v5unix.png](images/pdp11_v5unix.png)

動かすための手順については以下にまとめました。

- [PDP-11をARTY FPGAボードで動かしてみた(1) Vivado開発環境の準備](https://kanpapa.com/2016/06/pdp-11-arty-fpga-1-vivado.html)
- [PDP-11をARTY FPGAボードで動かしてみた(2) OpenCores開発環境の準備](https://kanpapa.com/2016/06/pdp-11-arty-fpga-2-opencores.html)
- [PDP-11をARTY FPGAボードで動かしてみた(3) FPGAのコンフィグレーション](https://kanpapa.com/2016/06/pdp-11-arty-fpga-4-unix-v5.html)
- [PDP-11をARTY FPGAボードで動かしてみた(4) UNIX V5を動かす](https://kanpapa.com/2016/06/pdp-11-arty-fpga-4-unix-v5.html)
