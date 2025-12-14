---
title: "メカナムロボットが障害物を回避するようになりました。（おおたfab 第37回 素人でもロボットをつくりたい）"
date: 2021-02-11
slug: "mecanum-wheel-robot-lesson2-fixed"
categories: 
  - "robot"
tags: 
  - "arduino"
  - "otafab"
  - "メカナムホイール"
  - "otafab-robot"
image: "images/mecanum_lesson2_fix1.jpg"
---

[おおたfab](https://ot-fb.com/ "おおたfab")さんのセミナー「素人でもロボットをつくりたい」では、[OSOYOOさんのメカナムロボット](https://osoyoo.com/2019/11/08/omni-direction-mecanum-wheel-robotic-kit-v1/ "Metal Chassis Mecanum Wheel Robotic (for Arduino Mega2560) ")を素材にして実験をしています。

![mecanum_lesson2_fix1.jpg](images/mecanum_lesson2_fix1.jpg) <!--more--> [前々回(第35回)のセミナー](https://kanpapa.com/2020/12/mecanum-wheel-robot-lesson2-1.html "メカナムロボットに超音波センサーを取り付けました（おおたFab 第35回 素人でもロボットをつくりたい）")でLesson2として障害物をよけて動くロボットを試したのですが、うまく動きませんでした。本来であればセンサーがあるとよける動きをすべきですが、なぜか後ろ向きに進み、障害物がセンサーに近づくと逆に寄ってくる挙動をします。

この回は時間切れのためトラブルシューティングは次回ということになりました。

今回は新しく２名の参加者も加わったことで、これまでのいきさつを説明すべきでしたが、途中から参加するかた向けの資料やセミナー中の情報共有の方法を考えていなかったので、かなりぐだぐだになってしまいました。ごめんなさい。次回からはあらかじめ参加者にGitHubのURLを送って事前に見ていただこうと思います。

最初に[GutHub](https://github.com/docofab/mechanumWheelRobot "mechanumWheelRobot")にまとめた内容をざっと説明し、その中のArduinoのソースコードを確認しました。

Lesson2がうまく動かないということは、実は前回のLesson1も正しく動いていないのではという疑いがあります。Lesson1のソースコードから読み取れた動きが実際のロボットの動きとあっているか確認しました。

本来は以下の動きをするはずです。

1. 前進
2. 後退
3. 左折
4. 右折
5. 右平行シフト
6. 左平行シフト
7. 左下斜め
8. 右上斜め上
9. 左上斜め上
10. 右下斜め

実際に動かしたところLesson1の動きもおかしいです。明らかに前後の動きが逆になっています。Arduinoのソースを修正して前後に動く関数の内容を変更してみましたが、他の動きが正しくありません。全体的に修正が必要のようです。

しかし、公開されているソフトウェアに不具合があるとは考えにくいです。商品なのですから不具合があればすでに修正されているでしょう。

ハードウェアの配線ミスの可能性が高いので、何度も配線を確認しましたが問題ありませんでした。

そのときマニュアルに次の一文が赤字で書かれていることに気づきました。

**Note: If you mecanum wheel car doesn't move as per the above sequence, rather than the following sequence, you need to download the other series code again, in order to make sure that the car in next lesson work normally.**

- **Backward/Forward;**
- **Right turn/Left turn;**
- **Left Parallel Shift/Right Parallel Shift;**
- **Up Right Diagonal/Down Left Diagonal;**
- **Down Right Diagonal/Up Left Diagonal;**

**You need to download the following file and unzip the download zip file lesson.zip.**

その下に、metal-2560-lesson1-reverse.zipというプログラムがありました。このプログラムをArduinoにアップロードしたところ、動作が正しくなりました。

結局マニュアルをよく読んでいなかったのが原因だったのです。

これまで使っていたmetal-2560-lesson1.zipと今回使ったmetal-2560-lesson1-reverse.zipのソースを比較してみたところ、モーターに与える電圧の極性がすべて反転していました。何らかの理由で製品に使用しているパーツに変更があったのかもしれません。

Lesson1の動作確認が終わったところで、Lesson2のreverse版のプログラムをアップロードしたところ、何事もなかったように障害物を回避する動きをするようになりました。

これで安心してLesson3に進めます。次回はライントレーサの予定です。
