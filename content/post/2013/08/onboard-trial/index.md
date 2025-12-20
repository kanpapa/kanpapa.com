---
title: "OnBoardを試用してみました"
date: 2013-08-11
slug: "onboard-trial"
categories: 
  - "electronics"
image: "images/onboard_3.jpg"
---

先日到着したDENSIKIT.COMさんのArduino互換の[OnBoard](http://arduino.densikit.com/home/onboard "OnBoard")を組み立てました。  
ほとんどのパーツは手元にあったのですが、長い細ピンヘッダが無かったのでそれだけ新規に購入しました。  
組み立て中の様子はこんな感じ。いつもながらゴチャゴチャしています。

![](images/onboard_0.jpg)

  
組み立ては特に問題なく、すべてのコネクタやピンソケットを取り付けました。シルク印刷も見やすく部品数も少ないためスムーズに進みました。  
6ピンヘッダにスイッチサイエンスの[FTDI BASIC](http://www.switch-science.com/catalog/1032/ "FTDI USBシリアル変換アダプター(5V/3.3V切り替え機能付き)")を取り付け、PCのUSBコネクタに接続したところ、LEDが点滅をはじめました。OnBoardは問題なく動作しているようです。

完成したOnBoardはこんな感じです。標準的な[小型ブレッドボード](http://akizukidenshi.com/catalog/g/gP-00315/ "ブレッドボード EIC-801")の横幅にピッタリ合います。

![](images/onboard_1.jpg)

せっかくですので何か作ってみようとパーツを探したところ、秋月電子で購入した[RGB LEDアレイ](http://akizukidenshi.com/catalog/g/gI-04761/ "高輝度10ポイントRGBLEDアレイOSX10201-LRPB2 フルカラー")と[I2C接続小型LCDユニット](http://akizukidenshi.com/catalog/g/gK-06795/ "I2C接続小型LCDモジュールピッチ変換キット")を接続することにしました。  
RGB LEDアレイはカソードコモンになっているので、接続するためにはOnBoardの端子とLED端子の間に電流制限用の抵抗を接続しなければなりません。このため先ほどの標準的なブレッドボードだけでは実装が難しいため、今回は少し[横長のブレッドボード](http://akizukidenshi.com/catalog/g/gP-00314/ "ブレッドボード EIC-701")を使用しました。

今回はD0〜D9から1KΩの抵抗をはさんで、RGB LEDアレイの11番端子から20番端子に接続し、D10をREDのカソード、D11をBLUEのカソード、D12をGREENのカソードに接続することで、RED/BLUE/GREENを順番に切り替えるようにしました。

LCDモジュールはI2C接続なので、OnBoardのSDA,SCL端子に接続すれば良いのですが、残念ながらパターンが接続されていないという報告が他のテスターのかたからありましたので、A4(SDA)、A5(SCL)に接続しました。LCDモジュールの電源はOnBoardの端子から容易に取り出せます。  
なお、このLCDモジュールは3.3Vなので、FTDI BASICで電源電圧を3.3Vに設定して動作させています。FTDI BASICで5V/3.3Vを切り替えられるのもプロトタイピングには便利な点だと思います。  
このLCDには表示している色を表示するようにしました。

RGB LEDアレイとI2C LCDを接続したOnBoardは写真のようにシンプルになりました。単色のLEDアレイであればLEDが並んでいるだけなので、横長のブレッドボードを使わなくても奇麗に収まるでしょう。I2C LCDの接続は非常にシンプルです。

![](images/onboard_3.jpg)

  
![](images/onboard_3.jpg)実際に動作している様子をYouTubeにアップしておきました。

{{< youtube wZnHkZZ6bHs >}}

正式版のOnBoardが楽しみです。今回OnBoardのテスターにご招待いただいた@will2ttさんに感謝いたします。
