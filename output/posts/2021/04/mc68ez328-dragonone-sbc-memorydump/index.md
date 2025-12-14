---
title: "MC68EZ328 DragonOne SBCでメモリダンプができました"
date: 2021-04-21
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
coverImage: "dragonone_mdump_python2.png"
---

前回[たった8バイトのCPU内蔵の実行用メモリ(IBUFF)でメモリの１バイトの情報をシリアルデータとして取り出す](https://kanpapa.com/2021/04/mc68ez328-dragonone-sbc-solder-parts.html "MC68EZ328 DragonOne SBCでブートローダーが動きました")ことができました。この仕組みを何度も繰り返すようにプログラミングすることで、メモリダンプもできるはずです。

### Pythonでメモリダンプ

試行錯誤をしながら、Python3でメモリダンププログラムを書いてみました。Pythonは初心者なのですが、Pyserialがあるのでシリアル通信が簡単に扱えるだろうと考えました。ソースプログラムは整理してからGitHubにあげようと思います。

実行結果は以下のようになりました。ブートローダーのマイクロコードのアドレス付近にはプログラムが書かれていて、いろんな値が見えるだろうとダンプしてみました。

![dragonone_mdump_python1.png](images/dragonone_mdump_python1.png) <!--more-->

フラッシュメモリが接続されているはずの$00000000のあたりをダンプしてみると、$FFが並んでいましたが、$00も見えました。念のため続けて２度実行しましたが同じ値が取れています。

![dragonone_mdump_python2.png](images/dragonone_mdump_python2.png)

しかし、本当にメモリの内容が正しく表示できているのか今一つ自信がありません。

### 連続したNOP命令を発見

もう少し広い範囲をダンプしてみたところ、次のような連続したデータがありました。

![dragonone_mdump_python3.png](images/dragonone_mdump_python3.png)

4E 71は68000 CPUにおけるNOP (No Operation) 命令です。このような意味のあるデータが確認できたので正常にメモリの内容を読み出せていることが確認できました。

### これで道具が揃いました

このダンププログラムでメモリの確認ができるようになりました。メモリの書き込みや実行はBレコードをブートローダーに読み込ませればよいので、最低限の道具はそろったことになります。

フラッシュメモリへの書き込みは手順があるようなので、DragonOneのページをみながら書き込みプログラムをアセンブラで作ってみようと思います。
