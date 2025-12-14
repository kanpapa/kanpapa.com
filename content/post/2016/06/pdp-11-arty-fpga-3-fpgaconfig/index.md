---
title: "PDP-11をARTY FPGAボードで動かしてみた(3) FPGAのコンフィグレーション"
date: 2016-06-05
slug: "pdp-11-arty-fpga-3-fpgaconfig"
categories: 
  - "pdp-11"
  - "retrocomputing"
tags: 
  - "arty"
  - "fpga"
  - "pdp-11"
---

[Vivadoの開発環境](https://kanpapa.com/2016/06/pdp-11-arty-fpga-1-vivado.html "Vivadoの開発環境整備")と[OpenCoresの開発環境](https://kanpapa.com/2016/06/pdp-11-arty-fpga-2-opencores.html "OpenCoresの開発環境")が準備できましたので、いよいよFPGAのコンフィグレーションを行います。

## bitstreamを作る

FPGAに書き込むためのbitstreamを生成します。実はbitstreamはOpenCoresのページにも用意されているのですが、試しにmakeをしてみたら簡単にbitstreamができたのでこちらを使いました。

ここでは生成までのログを参考までにそのまま掲載します。ログを見ると内部でVivadoが使われているのがわかります。

```
$ cd $RETROBASE/rtl/sys_gen/w11a/arty_bram/$ make　：Loading route data...Processing options...Creating bitmap...Creating bitstream...Writing bitstream ./sys_w11a_br_arty.bit...INFO: [Vivado 12-1842] Bitgen Completed Successfully.INFO: [Project 1-120] WebTalk data collection is mandatory when using a WebPACK part without a full Vivado license. To see the specific WebTalk data collected for your design, open the usage_statistics_webtalk.html or usage_statistics_webtalk.xml file in the implementation directory.INFO: [Common 17-186] '/home/ocha/oc_w11/trunk/rtl/sys_gen/w11a/arty_bram/project_mflow/project_mflow.runs/impl_1/usage_statistics_webtalk.xml' has been successfully sent to Xilinx on Sat Jun  4 15:45:44 2016. For additional details about this file, please refer to the WebTalk help file at /opt/Xilinx/Vivado/2016.1/doc/webtalk_introduction.html.INFO: [Common 17-83] Releasing license: Implementationwrite_bitstream: Time (s): cpu = 00:00:29 ; elapsed = 00:00:40 . Memory (MB): peak = 1643.305 ; gain = 452.859 ; free physical = 89 ; free virtual = 832INFO: [Vivado_Tcl 4-395] Unable to parse hwdef file sys_w11a_br_arty.hwdefINFO: [Common 17-206] Exiting Vivado at Sat Jun  4 15:45:46 2016...[Sat Jun  4 15:45:48 2016] impl_1 finishedwait_on_run: Time (s): cpu = 00:00:00.14 ; elapsed = 00:01:04 . Memory (MB): peak = 1626.848 ; gain = 0.000 ; free physical = 72 ; free virtual = 833Message control rules currently in effect are:Rule Name  Rule  Current Message Count  INFO: [Common 17-206] Exiting Vivado at Sat Jun  4 15:45:50 2016...$ lsMakefile                       sys_w11a_br_arty_pla_util.rptpdp11_hio70_arty.vbom          sys_w11a_br_arty_rou.dcppdp11_hio70_arty.vhd           sys_w11a_br_arty_rou_drc.rptproject_mflow                  sys_w11a_br_arty_rou_ds.rptsys_conf.vhd                   sys_w11a_br_arty_rou_pwr.rptsys_w11a_br_arty.bit           sys_w11a_br_arty_rou_sta.rptsys_w11a_br_arty.dep_vsyn      sys_w11a_br_arty_rou_tim.rptsys_w11a_br_arty.vbom          sys_w11a_br_arty_rou_util.rptsys_w11a_br_arty.vhd           sys_w11a_br_arty_rou_util_h.rptsys_w11a_br_arty_bit.log       sys_w11a_br_arty_syn.dcpsys_w11a_br_arty_imp.log       sys_w11a_br_arty_syn.logsys_w11a_br_arty_opt.dcp       sys_w11a_br_arty_syn_util.rptsys_w11a_br_arty_opt_drc.rpt   tbsys_w11a_br_arty_pla.dcp       vivado.jousys_w11a_br_arty_pla_cset.rpt  vivado.logsys_w11a_br_arty_pla_io.rpt$ ls -l *.bit-rw-rw-r-- 1 ocha ocha 2192125  6月  4 15:45 sys_w11a_br_arty.bit
```

この.bitファイルがFPGAのコンフィグレーションに使われるファイルです。

<!--more-->

## FPGAにbitstreamを書き込む

先ほど作成したbitstreamをFPGAに書き込みます。こちらもmakeするだけです。実行時のログをそのまま掲載します。

```
$ ls -l *.bit-rw-rw-r-- 1 ocha ocha 2192125  6月  4 15:45 sys_w11a_br_arty.bit$ make sys_w11a_br_arty.vconfigxtwv vivado -mode batch \        -source /home/ocha/oc_w11/trunk/rtl/make_viv/viv_init.tcl \        -source /home/ocha/oc_w11/trunk/rtl/bplib/arty/arty_setup.tcl \        -source /home/ocha/oc_w11/trunk/rtl/make_viv/viv_default_config.tcl \        -tclargs sys_w11a_br_artyXILINX_VIVADO already defined****** Vivado v2016.1 (64-bit)  **** SW Build 1538259 on Fri Apr  8 15:45:23 MDT 2016  **** IP Build 1537824 on Fri Apr  8 04:28:57 MDT 2016    ** Copyright 1986-2016 Xilinx, Inc. All Rights Reserved.source /home/ocha/oc_w11/trunk/rtl/make_viv/viv_init.tcl# source -notrace "$::env(RETROBASE)/rtl/make_viv/viv_tools_build.tcl"# source -notrace "$::env(RETROBASE)/rtl/make_viv/viv_tools_config.tcl"# source -notrace "$::env(RETROBASE)/rtl/make_viv/viv_tools_model.tcl"source /home/ocha/oc_w11/trunk/rtl/bplib/arty/arty_setup.tcl# set rvtb_part  "xc7a35ticsg324-1l"# set rvtb_board "arty"source /home/ocha/oc_w11/trunk/rtl/make_viv/viv_default_config.tcl# rvtb_default_config [lindex $::argv 0]WARNING: [Board 49-26] cannot add Board Part digilentinc.com:arty-z20:part0:1.0 available at /opt/Xilinx/Vivado/2016.1/data/boards/board_files/arty-z20/A.0/board.xml as part xc7z020clg400-1 specified in board_part file is either invalid or not availableWARNING: [Board 49-26] cannot add Board Part digilentinc.com:genesys2:part0:1.1 available at /opt/Xilinx/Vivado/2016.1/data/boards/board_files/genesys2/H/board.xml as part xc7k325tffg900-2 specified in board_part file is either invalid or not availableWARNING: [Board 49-26] cannot add Board Part digilentinc.com:zybo:part0:1.0 available at /opt/Xilinx/Vivado/2016.1/data/boards/board_files/zybo/B.3/board.xml as part xc7z010clg400-1 specified in board_part file is either invalid or not availableINFO: [Labtools 27-2285] Connecting to hw_server url TCP:localhost:3121WARNING: [Labtoolstcl 44-132] No matching hw_servers were found.INFO: [Labtoolstcl 44-466] Opening hw_target localhost:3121/xilinx_tcf/Digilent/210319789028AINFO: [Labtools 27-3164] End of startup status: HIGHINFO: [Common 17-206] Exiting Vivado at Sat Jun  4 21:15:57 2016...$ 
```

これでARTY FPGAボードがPDP-11になったはずです・・・。（たぶん）

いよいよ[UNIX V5を動かして](https://kanpapa.com/2016/06/pdp-11-arty-fpga-4-unix-v5.html "UNIX v5を動かす")みます。
