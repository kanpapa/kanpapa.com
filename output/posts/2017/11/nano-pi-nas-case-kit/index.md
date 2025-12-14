---
title: "Nano Pi NEO用NASケースキットを組み立ててみた"
date: 2017-11-18
categories: 
  - "electronics"
tags: 
  - "nano-pi-neo"
coverImage: "nanopi_nas10.jpg"
---

[秋月電子](http://akizukidenshi.com/ "秋月電子通商")さんで[Nano Pi NEO](http://akizukidenshi.com/catalog/g/gM-12301/ "Nano Pi NEO 512MB")用のNASケースの販売が始まったようです。

- [Nano Pi NEO/NEO2用NASケースキット (2,180円)](http://akizukidenshi.com/catalog/g/gM-12591/ "Nano Pi NEO/NEO2用NASケースキット")

Nano Pi NEOでどんなNASができるのか、試しに購入してみました。

到着したパッケージはこんな感じでした。思ったより大きいです。

![nanopi_nas1.jpg](images/nanopi_nas1.jpg) <!--more-->

パッケージを開けるとケースがでてきました。なかなかしっかりした作りのケースに見えます。

![nanopi_nas2.jpg](images/nanopi_nas2.jpg)

この中に基板と付属部品が格納されていましたので、とりだしてみました。

![nanopi_nas3.jpg](images/nanopi_nas3.jpg)

NAS基板に加えて、Nano Pi NEO用とNano Pi NEO2用のパネルが付属していて選べるようになっています。また、ヒートシンクも付属されています。

早速手持ちのNano Pi NEO 512MBにピンヘッダをはんだ付けして、ヒートシンクを取り付けます。

![nanopi_nas5.jpg](images/nanopi_nas5.jpg)

これを、NAS基板に取り付けます。ストレージは手持ちの64GB SSDをとりつけました。

![nanopi_nas6.jpg](images/nanopi_nas6.jpg)

次は、ファームウェアの準備です。[マニュアルページ](http://wiki.friendlyarm.com/wiki/index.php/1-bay_NAS_Dock_v1.2_for_NanoPi_NEO/NEO2 "1-bay NAS Dock v1.2 for NanoPi NEO/NEO2")にあるファームウェアと書き込みツールをダウンロードしてmicroSDカードに書き込みます。

![nanopi_nas_sdwrite.png](images/nanopi_nas_sdwrite.png)

書き込んだmicroSDカードをNano Pi NEOに取り付けて準備は完了です。

手持ちの12Vの電源アダプタを接続し、電源を投入してみます。

![nanopi_nas8.jpg](images/nanopi_nas8.jpg)

LEDが点灯し、LANコネクタのLEDがちかちか点灯しているので、無事動いているように見えます。

セットアップはWebブラウザから行うようですが、IPアドレスがわからなかったのでルーターで割り当てられたと思われるIPアドレスを探しました。ブラウザで接続するとログイン画面が表示されます。日本語が指定できるようなので、日本語を指定し、adminでログインしたところ無事設定画面が表示されました。それもきちんとした日本語でカッコいい画面です。

![nanopi_nas_setup.png](images/nanopi_nas_setup.png) [openmediavault](https://www.openmediavault.org/ "openmediavault")というOSSのNASソフトをdebian上で動かしているようです。少し触ってみましたが、NASとしての完成度は高いようです。

設定画面の中にsshという設定がありましたので、sshでログインしてみました。Nano Pi NEOのrootアカウントで試したところ、あっさりログインできてしまいました。

![nanopi_nas_ssh.png](images/nanopi_nas_ssh.png)

もちろんsshの設定でrootでログインできないようにもできます。

次にソフトウェアのアップデートを行ってみました。これもNASの設定画面から行えます。

![nanopi_nas_update.png](images/nanopi_nas_update.png)

まさにdebianのアップデートですね。

無事動作確認も行えましたのでケースに収納して完成です。

![nanopi_nas10.jpg](images/nanopi_nas10.jpg)

Nano Pi NEOの特徴は小型であり、機器に組み込みやすい大きさになっていることですが、このNASへの応用は良い事例だと思います。こんなに手軽に低価格なNASを作ることができるのは素晴らしいですね。また、大容量のストレージが接続できているので、カスタマイズすればちょっとしたサーバとしても使えるのではと思います。ぜひお試しください。
