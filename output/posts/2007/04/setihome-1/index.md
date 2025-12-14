---
title: "玄箱でseti@homeに参加する その２"
date: 2007-04-06
categories: 
  - "server"
tags: 
  - "玄箱"
---

玄箱でのBOINCの準備ができたところで、手持ちのPCにもBOINCをインストールする。

一度PC上でBOINCを動かしてからのほうが作業が楽だと思う。

でも最終的な目的は玄箱のBOINC clientをPCのBOINC managerで制御するため。

もし、seti@homeのアカウントを持っていない場合は、PCのBOINC managerからアカウントを取ってしまおう。うまくいくと、メールでアカウントキーが送られてくる。

玄箱にログインして次のようにコマンドを入れる。

> $ boinc\_cmd --host localhost --project\_attach [http://setiathome.berkeley.edu](http://setiathome.berkeley.edu) xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ←アカウントキー（英文字の羅列）

状態をみるのは以下のコマンド

> $ boinc\_cmd --get\_state
> 
> $ boinc\_cmd --get\_message 0

PCのBOINC Managerからでも制御ができる。「高度な操作」→「コンピュータの選択」→玄箱のIPを入力すればよい。私はパスワードはつけなかったのでそこは空欄。

PCだとこれでアプリケーションをseti@homeのサーバからダウンロードして、勝手に計算を始めるはずなのだが、どうも動かない。

メッセージをみると以下のような怪しいものがでていた。

> SETI@home 1 1174713403 Message from server: platform 'powerpc-unknown-linux-gnu' not found

これってもしかして、玄箱のBOINCで動くseti@homeのアプリケーションが無いってこと？

そういえば、こんなパッケージがあったことを思いだした。

> boinc-app-seti - SETI@home application for the BOINC client

とりあえず、これをインストールして再度チャレンジしたらあっさり動いてしまった。

でも、そういうことなら玄箱の上ではseti@homeのアプリケーションしか動かないってことかな。

アプリケーションのソースがあれば自分でコンパイルすればいいんだろうけど。

ちなみに、玄箱で１つのWORKUNITにかかる時間は、こんな感じ。

> Created 24 Mar 2007 2:13:48 UTC
> 
> Sent 24 Mar 2007 15:54:13 UTC
> 
> Received 29 Mar 2007 8:14:29 UTC
> 
> CPU time 394143.22

５日間かけてやり遂げるだけでも偉いなということで。はい。

もし玄箱でseti@homeをやっている人がいたらチームを組みたいな。
