---
title: "Pololu 3pi robotにプログラムを書き込んでみた"
date: 2010-11-19
slug: "pololu-3pi-programming"
categories: 
  - "robot"
---

Pololu 3pi robotのマイコンにサンプルプログラムを書き込んでみました。  
材料は以下の通りです。

- AVR Studio 4
- WinAVR
- libpololu-avr
- AVRISP mkII (ISP)

作業環境は愛機MacBook Proで、Parallels Desktop上でのWindows XPです。  
まずはいつものLEDチカチカ。ここまではArduinoとかmbedとかと同じ感じ。  
結構高速点滅ですね。

{{< youtube HYWOCk8CQRM >}}

次にライントレーサのサンプルプログラムを書き込んでみました。

{{< youtube sfId4bowoRA >}}

コースはLEGO MINDSTORMS NXTについていたものですが、STARTの文字の周りも正確に曲がっているのはすごいです。じっくりサンプルプログラムのソースを読んでみたいと思います。
