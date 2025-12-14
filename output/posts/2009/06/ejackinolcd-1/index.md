---
title: "eJackinoでLCD表示温度計をつくる"
date: 2009-06-06
categories: 
  - "electronics"
tags: 
  - "arduino"
  - "ejackino"
  - "lcd"
  - "lm73"
coverImage: "eJackino_lm73.jpg"
---

eJackinoからLCDに表示ができるようになったので、何か表示させるものはないかなとジャンク箱を探していたら、エレキジャックの付録基板でLM73という温度センサーが目に留まりました。  
arduinoにLM73を接続している人はいないかなぁと検索したところ、以下の記事がみつかりました。

- [初心者の電子の館 - Arduinoでエレキジャック付録のLM73を使う](http://fromgoldenwells.blog.so-net.ne.jp/2008-12-30)

なんと、このかたもeJackino基板が当選したようです。ちょっとびっくり。  
早速参考にして、ソースを一部書き換えて、LCDに温度をリアルタイムに表示するようにしてみました。

![](images/eJackino_lm73.jpg)

見事にLCD表示の温度計のできあがりです。LCD表示できるようになってから数時間後のことです。  
本当にお手軽にいろんな実験ができますね。
