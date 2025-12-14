---
title: "玄箱でYahoo!デベロッパーネットワークに参加する"
date: 2007-04-12
categories: 
  - "server"
tags: 
  - "玄箱"
---

さらに何かおもしろいことはないかと思っていたところで、「Yahoo!デベロッパーネットワーク」なるものを見つけました。

Yahoo!JAPANの公開APIが使えるらしいとのことで、手持ちのYahoo!IDを使ってアプリケーションIDを取得すれば準備完了です。早速サンプルプログラムを玄箱の上で動かしてみました。

この時点で玄箱にはApache1.3とPHP4がインストール済みです。

サンプルプログラムがあったので、それを/var/wwwに展開しました。

とりあえずわかりやすそうなsearchから実験です。

> $ cd
> 
> $ ls
> 
> yjws-1.7.tgz
> 
> $ zcat \*.tgz | tar xvf -
> 
> $ cd yjws-1.7
> 
> $ ls -l
> 
> total 16
> 
> drwxr-xr-x 3 ocha users 4096 Sep 5 2006 auctions
> 
> drwxr-xr-x 4 ocha users 4096 Dec 15 15:06 category
> 
> drwxr-xr-x 5 ocha users 4096 Sep 5 2006 search
> 
> drwxr-xr-x 4 ocha users 4096 Sep 5 2006 webunit
> 
> $ cd search
> 
> $ ls
> 
> README.txt javascript perl php
> 
> $ cd php
> 
> $ ls
> 
> 1.0
> 
> $ cd 1.0
> 
> $ ls -l
> 
> total 20
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example1
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example2
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example3
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example4
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example5
> 
> $ cd example1
> 
> $ ls
> 
> YJSearchExample.php common.php
> 
> $ cd ..
> 
> $ sudo mv example\* /var/www/. ←面倒なので全部移動！
> 
> $ cd /var/www
> 
> $ ls -l
> 
> total 36
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example1
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example2
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example3
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example4
> 
> drwxr-xr-x 2 ocha users 4096 Sep 5 2006 example5
> 
> \-rw-r--r-- 1 www-data www-data 5258 Apr 3 23:38 index.html
> 
> \-rw-r--r-- 1 root root 20 Apr 8 13:50 info.php
> 
> $

この状態で、http://玄箱のIP/example1/YJSearchExample.php　と叩いてみたところ何やらエラーが。

どうもxmldomが必要のようです。早速、検索。

> $ apt-cache search domxml
> 
> php4-domxml - XMLv2 module for php4

ありました。早速インストール

> $ sudo apt-get install php4-domxml

あと、

> common.phpの"$appid ="部分に取得したアプリケーションIDを設定してください。

ということなので、ここに取得したアプリケーションIDを設定。

再度、http://玄箱のIP/example1/YJSearchExample.phpをブラウザで開くと、検索キーワードを入力できる画面が表示されました。

適当な言葉を入れて、検索すると、結果がちゃんと表示されます。

思ったより簡単ですね。こんな開発サーバにも玄箱は使えそうです。
