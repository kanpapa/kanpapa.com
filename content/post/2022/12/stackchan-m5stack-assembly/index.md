---
title: "スタックチャンを組み立てました"
date: 2022-12-13
slug: "stackchan-m5stack-assembly"
categories: 
  - "electronics"
  - "m5stack"
tags: 
  - "m5stack"
  - "stack-chan"
image: "images/stackchan_complete.jpg"
---

前々から気になっていた@meganetaaanさんの[スタックチャン](https://github.com/meganetaaan/stack-chan "スタックチャン")ですが、3Dプリンタも自宅に導入したので公開されているデータをもとに製作してみました。製作に必要なデータはGithubから入手しています。

- [meganetaaan/stack-chan: A JavaScript-driven M5Stack-embedded super-kawaii robot.](https://github.com/meganetaaan/stack-chan/ "meganetaaan/stack-chan: A JavaScript-driven M5Stack-embedded super-kawaii robot.")

### 3Dプリンタでのケース出力

GitHubのデータをスライサでGcodeに変換し、まずはShellからプリント開始です。

![stackchan_case_shell_1.jpg](images/stackchan_case_shell_1.jpg)

スライサのサポートの設定が良くなかったのかサポートが多くついてしまいました。慎重にサポートを取り外して何とか形にはなっています。

![stackchan_case_shell_2.jpg](images/stackchan_case_shell_2.jpg)

続いてモーターのケースです。これはまあまあの出来。

![stackchan_case_sg90_1.jpg](images/stackchan_case_sg90_1.jpg)

足の部分もプリントしました。これはきれいにできました。

![stackchan_case_feet_1.jpg](images/stackchan_case_feet_1.jpg)

残るバッテリーケースをプリントして、ケースのパーツが揃いました。

![stackchan_case_all.jpg](images/stackchan_case_all.jpg)

### ケースの仮組み

ケースにモーターを取り付けて仮組みをしてみました。今回は安価な[SG92](https://akizukidenshi.com/catalog/g/gM-08914/ "マイクロサーボ　ＳＧ９２Ｒ")を使っています。

![stackchan_case_sg92_1.jpg](images/stackchan_case_sg92_1.jpg)

![stackchan_case_sg92_2.jpg](images/stackchan_case_sg92_2.jpg)

モーターはぴったり収まりました。これに足の部分を取り付けます。

![](images/stackchan_case_temp_-assembly1.jpg)

さらにこれをシェルに取り付けます。

![](images/stackchan_case_temp_-assembly2.jpg)

スタックチャンの形になってきました。

### プリント基板の入手とはんだ付け

ケースができたところで次はM5Stackを取り付けるプリント基板の製作です。

nyaru labさんが[Boothで基板を配布](https://booth.pm/ja/items/4094998)されていたのでそちらを購入しました。コネクタもセットなのでありがたいです。この基板はv0.2.0で、現在の最新版v0.2.1の基板とは若干構成が違いますので、GitHubにあるv0.2.0用のドキュメントを参照しました。

![stackchan_pcb1.jpg](images/stackchan_pcb1.jpg)

基板に実装するパーツは秋月電子と千石電商で集めました。

![stackchan_pcb2.jpg](images/stackchan_pcb2.jpg)

ルーペで確認しながらハンダ付けしていきます。

![stackchan_pcb3.jpg](images/stackchan_pcb3.jpg)

完成した基板です。こちらはM5Stackを取り付ける側。

![stackchan_pcb4.jpg](images/stackchan_pcb4.jpg)

こちらはモーターとバッテリーを取り付ける側です。

![](images/stackchan_pcb5.jpg)

これを仮組みしているスタックチャンのケースに取り付けます。

### テストプログラムでの動作確認

M5Stackを製作した基板に取り付けてテストプログラムによる動作確認を行うため、モーターと基板を仮接続します。

![](images/stackchan_test1.jpg)

テストプログラムは@mongonta0716 さんのstack-chan-testerを使いました。

- [mongonta0716/stack-chan-tester: stack-chan test application for pwm servo](https://github.com/mongonta0716/stack-chan-tester "mongonta0716/stack-chan-tester")

すでにM5StackのArduino IDE環境を使っていましたので、すぐにプログラムを書き込むことができました。

モーターは問題なく動きました。モーターの回転位置はこのテストプログラムで合わせると調整が楽です。

ケースに仮組してみます。

USBケーブルで給電しているため、本体が固定されてしまい足だけが動いていますが、ハードウェアは問題なさそうです。

### 公式ファームウェアの書き込みと動作確認

最後に公式ファームウェアを書き込みます。Arduino IDEとかで書かれているのかと思っていたのですが、Moddable SDKをつかってJavaScriptで書かれていました。このあたりは初めて使うのでまずはソースを眺めてみました。

手順書通りに書き込んでみましたが、そのままではシリアルモーター用で、PWMモーターのSG90用になっていないようでしたので、ソースコードを追って一部修正して書き込んだら正常に動作しました。

公式ファームウェアでのテストの様子です。いったんケースは外しています。

問題なさそうなので、元通りケースに収めてスタックチャンの完成です。

![](images/stackchan_complete.jpg)

### まとめ

最初にプリントしたシェルケースがややガタガタでかっこ悪かったので、サポートの取り付けを見直してもう一度プリントしたものに交換し、見栄えが良くなりました。

![](images/stackchan_case_rev2.jpg)

Moddableは未経験でまだ構造があまり理解できていません。参考書は無いかなと探したところ[「実践Moddable JavaScriptではじめるIoTアプリケーション」](https://nextpublishing.jp/book/12230.html "実践Moddable JavaScriptではじめるIoTアプリケーション")という書籍がありましたので、これを見ながら理解していきたいと思います。そういえば昔、[Firefox OS](https://kanpapa.com/tag/firefox-os)というものもいじっていたのでそれに近いのかなとも思っています。

このような楽しいスタックチャンを開発、公開いただいた作者のみなさまに感謝です。
