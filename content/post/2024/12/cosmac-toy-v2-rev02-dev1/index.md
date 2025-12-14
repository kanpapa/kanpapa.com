---
title: COSMAC TOY V2を開発中です
date: 2024-12-12
slug: cosmac-toy-v2-rev02-dev1
categories:
- cosmac
- retrocomputing
tags:
- cosmac-toy-v2
image: images/cosmac-toy-v2-rev02-dev1-photo1.jpg
---

部屋の整理をしていたら[COSMAC TOY](https://github.com/kanpapa/cosmac_toy)の実機が何個かでてきました。いずれも[Maker Faire出展](https://kanpapa.com/cosmac/blog/2019/07/cosmac-maker-faire-tokyo-2019-1.html)向けに製作したものです。このまま寝かせておくよりは[COSMAC](https://kanpapa.com/cosmac/cosmac-cpu)を体験したいかたにお譲りするのが良いかなとXで聞いてみたところ、何名かご希望をいただきましたのでBOOTHにて頒布したところすべて引き取り先がきまりました。ありがとうございました。

## COSMAC TOY Version 2の開発

もしかすると、トグルスイッチでのプログラミングやCOSMACに興味があるかたが潜在的にいるのかもと、COSMAC TOYを大幅に見直して、COSMAC TOY V2としてより簡単に製作できるように再設計してみました。

当初のアイデアとしては以下の通りです。

- 基板は１枚にしてシンプルにする。できればB基板サイズに収めたい。
- 入手しやすい部品を使用する。
- メモリの値の確認や修正が行えるようにする。
- CPUの全ピンにアクセスできるようにする。
- Q出力にはLEDを接続して基板だけで遊べるようにする。
- S-RAMは300mil/600milどちらも対応したい。

これらを取り入れたところ以下のような基板設計になりました。

![](images/cosmac-toy-v2-rev02-dev1-pcb1.png)

3Dイメージだとこのようになります。

![](images/cosmac-toy-v2-rev02-dev1-pcb3d1.png)

実はRev.0.2基板の製作の前にRev.0.1基板も試作しました。回路を手直ししながらメモリの読み込みを確認している様子です。この結果をもとにRev.0.2基板を起こしています。

https://youtu.be/m1Ll-BvsBz4

COSMAC TOY V2の詳細はGitHubにまとめましたのでそちらをご覧ください。サンプルプログラムも大幅に整理して命令コードの説明や動作中の写真や動画リンクも追加しました。COSMAC TOY V1を利用のかたも参考になるかもしれません。

https://github.com/kanpapa/cosmac\_toy\_v2

## Rev.0.2基板が完成

とりあえずRev. 0.2ということで基板を5枚製作しました。1枚は自身で製作して今の所は快調に動作しています。

![](images/cosmac-toy-v2-rev02-dev1-photo1-1024x771.jpg)

GitHubにガーバーデータを公開していますのでそちらで基板を発注いただけます。

## 今後について

まずはRev.0.2でサンプルプログラムを拡充させてみようかと思っています。CPUの全ピンにアクセスできるようになったので、他のハードウェアと組み合わせたサンプルプログラムも考え中です。

次版の製作は今のところ未定ですが改善点があればアップデートしていきますので、お気づきの点があればGitHubのissueに登録ください。サンプルプログラムのプルリクも歓迎です。またニーズがあれば完成品の頒布も考えたいと思っています。
