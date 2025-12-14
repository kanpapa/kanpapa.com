---
title: "MC68EZ328 DragonOne SBCの基版をKiCadで設計中です。"
date: 2021-03-14
slug: "mc68ez328-dragonone-sbc-kicad"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/DragonOne_rev00_kicad.jpg"
---

ブログをリニューアルしたせいかよく質問が届きます。

すこし前に[MC68EZ328の記事](https://www5.kanpapa.com/tag/mc68ez328 "MC68EZ328の記事")を見たかたから、BBUG.EXEの入手先について聞かれました。[NXPのサイト](https://www.nxp.com/search?keyword=MC68EZ328 "Search | NXP")にあったはずなので、調べてみたところ見つからず、いつの間にか無くなっていました。

すでにEOLになっているのでやむを得ないのですが、MC68EZ328は何個か購入しているので、資料が無くなる前にいろいろ試してみようと考えました。

![dragonball_mc68ez328_cpu.jpg](images/dragonball_mc68ez328_cpu.jpg) <!--more-->

中でも気になっていたのは[DragonOne](http://www.mediumware.net/DragonOne/DragonOne.htm "DragonOne")というマイコンボードの記事で、[μClinux](https://ja.wikipedia.org/wiki/%CE%9CClinux "μClinux")をMC68EZ328で動かしているものです。こちらのページもリンク先がことごとく無くなっていて、InternetArchiveでも見つからないものも多数です。

- [http://www.mediumware.net/DragonOne/DragonOne.htm](http://www.mediumware.net/DragonOne/DragonOne.htm "DragonOne")

というわけで、情報が無くなる前にこのDragonOneを作ってみることにしました。ガーバーデータは掲載されているのですが、ガーバービューワーで正常に表示されないので、勉強がてらこのサイトにある回路図とPCBパターンの画像からKiCadで基板を起こしてみることにしました。ただし、サイトにある回路図とPCBパターンは一致してないようで、PCBパターンを優先して回路図を起こしています。

一応ある程度形になったものがこちらです。CPUはMC68EZ328、Flash RAM 4Mx16bit、DRAM 4Mx16bit、RTCの構成です。

![DragonOne_rev00_kicad.jpg](images/DragonOne_rev00_kicad.jpg)

まだ電源周りの配線が未整理だったり未確認な箇所も残っていることもあり、AliExpressでオーダーしたパーツと基板パターンを突き合わせたのちに基板を発注するつもりです。初めての本格的な表面実装なので慎重にすすめていきます。
