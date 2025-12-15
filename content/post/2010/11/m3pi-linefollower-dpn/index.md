---
title: "m3piでライントレーサを動かしてみました"
date: 2010-11-23
slug: "m3pi-linefollower-dpn"
categories: 
  - "electronics"
---

前回はセンサーなどを使っていないただ走るだけのプログラムを試しましたが、今回はライントレーサのプログラムを書き込んでみました。  
[mbed.org](http://mbed.org/)に公開されている[m3pi](http://mbed.org/cookbook/m3pi)のプログラムはたくさんあるのですが、darron nielsenさんのNoteBook [ARM Techcon / mbed Robot Racing](http://mbed.org/users/microsat/notebook/arm-techcon--mbed-robot-racing-/)のページに掲載されている[m3pi\_LineFollower\_dpn](http://mbed.org/users/microsat/programs/m3pi_LineFollower_dpn/lhpdou)を試しました。  
これが速いのなんのって、高速で線の上を駆け回ります。少し誤検知しておもしろい動きをするときもありましたが、問題なく走り回ります。  
その様子をYouTubeにアップしておきました。（ちょっとiMovieで編集してます。）

https://youtu.be/ScNM92hNAi8?si=G4wjNrMEowiiewVD

m3pi\_LineFollower\_dpnのプログラムはそんなに長いものではありませんが、高速に走れるように工夫されているようです。  
私が持っているMINDSTORMS NXTのコースがスムーズに走れるように少し調整してみたいと思います。
