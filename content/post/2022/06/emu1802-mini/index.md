---
title: EMU1802-mini の回路を修正しました
date: 2022-06-23
slug: emu1802-mini
categories:
- cosmac
- retrocomputing
tags:
- emu1802
image: images/emu1802-mini-added-diode_pcb_back.jpg
---

EMU1802-miniで実験していると、USBシリアルをつないだだけでPOWER LEDが点灯してしまいます。このため逆流防止のためダイオード 1N4148を追加しました。

回路図では以下のような修正となります。

![emu1802-mini-added-diode.png](images/emu1802-mini-added-diode.png)

<!--more-->

Rev0.1の基板では以下のように修正してください。表面で一か所パターンカット、裏面にダイオードを実装します。比較的簡単に修正できます。

表面

![emu1802-mini-added-diode_pcb_front.jpg](images/emu1802-mini-added-diode_pcb_front.jpg)

裏面

![emu1802-mini-added-diode_pcb_back.jpg](images/emu1802-mini-added-diode_pcb_back.jpg)

回路図は後ほど修正しておきます。基板はもし改版する機会があれば修正します。
