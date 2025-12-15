---
title: "NXP DIP ARMでLED点滅ができました"
date: 2012-09-05
slug: "nxp-dip-arm-led-blink"
categories: 
  - "electronics"
image: "images/dip_arm_lpclink.jpg"
---

秋月電子などで販売を開始したDIPのARM [LPCマイコン LPC1114FN28](http://akizukidenshi.com/catalog/g/gI-06071/)を使ってLチカを行ってみました。

お手軽にブレッドボードが使えるのが良いですね。しかもお安いですし。32bit CPUなのに・・・。

私の場合は秋月電子の通販で購入したのですが、パッケージに同封されている1枚の紙に役立つ情報が書かれていたので、これを参考にして実験しました。この紙は秋月電子の販売ページにもLPC1114FN28説明書としてPDFで公開されています。

**1\. 開発環境の準備**

開発環境のLPCXpressoをダウンロードしました。最新のものはMac版もあるようなので、Mac版をダウンロードしました。説明書にあるようにアクティベーションをしました。（何度目だろう・・・）

**2\. LPC-Linkの準備**

手持ちのLPCXpresso LPC1768の出番です。先ほどの説明書にもありますが、私の場合は、LPC-Link側とターゲットCPUをつないでいるパターンはすでにカッターで切断済みで、ピンヘッダをつけています。普通に使うときはジャンパーピンで全ピンを接続し、今回のようなときはジャンパーピンを外して必要な信号線を取り出しています。

**3\. LEDの接続**

ブレッドボードにLPC1114FN28を取り付けて、LPCXpresso LPC1114と同じように、PIO0\_7 (28番ピン）に330Ωの抵抗を入れてLEDを接続し、GNDにつなぎました。

**4\. LPC-Linkとの接続**

LPC-LinkとLPC1114FN28の接続は説明書とおりにジャンパー線で結線すればOKです。

![dip_arm_lpclink.jpg](images/dip_arm_lpclink.jpg)

**5\. LPCXpressoでサンプルコードをコンパイル**

LPCXpressoをインストールすると、インストールされたディレクトリの中にサンプルプログラムが入っています。

Mac版の場合ですと、

/Applications/lpcxpresso\_4.2.4\_267/lpcxpresso/Examples/NXP/

LPC1000/LPC11xx/LPCXpresso1114\_cmsis2.zip

になります。

LPCXpressoを立ち上げて、左下のQuickstartのメニューにあるImport and ExportのImport archived projects (zip)で上記のZIPファイルを取り込みます。取り込みが完了するといくつかのプロジェクトができますが、LチカはLPCX1114\_cmsis2\_systickが該当します。

説明書の裏面にあるLPCXpressoでデバックするときのTipsに従って、ターゲットマイコンをLPC1114FN/102にして、ClockソースをIRCにします。説明書に書かれているsystem\_LPC11xx.cはCMSISv2p00\_LPC11xxのプロジェクトのsrcにありますので、このファイルを修正します。

修正後にLPCX1114\_cmsis2\_systickのプロジェクトをビルドするとバイナリができあがります。

**6\. LPC-Linkデバッカで動かす。**

ビルドができたら、左下のQuickstartのメニューにあるDebug and RunのDebug 'LPC1114\_cmsis\_systick' \[debug\]をクリックすると、LPC-Link経由でプログラムがマイコンに書き込まれます。あとはRunメニューでステップ実行をするもよし、動かしてみてください。

動作中の画像はこちらです。ゆっくり点滅していますが、systick.cを修正して点滅速度を変えることもできます。

LPC-LinkとLPCXpressoという強力な開発環境がありますので、今後様々な活用事例がでてくると思います。

12月のMakeが楽しみですね。
