---
title: Apple1レプリカのreplica1 TEを組み立ててみる（３）
date: 2018-06-16
slug: replica1-te-3
categories:
- retrocomputing
tags:
- apple1
- '6502'
image: images/replica1_te_36.jpg
---

replica1 TE kitのパーツの確認も終わったので、まずは背の低いパーツである抵抗からはんだ付けしていきます。

![](images/replica1_te_31.jpg)

ICソケット、電源周り、コネクタ類をはんだ付けします。だんだんコンピュータらしくなってきました。

![](images/replica1_te_32.jpg)

  

欠品の電源スイッチのところはリード線でショートしておきます。

![replica1_te_33.jpg](images/replica1_te_33.jpg)

この状態でICは取り付けずに電源をいれてみます。

電源は7V～9Vとありましたので、手持ちの9V DCアダプタを使ってみました。LEDが点灯し電源も5Vがでています。

![replica1_te_34.jpg](images/replica1_te_34.jpg)

ここまで動いたのでいったん電源を切り、ICを取り付けていきます。

ここでICピンそろった君の出番です。ICソケットに挿しやすいようにピンをそろえておきましょう。

![](images/replica1_te_35.jpg)

マニュアル通りに最初はビデオ周りのIC（Parallax Propeller P8X32A-D40と24LC256 EEPROM）だけ載せてビデオ出力の確認を行います。

![replica1_te_36.jpg](images/replica1_te_36.jpg)

ビデオ出力をテレビに接続して電源を入れたところ、見事に@が表示されました。

![](images/replica1_te_37.jpg)

これで6821にシリアル接続され、ビデオ出力とキーボード入力のコントロールを行うPropellerチップは問題なく動作しているようです。

次はすべてのICを取り付けての動作確認に入ります。
