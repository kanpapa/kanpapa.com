---
title: "MovableTypeでInternal Server Errorがでた"
date: 2008-09-11
slug: "movabletypeinternal-server-error"
draft: true
---

いろいろ、mt4のページ管理画面をいじっていたら突然、Internal Server Errorが表示されるようになってしまった。設定をもとに戻して再構築したり、テンプレートを初期化してみても直らない。 しかし、同じサイトにある「[きょうのかんぱぱ](https://kanpapa.com/)」は何も問題はない。[mt4](https://kanpapa.com/mt4/)だけの問題なのだから、共通的な/mt/配下は問題ないだろうと、/mt4/配下のファイルを確認していたら、.htaccessなるものができている。/today/配下にはこのファイルがない。もしかしてと、mv .htaccess ~/htaccess.backup としたところ直った。どうもこのファイルはダイナミックパブリッシングに設定するとできるようだ。さくらインターネットのレンタルサーバではこの設定がうまく動かないようだ。
