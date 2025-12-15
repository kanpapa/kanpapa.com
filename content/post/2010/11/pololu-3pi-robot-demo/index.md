---
title: "Pololu 3pi robotのデモプログラムを動かしてみる"
date: 2010-11-17
slug: "pololu-3pi-robot-demo"
categories: 
  - "robot"
---

Pololu 3pi robotに電池をいれてみました。単４電池４本です。  
LCD基板を外してから電池をセットします。  
モーターを回すので単四だとあまり電池が持たないかもしれません。今度eneloopの単４を買いこんでこようと思います。  
購入した時点でマイコンにデモプログラムが書き込まれているそうで、すぐ動作確認ができるようです。  
その様子はこんな感じ。(iPhone4で縦撮影したので画面が小さくてすみません。）

https://youtu.be/XWZ0ZlFlbLg?si=BMXd3ZACAXmCyAKj

Timer, Battery, LEDs, Sensors, Motors, Music.....などなど、デモプログラムだけで細かい操作ができます。  
光センサーを５つ搭載しているので、本体を傾けることで光量が変化するとグラフが変化します。  
モーターはスイッチを押しっぱなしにすると回転数があがっていきます。  
一通りの機能は問題無いようです。  
次はプログラミング環境の準備ですね。手持ちのAVR StudioとAVRISP mkIIで書き込んでみたいと思います。  
今日は遅いのでこのへんで。
