---
title: "PDP-11 DCJ11 CPUでUNIX v6を動かしてみました"
date: 2024-08-03
categories: 
  - "pdp-11"
  - "retrocomputing"
tags: 
  - "dcj11"
  - "fpga"
  - "pdp-11"
  - "tang-nano"
  - "tangnanodcj11mem"
coverImage: "pdp-11-unix-v6-eyecatch1.jpg"
---

本記事はPDP-11の命令セットを持つ[DCJ11(Jaws)CPU](https://gunkies.org/wiki/J-11_chip_set)を動作させるためにRyo Mukaiさんが開発した[TangNanoDCJ11MEM](https://github.com/ryomuk/TangNanoDCJ11MEM)を使用しています。GitHubで公開されています。

## PDP-11 CPUでUnixを動かしたい

[PDP-11](https://ja.wikipedia.org/wiki/PDP-11)と言えば最初に[UNIX](https://ja.wikipedia.org/wiki/UNIX)というOSが動作したマシンです。[TangNanoDCJ11MEM](https://github.com/ryomuk/TangNanoDCJ11MEM)でPDP-11のCPUが動きだした状態ですので、何とかUNIXも動かせないものかとTangNanoDCJ11MEM開発者のRyo Mukaiさんも考えられたようで初期のバージョンである[UNIX v1](https://gunkies.org/wiki/UNIX_First_Edition)を動かせる環境を作成しています。

https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/unix-v1

UNIX v1の動作環境やセットアップ方法については上記のGitHubで公開されており安定して動作しているのでそちらを見ていただくこととし、ここではUNIX v6を動かすことにチャレンジしてみました。

## UNIX v6とは

[UNIX v6](https://ja.wikipedia.org/wiki/Version_6_Unix)は一般に公開された最初のUNIXであり、ソースコードも提供されたため大学などで研究目的で利用されました。ソースコードは約9000行であり、全体を見渡すことができる規模のものです。またUNIX v6のソースコードを解説した書籍が今でも発売されています。

- [Commentary on the Sixth Edition UNIX Operating System by John Lions](http://www.lemis.com/grog/Documentation/Lions/)　PDFで公開中
- Lions' Commentary on UNIX 日本語版(アスキー)　現在は絶版
- [はじめてのOSコードリーディング――UNIX V6で学ぶカーネルのしくみ](https://gihyo.jp/book/2013/978-4-7741-5464-0)　現在も発売中

私はUNIX v6の名前は知っていましたが、実際に動かしたことはないので、この機会に本物のPDP-11のCPUで動かしてみたいと考えました。なお、上記の2冊の日本語版の書籍はこの機会に入手しておきました。

## シミュレーション環境でのUnix v6の起動

PDP-11でのUNIX v6は歴史的なコンピュータのシミュレーション環境である[simh](http://simh.trailing-edge.com/)を使うことで体験することができます。今回はこのsimhで動作しているディスクイメージをTangNanoDCJ11MEMのmicroSDカードに書き込んで本物のPDP-11 CPUで動かします。そのため、まずはsimhの環境を作成します。simhはWindows/Mac/Linux上で動作させることができますが、私はUbuntu 22.04 LTSの環境で動かしました。

### simhのインストール

simhはUbuntuであればパッケージが提供されていますのでaptコマンドで簡単にインストールできます。

```
sudo apt install simh
```

そのほかの環境の場合は[simhの公式サイト](http://simh.trailing-edge.com/)で確認してください。

### simh環境でのUNIX v6インストールと起動

simh環境へのUNIX v6インストール方法は以下のページに詳しくまとまっています。

https://gunkies.org/wiki/Installing\_UNIX\_v6\_(PDP-11)\_on\_SIMH

すでにsimh用にセットアップされた[Software Kit](http://simh.trailing-edge.com/software.html)もあるのですが、ここではUNIX v6の紙テープデータを使ってsimhの環境にインストールしていきます。この作業を通して紙テープからディスクにシステムを読み込み、UNIX v6を起動するまで一連の流れを体験することができます。なお、Software Kitに登録されているuv6swre.zipはPDP-11/45用にカスタマイズされているようで、PDP-11/40の環境では動きませんでした。

インストールが完了したら、simhの環境でUNIX v6を起動してみます。私の場合はsimhのコンフィグファイルとしてunixv6.iniを作成して起動しています。参考のため起動から終了までの実行例を示します。

```
$ cat unixv6.ini　　　　　 ← 作成したsimhのコンフィグファイル
set cpu 11/40
set cpu idle
set tto 7b
set tm0 locked
attach rk0 rk0
attach rk1 rk1
attach rk2 rk2
attach lpt printer.txt
boot rk0
$ pdp11 unixv6.ini         ← コンフィグファイルを指定してPDP-11を起動
PDP-11 simulator V3.8-1
Disabling XQ
@unix　　　　　　　　　　　← ブートディスク rk0にあるunixというファイルを読み込んで実行

login: root　　　　　　　　← rootでログイン
# ps　　　　　　　　　　　 ← 試しにpsコマンドをたたいてみた
TTY  PID COMMAND
       9 -
      18 ps
#
# sync　　　　 ← 停止するときはsync 3回でディスクと同期しておく
# sync
# sync
#　　　　　　　← Ctrl+Eで実行を中断してsimhに戻る
Simulation stopped, PC: 021630 (MOV (SP)+,177776)
sim> quit      ← simhを終了
Goodbye
$
```

TangNanoDCJ11MEMでも同様の流れでUNIX v6を起動することができるはずです。

### UNIX v6のブートの流れ

ここでUNIX v6のブートの流れを整理しておきます。TangNanoDCJ11MEMでも同様の流れになります。一度にすべてを読み込むわけではなく、小さいものからステップを踏んで読み込んでいきます。

1. Bootstrap loaderの起動
    1. RK0ディスクの最初のブロック(512byte)に書かれているカーネルローダーをメモリ000000番地にロードする。
    2. 000000番地からカーネルローダーを実行する。
2. カーネルローダーの起動
    1. カーネルローダーは「＠」を表示し、カーネルファイル名の入力待ちの状態になる。
    2. unixカーネルファイル名を入力する（例：unix）
    3. RK0ディスクにあるunixファイルシステムからunixカーネルファイルを読み込んで、メモリ000000番地にロードする。
    4. 000000番地からunixカーネルを実行する。
3. UNIXカーネルの起動
    - 無事UNIXカーネルが実行されるとlogin: が表示されます。

## TangNanoDCJ11MEMでのUNIX v6の起動

いよいよTangNanoDCJ11MEMでUNIX v6を起動してみます。ハードウェアの設定変更もありますので、GitHubのunix-v6をまず確認してください。

https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/unix-v6

### microSDカードの作成

simh環境ではrk0, rk1, rk2というディスクイメージができているはずです。これらをmicroSDカードに書き込みます。TangNanoDCJ11MEMで実装されているRKディスクドライバの仕様に合わせて書き込めば、アプリケーションからはmicroSDカードがディスクに見えます。このあたりは[GitHubのunix-v6](https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/unix-v6)の説明にも記載されていますので、そちらも確認してください。

以下は書き込みのための手順です。

```
dd if=/dev/zero of=sd.dsk bs=512 count=1024
dd if=rk0 of=sd.dsk bs=512 seek=1024 conv=notrunc
dd if=rk1 of=sd.dsk bs=512 seek=7168 conv=notrunc
dd if=rk2 of=sd.dsk bs=512 seek=13312 conv=notrunc
sudo dd if=sd.dsk of=/dev/sdb
```

SDカードに書き込むときのデバイス名（この例では/dev/sdb）は**必ずSDカード**であるかを確認してください。間違えてハードディスクやSSDを壊してしまうと取り返しがつきません。

### TangNanoDCJ11MEMでUNIX v6を起動

TangNanoDCJ11MEMのファームウェアをUNIX-v6用に書き換え、必要なジャンパー線の取り付けやパターンカットなどハードウェアの調整を行ったのちに、先ほど作成したmicroSDカードを取り付けて174000番地のBootstrap loaderを実行すればUNIX v6が起動します。ターミナルの設定は115200bps、7bitにしてください。なお、PDP11GUIのターミナルであればそのまま使えます。

```
@174000g@unix
mem = 86
RESTRICTED RIGHTS

Use, duplication or disclosure is subject to
restrictions stated in Contract with Western
Electric Company, Inc.

login: root
#
```

### UNIX v6が起動できるまでの様々な課題

現在のTangNanoDCJ11MEMではUNIX v6用のBootstrap loaderの実装やメモリ保護も行われ安定して起動するようになりました。UNIX v6が起動できるまでには様々な課題がみつかりましたが、いずれもRyo Mukaiさんに解決いただきました。ありがとうございました。

なお、発生した課題の詳細については以下のメモに記録していますので、参考にしてください。

https://lateral-apartment-215.notion.site/unix-v6-67b9abee6b784c4795d5094cf69c4f96

## PDP-11実機との違い

TangNanoDCJ11MEMでUNIX v6が動くようにはなりましたが、メモリ空間が60KBしかないため、仮想メモリの利用を前提としたUNIX v6では大きなプログラムが動かないことがわかりました。

例えばC言語を実行すると以下のようにエラーとなります。この例にあるedコマンドはラインエディタですので慣れが必要ですがviコマンドを知っていれば何とかなるかなと思います。

```
# chdir /tmp
# ed test.c　　　　　　　　← ラインエディタを起動
?　　　　　　　　　　　　　← コマンドモードであることを示す
a                          ← appendコマンドで行入力状態にする
main(){　　　　　　　　　　← 間違えないように入力していく
printf("Hello World\n");
}
.　　　　　　　　　　　　　← ピリオドで入力終了。コマンドモードに戻る
w　　　　　　　　　　　　　← ファイルに書き出すコマンド
35　　　　　　　　　　　　 ← 書き出したデータのサイズが表示される
q　　　　　　　　　　　　　← quitコマンドでラインエディタを終了する
# cat test.c　　　　　　　 ← 作成したファイルの内容を表示
main(){
printf("Hello World\n");
}
# cc test.c　　　　　　　　← コンパイルしてみる
Can't find /lib/c0　　　　 ← /lib/c0のファイルは存在するがエラーとなる
#
```

simh環境ではメモリを64KBに設定することができますが、その環境でも同様のエラーが発生しました。

```
# cc test.c
Can't find /lib/c0
#
```

このようにメモリが64KBまでの場合は、UNIX v6の起動確認までは行うことはできますが、C言語を使って何かプログラムを作成したり、カーネルを再構築を行うということはできません。実験環境としては使えるかもしれませんが、せっかくのUNIX環境ですのでC言語は動かしたいところです。

simh環境で何パターンかメモリ容量を変更して確認したところメモリが128KBあればC言語が動作するようです。使用しているFPGA開発ボードのTangNano 20Kのメモリは828Kbitしかなく、使用できる接続ピンも枯渇しているためこのままではメモリ空間を増やすことはできません。搭載されているDCJ11 CPUは4MBまでのメモリ空間を扱うことができますので、外部に物理メモリを接続し、I/OはTangNano 20Kを使用するなどハイブリッドなハードウェアにする必要がありそうです。

## MINI-UNIXを試してみる

TangNanoDCJ11MEMのメモリ容量で動作するUNIX系OSを探したところ、[MINI-UNIX](https://gunkies.org/wiki/MINI-UNIX)というものを見つけました。これはMMUを搭載しないPDP-11用に書き直されたUNIX v6の派生版です。UNIX v6の一部の機能が外されているものの、大部分のUNIX v6の機能が使えるとのことです。

このMINI-UNIXであれば56KByteのメモリで動作するとのことなので、まずはsimhで動かして評価したうえで、問題がなさそうであれば、TangNanoDCJ11MEMで動作させてみます。

追記：[PDP-11 DCJ11 CPUでMINI-UNIXを動かしてみました](https://kanpapa.com/2024/08/tangnanodcj11mem-pdp-11-dcj11-cpu-mini-unix.html) にまとめました。

## まとめ

TangNanoDCJ11MEMでUNIX v6を起動させることはできましたが、メモリ空間の制約から現在のハードウェアでは期待した動作はできませんでした。しかし、UNIX v6を実際に動かすことで、OSの起動の仕組みや構造、仮想メモリの仕組みなどを体験することができました。PDP-11の資産は豊富にありますので、TangNanoDCJ11MEMで動くものを試していきます。
