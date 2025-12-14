---
title: "PDP-11 DCJ11 CPUでMINI-UNIXを動かしてみました"
date: 2024-08-04
categories: 
  - "pdp-11"
  - "retrocomputing"
tags: 
  - "dcj11"
  - "fpga"
  - "mini-unix"
  - "pdp-11"
  - "simh"
  - "tang-nano"
  - "tangnanodcj11mem"
coverImage: "tangnanodcj11mem-pdp-11-dcj11-cpu-mini-unix1.jpg"
---

本記事はPDP-11の命令セットを持つ[DCJ11(Jaws)CPU](https://gunkies.org/wiki/J-11_chip_set)を動作させるためにRyo Mukaiさんが開発した[TangNanoDCJ11MEM](https://github.com/ryomuk/TangNanoDCJ11MEM)を使用しています。GitHubで公開されています。

## PDP-11 CPUでMINI-UNIXを動かしたい

前回は[PDP-11 DCJ11 CPUでUNIX v6を動かしてみました](https://kanpapa.com/2024/08/tangnanodcj11mem-pdp-11-cpu-4-unix-v6.html)が、TangNanoDCJ11MEMで実装されているメモリ容量ではUNIX v6の本格的な利用は難しいことがわかりました。そこでMMUを使用せず56KBのメモリでも動作するらしい[MINI-UNIX](https://gunkies.org/wiki/MINI-UNIX)を動かすことにチャレンジしてみました。まずはsimhで動かして評価したうえで、問題がなさそうであれば、TangNanoDCJ11MEMで動作させてみます。

## MINI-UNIXとは

[MINI-UNIX](https://gunkies.org/wiki/MINI-UNIX)はMMUを搭載しないローエンドの[PDP-11/05](https://gunkies.org/wiki/PDP-11/05)などに書き直されたUNIX v6の派生版です。UNIX v6の一部の機能が外されているものの、大部分のUNIX v6の機能が使え、56KBのメモリで動作するとのことです。

調べてみたところ、[以下のサイト](https://www.tavi.co.uk/unixhistory/mini-unix.html)でsimh環境へのインストール方法がまとまっているようで、simhでどのようなものであるかの確認ができそうです。

https://www.tavi.co.uk/unixhistory/mini-unix.html

## シミュレーション環境でのMINI-UNIXの起動

UNIX v6の時と同様に歴史的なコンピュータのシミュレーション環境である[simh](http://simh.trailing-edge.com/)を使います。この上でMINI-UNIXを起動し、56KBのメモリでどこまで動くのかを確認したのちに、作成したディスクイメージをTangNanoDCJ11MEMのmicroSDカードに書き込んで本物のPDP-11 CPUで動かします。

### simhのインストール

simhはUbuntuであればパッケージが提供されていますのでaptコマンドで簡単にインストールできます。

```
sudo apt install simh
```

そのほかの環境の場合は[simhの公式サイト](http://simh.trailing-edge.com/)で確認してください。

### 必要なファイルの入手

[MINI-UNIXのサイト](https://www.tavi.co.uk/unixhistory/mini-unix.html)から必要なファイルをダウンロードします。最低限以下の２つのファイルがあればsimh環境でのMINI-UNIXの起動ができます。

- munix-tap.zip - MINI-UNIXのインストールテープ

- munix-initfiles.zip - simh用のコンフィグレーションファイル

ダウンロードしたファイルはunzipで展開しておきます。

```
$ unzip munix-initfiles.zip
Archive:  munix-initfiles.zip
  inflating: pdp11.ini
  inflating: setup.ini
$ unzip munix-tap.zip
Archive:  munix-tap.zip
  inflating: munix.tap
$ ls -l *.ini *.tap
-rw-r--r-- 1 ocha ocha 6292004 Aug  5  2017 munix.tap
-rw-r--r-- 1 ocha ocha      90 Dec 31  2019 pdp11.ini
-rw-r--r-- 1 ocha ocha     219 Dec 31  2019 setup.ini
$
```

### インストールテープからブートしてディスクイメージを作成する

インストール用のsimhコンフィグファイルを確認してみます。

```
set cpu 11/20
set cpu 64k
attach tm0 munix.tap
attach rk0 system.dsk
attach rk1 source.dsk
attach rk2 doc.dsk
dep 100000 012700
dep 100002 172526
dep 100004 010040
dep 100006 012740
dep 100010 060003
dep 100012 000777
```

ダウンロードしたMINI-UNIXのインストールテープはtm0にattachされます。rk0～rk2はディスクイメージにattachされますが最初は中身は空の状態です。dep命令で100000番地からメモリに書き込みを行っていますが、これはインストールテープからbootstrapを読み込むプログラムのようです。参考までに逆アセンブルリストを以下に示します。テープドライバのレジスタを操作していることがわかります。

```
100000: mov     #172526,r0              [012700 172526]
100004: mov     r0,-(r0)                [010040]
100006: mov     #060003,-(r0)           [012740 060003]
100012: br      100012                  [000777]
```

インストール用のsimhのコンフィグファイルを使い、[Mini-UNIXのサイト](https://www.tavi.co.uk/unixhistory/mini-unix.html)の説明にしたがってインストールしていきます。

```
$ pdp11 setup.ini 　　　←セットアップ用のコンフィグファイルを指定して実行

PDP-11 simulator V3.8-1
Disabling CR
Disabling XQ
RK: creating new file
RK: creating new file
RK: creating new file
sim> run 100000　　　　　←コンフィグファイルで書き込んだbootstrapを起動

Simulation stopped, PC: 100012 (BR 100012)　←数分したらCtrl-Eでsimhを一度中断
sim> run 0　　　　　　←インストールテープからメモリに読み込んだツールを実行
=tmrk                 ←テープからrkディスクにコピーするコマンド
disk offset　　　　　 ←ディスクの先頭にブートローダーをコピーする
0
tape offset
100
count
1
=tmrk                  ←もう一度テープからrkディスクにコピーするコマンドを実行
disk offset　　　　　　←ディスクのブートローダー以降にディスクイメージをコピー
1
tape offset
101
count
3999
=　　　　　　　　　　　←読み込みが終わったらCtrl-Eでsimhを終了
Simulation stopped, PC: 137274 (TSTB @#177560)
sim> quit
Goodbye
$ ls -l *.dsk
total 28648
-rw-r--r-- 1 ocha ocha        0 Jul 30 16:44 doc.dsk
-rw-r--r-- 1 ocha ocha        0 Jul 30 16:44 source.dsk
-rw-r--r-- 1 ocha ocha  2048000 Jul 30 16:46 system.dsk  ←システムディスクができている
$ 
```

このようにsystem.dskにデータが書き込まれていればテープからのコピーは完了です。

### システムディスクから起動する

システムディスクの作成が完了したら、simhの環境でMINI-UNIXを起動してみます。起動用に提供されているコンフィグレーションファイルpdp11.iniを示します。PDP-11/20のメモリ64KBで各ディスクイメージをattachしている単純なものです。

```
set cpu 11/20
set cpu 64k
attach rk0 system.dsk
attach rk1 source.dsk
attach rk2 doc.dsk
```

pdp11.iniはデフォルトのファイル名ですので、pdp11と起動すれば自動的に読み込まれます。参考のため起動から終了までの実行例を示します。

```
$ pdp11

PDP-11 simulator V3.8-1
Disabling CR
Disabling XQ
sim> boot rk　　　　　　← rkディスクからブート
@rkmx　　　　　　　　　 ← ブートディスク rk0にあるrkmxというファイルを読み込んで実行

RESTRICTED RIGHTS

USE, DUPLICATION OR DISCLOSURE IS SUBJECT TO
RESTRICTIONS STATED IN YOUR CONTRACT WITH
WESTERN ELECTRIC COMPANY, INC.

;login: root     ← rootでログイン
#
# ps             ← 試しにpsコマンドをたたいてみた
  PID TTY TIME COMMAND
     6 8  0:27 -
     7 8  0:00 ps
# ls -l
total 168
drwxrwxr-x  2 bin      1136 Sep 18 01:02 bin
drwxrwxr-x  2 bin      1824 Sep 18 01:24 dev
drwxrwxr-x  2 bin       496 Sep 18 01:47 etc
-rwxrwxrwx  1 root    19208 Sep  4 03:18 hpmx
drwxrwxr-x  2 bin       464 Sep  4 03:37 lib
drwxrwxr-x  2 bin        32 May 13  1975 mnt
-rwxrwxrwx  1 root    19010 Sep 18 01:18 mx
-rwxrwxrwx  1 root    19010 Sep 18 01:28 rkmx
-rwxrwxrwx  1 root    19148 Sep  4 03:15 rpmx
drwxrwxrwx  2 bin       272 Sep 18 04:23 tmp
drwxrwxr-x 13 bin       240 Jun 17 13:38 usr
# sync         ← 停止するときはsync 3回でディスクと同期しておく
# sync
# sync
#              ← Ctrl+Eで実行を中断してsimhに戻る
Simulation stopped, PC: 012030 (MOV (SP)+,177776)
sim> quit      ← simhを終了
Goodbye
$
```

### C言語でHello Worldを動かしてみる

UNIX v6では動かなかったC言語をMINI-UNIXで動かしてみます。手順はUNIX v6の時と同じです。

```
# chdir /tmp
# ls
# ed test.c                  ← ラインエディタを起動
?                            ← コマンドモードであることを示す
a                            ← appendコマンドで行入力状態にする
main(){                      ← 間違えないように入力していく
printf("Hello World\n");
}
.                            ← ピリオドで入力終了。コマンドモードに戻る
w                            ← ファイルに書き出すコマンド
35                           ← 書き出したデータのサイズが表示される
q                            ← quitコマンドでラインエディタを終了する
# cat test.c                 ← 作成したファイルの内容を表示
main(){
printf("Hello World\n");
}
# cc test.c　　　　　　　　　 ← コンパイラは問題なく終了
# ls -l
total 4
-rwxrwxrwx  1 root     1188 Sep 18 01:52 a.out    ← a.outができている
-rw-rw-rw- 1 root       35 Sep 18 01:52 test.c
# a.out
Hello World　　　　　　　　　　　　　　　　　     ← 実行OK
#
Simulation stopped, PC: 012030 (MOV (SP)+,177776)
sim> show cpu
CPU, 11/20, idle disabled, autoconfiguration enabled, 64KB　← メモリ容量は64KB
sim>　　　　　
```

問題なくHello Worldが表示されました。

### カーネルのセルフビルド

simh環境ではカーネルのセルフビルドを行うこともできます。カーネルのソースは/usr/sysの下にありますので、ここに用意されているrunスクリプトをshで実行するとカーネルがビルドされます。なお、いきなり /rkmx, /rpmx, /hpmxのカーネルファイルが上書きされますので十分注意してください。

## TangNanoDCJ11MEMでのMINI-UNIXの起動

いよいよTangNanoDCJ11MEMでMINI-UNIXを起動してみます。動作環境はGitHubのunix-v6と同じですのでGitHubのリポジトリを確認してください。

https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/unix-v6

### microSDカードの作成

simh環境ではsystem.dsk, source.dsk, doc.dskというディスクイメージができているはずです。これらをmicroSDカードに書き込みます。TangNanoDCJ11MEMで実装されているRKディスクドライバの仕様に合わせて書き込めば、アプリケーションからはmicroSDカードがディスクに見えます。このあたりは[GitHubのunix-v6](https://github.com/ryomuk/TangNanoDCJ11MEM/tree/main/applications/unix-v6)の説明にも記載されていますので、そちらも確認してください。

以下は書き込みのための手順です。

```
$ dd if=/dev/zero of=sd.dsk bs=512 count=1024
$ dd if=system.dsk of=sd.dsk bs=512 seek=1024 conv=notrunc
$ dd if=source.dsk of=sd.dsk bs=512 seek=7168 conv=notrunc
$ dd if=doc.dsk of=sd.dsk bs=512 seek=13312 conv=notrunc
$ sudo dd if=sd.dsk of=/dev/sdb
```

microSDカードに書き込むときのデバイス名（この例では/dev/sdb）は**必ずmicroSDカード**であるかを確認してください。間違えてハードディスクやSSDを壊してしまうと取り返しがつきません。

### MINI-UNIXの起動

UNIX-v6用に準備したTangNanoDCJ11MEMに先ほど作成したmicroSDカードを取り付けて174000番地のBootstrap loaderを実行し、カーネルのファイル名である rkmx を入力すればMINI-UNIXが起動します。ターミナルの設定は115200bpsにしてください。PDP11GUIのターミナルも使えます。

```
@174000g@rkmx

RESTRICTED RIGHTS

USE, DUPLICATION OR DISCLOSURE IS SUBJECT TO
RESTRICTIONS STATED IN YOUR CONTRACT WITH
WESTERN ELECTRIC COMPANY, INC.

login: root
# 
# ls -l
total 168
drwxrwxr-x  2 bin      1136 Sep 18 01:02 bin
drwxrwxr-x  2 bin      1824 Sep 18 01:24 dev
drwxrwxr-x  2 bin       496 Sep 18 01:47 etc
-rwxrwxrwx  1 root    19208 Sep  4 03:18 hpmx
drwxrwxr-x  2 bin       464 Sep  4 03:37 lib
drwxrwxr-x  2 bin        32 May 13  1975 mnt
-rwxrwxrwx  1 root    19010 Sep 18 01:18 mx
-rwxrwxrwx  1 root    19010 Sep 18 01:28 rkmx
-rwxrwxrwx  1 root    19148 Sep  4 03:15 rpmx
drwxrwxrwx  2 bin       272 Sep 18 01:53 tmp
drwxrwxr-x 13 bin       240 Jun 17 13:38 usr
# ps ax
  PID TTY TIME COMMAND
     0 8  0:00 /etc/init
     6 8  0:24 -
    10 8  0:00 ps ax
     5 8  0:00 /etc/update
#
```

特に問題なく動作しているようです。

### C言語でHello Worldを動かしてみる

TangNanoDCJ11MEMのUNIX v6では動かせなかったC言語が動作するかを確認してみます。

```
# chdir /tmp
# ed test1.c
?
a
main(){
printf("Hello World\n");
}
.
w
35
q
# cat test1.c
main(){
printf("Hello World\n");
}
# cc test1.c
# ls -l
total 4
-rwxrwxrwx  1 root     1188 Sep 18 01:56 a.out
-rw-rw-rw- 1 root       35 Sep 18 01:56 test1.c
# a.out
Hello World
#
```

問題なく動作することが確認できました。

### カーネルのセルフビルド

カーネルのセルフビルドを試してみたのですが、simh環境とは異なりコンパイル中に大量のエラーが出て、最終的にはHALTになりました。こちらは原因調査中です。→[TangNanoDCJ11MEM Rev.2](https://kanpapa.com/2025/09/tangnanodcj11mem-pdp-11-dcj11-cpu-mini-unix-rev2.html)で解決しました。

## MINI-UNIXを使ってみる

### UNIX v6との違いと使用感

まだ本格的に使ってはいないのですが、気づいた点をあげておきます。、

- bootの時のファイル名ですが、mxでも良さそう。rkmxと同じものがmxとして存在します。

- unix v6に比べると、ややもっさりした動きに見えます。制限された環境なのでやむを得ないようです。

- 一部の命令は下位CPUでも動くようにエミュレーションしているそうです。→ここを外すと速くなるかも。

- パイプは存在しないので、シェルのパイプはファイルで代用している。→便利なので無いよりはまし。

- simh環境ではカーネルのセルフビルドを行うことができますが、TangNanoDCJ11MEMではビルド中にエラーが発生します。この原因は調査中です。→[TangNanoDCJ11MEM Rev.2](https://kanpapa.com/2025/09/tangnanodcj11mem-pdp-11-dcj11-cpu-mini-unix-rev2.html)で解決しました。

- MINI-UNIXの十分なdocumentは用意されているようですが、まだ目を通せていないので何かあれば追記します。

### source.dsk, doc.dskをattachしてみる

simhで作成した環境ではsource.dsk, doc.dskのディスクが空の状態です。MINI-UNIXのウェブサイトに掲載されていますが、ディスクイメージが発見されたそうなので、それをattachしてmountしてみます。

ディスクイメージがまとまっているzipファイル名はmunixrks.zipです。これをダウンロードしてunzipし、microSDカードを再作成しました。

```
$ unzip munixrks.zip
Archive:  munixrks.zip
  inflating: mxrk05a.img　　　　　　 ; system.dsk ... これは使わない
  inflating: mxrk05b.img             ; source.dsk？ 
  inflating: mxrk05c.img             ; doc.dsk？
$ ls -l *.img
total 8508
-rw-r--r-- 1 ocha ocha 2462208 Jun  9  2020 mxrk05a.img
-rw-r--r-- 1 ocha ocha 2048000 Jun  9  2020 mxrk05b.img
-rw-r--r-- 1 ocha ocha 2048000 Jun  9  2020 mxrk05c.img
$ cp mxrk05b.img source.dsk　　　　 ← source.dskファイルを上書き
$ cp mxrk05c.img doc.dsk　　　　　　← doc.dskファイルを上書き
$ dd if=/dev/zero of=sd.dsk bs=512 count=1024  ←ここから先はmicroSDカードの作成と同じ
$ dd if=system.dsk of=sd.dsk bs=512 seek=1024 conv=notrunc
$ dd if=source.dsk of=sd.dsk bs=512 seek=7168 conv=notrunc
$ dd if=doc.dsk of=sd.dsk bs=512 seek=13312 conv=notrunc
$ sudo dd if=sd.dsk of=/dev/sdb
```

新しく作ったmicroSDカードで起動してmountしてみます。mountコマンドは/etc/mountです。マウントポイントは/mntがありましたので、そこを使いました。なお、ディスクデバイスが２つしか作成されていなかったので、３つのディスクを接続するときはmknodが必要のようです。（まだ未確認）

今回はsource.dskを/mntにmountしてみました。

```
@174000g@rkmx

RESTRICTED RIGHTS

USE, DUPLICATION OR DISCLOSURE IS SUBJECT TO
RESTRICTIONS STATED IN YOUR CONTRACT WITH
WESTERN ELECTRIC COMPANY, INC.

login: root
# df
/dev/rk0 805
/dev/rk1 773
# /etc/mount /dev/rk1 /mnt　　　　← /mnt に /dev/rk1をmount
# chdir /mnt
# ls -l                           ← /dev/rk1にあるソースファイルが見えている
total 36
drwxrwxr-x  2 bin       368 Jan 26  1976 as
drwxrwxr-x  2 bin       928 Aug 31 02:34 c
drwxrwxr-x  5 bin       128 May 13  1975 cref
drwxrwxr-x 11 bin       368 Sep  4 01:45 fort
drwxrwxr-x  2 bin      1248 Jan 27  1976 iolib
drwxrwxr-x  2 bin       320 Jan 27  1976 m6
drwxrwxr-x  2 bin       464 Sep  4 01:46 mdec
drwxrwxr-x  2 bin       288 Sep  3 23:35 rat
-rw-rw-r-- 1 bin       753 May 18  1975 run
drwxrwxr-x  2 bin      1696 Sep  4 04:41 s1
drwxrwxr-x  2 bin      1280 Sep  4 01:47 s2
drwxrwxr-x  2 bin       816 Jan 26  1976 s3
drwxrwxr-x  2 bin      2544 Jan 26  1976 s4
drwxrwxr-x  2 bin      1264 Jan 26  1976 s5
drwxrwxr-x  2 bin       800 Aug 31 00:28 s7
drwxrwxr-x  2 bin       384 Sep  4 03:38 salloc
drwxrwxr-x  2 bin       224 Aug 30 22:44 sno
drwxrwxrwx  3 hl        192 Sep  4 03:47 tmg
drwxrwxr-x  4 bin        80 May 13  1975 yacc
#
```

これでディスクのmountができることも確認できました。

## まとめ

TangNanoDCJ11MEMでMINI-UNIXを使うことができましたが、カーネルのセルフビルドなどまだ動かない部分もありますので、引き続き調べてみようと思います。また、MINI-UNIXは完全なUNIX v6というわけではありませんので、いずれはUNIX v6を動かせるような環境を準備できればと考えています。

20250915追記：[PDP-11 DCJ11 CPUでMini-UNIXを動かしてみました（TangNanoDCJ11MEM Rev.2版）](https://kanpapa.com/2025/09/tangnanodcj11mem-pdp-11-dcj11-cpu-mini-unix-rev2.html)もご覧ください。
