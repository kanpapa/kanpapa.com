---
title: "MC68EZ328 uCsimmを動かしてみました(1) ～uClinuxを起動する～"
date: 2021-06-13
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
coverImage: "uCsimm_front.jpg"
---

以前ヤフオクで購入したあと行方不明になっていたuCsimmカードとuCgardenerベースカードが見つかりましたので動かしてみました。

### uCsimmカード

uCsimmカードは2000年頃にRt-Control, Inc.とLineo, Inc.が開発したMC68EZ328でuClinuxが動作する30-pin SIMMサイズのマイコンボードです。これに刺激をうけて、uCdimm、ez328simm、DragonOneが登場したと思われます。現在開発中のMC68EZ328 SBCでも参考にしています。

![uCsimm_front.jpg](images/uCsimm_front.jpg) ![uCsimm_back.jpg](images/uCsimm_back.jpg)

uCsimmカードのスペックは以下の通りです。

- MC68EZ328 CPU
- 8 MB RAM
- 2 MB Flash
- 10 Mbit Ethernet controller (CS8900)
- 30-pin SIMM module.

これらのチップに加えてRS232Cのレベル変換ICやLAN用パルストランスまでがSIMMモジュールに実装されています。これは組み込み前提で交換保守がしやすいようになっているのではと思われます。

<!--more-->

### ベースボードの修理

このuCsimmカードを使うためにはSIMMスロットがあるベースボードが必要になります。

![uCsimm_gardener.jpg](images/uCsimm_gardener.jpg)

電源はベースボードから供給するのですが、電源コネクタがセンターマイナスであることに気づかずにセンタープラスの電源を差してしまい、3.3Vのレギュレーターが故障したようです。VIN, GNDピン周辺のパッケージが膨らんでいて過大な電流が流れたように見えます。おかげでuCsimmカードは無事だったと思われます。

![TC55RP3302.jpg](images/TC55RP3302.jpg)

このため、レギュレーターとケミコンを取り外して、ユニバーサル基板の電源ラインから3.3Vの電源を直接供給するように改造しました。

### 電源投入

ベースボードのシリアルコネクタにRS232C-USB変換ケーブルを取り付け、LANケーブルを接続した状態で電源を投入します。

![uCsimm_running.jpg](images/uCsimm_running.jpg)

シリアルコンソールとなっているTeratermにメッセージが表示されました。uCsimmカードのCPUとシリアルポートは問題なく動作しているようです。

![uCbootstrap_startup.png](images/uCbootstrap_startup.png)

ブートローダーでgoと入力するとuClinuxが起動すると聞いていますので、その通りに操作しました。

![uCbootstrap_go1.png](images/uCbootstrap_go1.png)

ファームに書き込まれているuClinuxのバージョンは2.0.38.1pre5のようです。最初から書き込まれていたものかどうかはわかりません。

### uClinuxにログインしてみる

uClinuxの起動メッセージが続き、無事loginプロンプトが表示されました。初期アカウントはroot、初期パスワードはuClinuxと聞いていますので、そのように入力しました。

![uCsimm_uClinux_login.png](images/uCsimm_uClinux_login.png)

無事ログインできました。早速uCsimmのuClinuxを探検してみます。（[続く](https://kanpapa.com/2021/06/mc68ez328-ucsimm-2.html "MC68EZ328 uCsimmを動かしてみました(2) ～uClinuxを探検する～")）
