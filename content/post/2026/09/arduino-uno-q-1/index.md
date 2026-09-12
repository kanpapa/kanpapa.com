---
title: "Arduino Uno Qを触ってみました"
date: 2026-09-12T07:26:03+09:00
slug: 'arduino-uno-q-1'
tags:
  - 'Arduino'
  - 'UnoQ'
  - '電子工作'
  - 'AI'
categories:
  - 'Electronics'
image: 'arduino-uno-q-front.jpg'
---
## はじめに

前々から気になっていた[Arduino Uno Q](https://ssci.to/10800)ですが、今度最大40 TOPSの推論性能を持つ[Arduino VENTUNO Q](https://ssci.to/11359)というものが発売されるようで、そろそろArduino Uno Qも触っておいたほうがいいかなとArduino Uno Q 4GBを購入してみました。  
Arduino Uno QはLinuxが動くSoCとSTM32マイコンが連携しながら動かせるもので、NPUも搭載しある程度のLLMも動かせそうです。今後はこのようなマイコン（リアルタイム制御）＋小型Linux SBC（エッジAI/ネットワーク）の組み合わせが主流になるものと思われます。

![購入したArduino Uno Q 4GB](arduino-uno-q-box.jpg)

## 外観

おなじみのArduinoフォームファクタですので小さく感じます。

![Arduino Uno Q](arduino-uno-q-front.jpg)

表面はこれまでのArduinoと見た目は変わりませんが、裏面をみると2つのコネクタがあります。ピン数が多くここから様々な機能拡張ができそうです。

![Arduino Uno Qの裏面](arduino-uno-q-back.jpg)

## 電源投入

Arduino Uno QにはUSB-Cコネクタがありますので、ここからPCに接続して電源を供給します。
電源を投入するとマトリクスLEDにArduinoのロゴがアニメーションで表示され、その後ハートのマークになりました。

{{< youtube i234J-Oknwo >}}

この動画の右上にある4個のRGB LEDがQRB SoCやSTMマイコンの動作状態を示しているようです。

## Arduino App Lab 

Arduino Uno Qの標準の開発環境である[Arduino App Lab](https://docs.arduino.cc/software/app-lab/)をインストールしました。起動すると対応ボードの接続を要求されます。

![対応ボードの接続要求画面](arduino-app-lab-no-boards-found.png)

この状態でArduino Uno QをUSBに接続すると自動認識されますので、ボードに名前を付けます。ここではkanpapaとしました。

![ボードに名前を設定](arduino-uno-q-name.png)

次にWiFiに接続するように案内され、接続すると自動的にソフトウェアアップデートが動きます。

![ARDUINO UNO Q Software Updateの画面](arduino-app-lab-software-update.png)

アップデートが終わるとArduino App Labの初期画面が表示されました。サンプルプログラムはinspirationsにあるようなので眺めてみます。

![Inspirationsの画面](arduino-app-lab-inspirations.png)

この中ですぐ試せそうなEdge AI Assistantを実行してみました。UIはブラウザになります。

![Edge AI Assistantの実行例](edge-ai-assistant.png)

それなりに回答できているようですが、よく見るとUno Qではなく一般的なUnoの情報が表示されているように見えます。これはエッジAIのローカルLLMなのでやむを得ないでしょう。

## Arduino IDE 2.0

MCUだけ使うプログラムであればArduino IDE 2.0も使用できます。サンプルのBlink.inoを動かしたところ、ボード上のRGB LED 3が赤く点滅をはじめました。

![Arduino IDE 2.0でBlinkを書き込む](arduino-uno-q-ide.png)

もちろん、こうしたLチカ程度の単体動作だけであれば従来のArduino Unoで事足りますが、従来の開発環境もそのまま使えるのは安心感があります。

## まとめ

Arduino App Labは非常にパワフルで直感的な可能性を感じる一方、これまでのArduino IDEとは全く異なるものですので、公式ドキュメントを読みながら手探りで試している段階です。今後、日本語を含むローカライズにも期待したいところです。    
最近、[Arduino Uno Q メディアキャリアボード](https://ssci.to/11135)というものが発売されたようです。これを使えばカメラやディスプレイ、オーディオなどが直接接続できるので、次はメディアキャリアボードを取り付けてAIによる画像認識や音声認識やQualcomm SoCとSTM32間の通信連携などを試してみます。
