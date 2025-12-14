---
title: "旧ConoHaから新ConoHaにMT環境を移行してみた。"
date: 2015-12-27
slug: "new-conoha-centos7"
categories: 
  - "server"
tags: 
  - "conoha"
---

これまでkanpapa.comは[ConoHa](http://conoha.jp/)を使ってきましたが、リニューアルされたConoHaに移行することにしました。リニューアル後も利用料金は変わらないのですが、システムが刷新されSSD化もされています。APIなども準備されているとのことで楽しそうです。ついでにCentOS6からCentOS7にしてみます。

kanpapa.comでは[MovableType](http://movabletype.jp/)を使用していますので、次の手順で移行することにしました。

<!--more-->

1\. 現ConoHaサーバのバックアップを取得

- Apache設定ファイル一式（/etc/httpd配下一式）
- SSLサーバ証明書（/etc/letsencrypt配下一式）
- MovableTypeにインストールしたプラグイン（/var/www/cgi-bin/mt/plugin）
- MovableTypeのシステムメニューでのバックアップ

2\. 新ConoHaサーバーでのセットアップ

- CentOS7をVPSにインストールして起動
- SSLサーバ証明書のコピー
- Apacheのインストール
- 現Apache設定ファイルとdiffを取りApacheの環境設定。httpsまで動くことを確認
- MariaDBのインストールとDB rootユーザの設定
- MovableTypeのインストール
- MovableTypeで必要なPerlパッケージのインストール
- 現MovableTypeで追加したプラグインのコピー
- MovableTypeのバックアップファイルからシステムメニューでの復元
- MovableTypeでの全体の再構築。コンテンツファイルができていることを確認。

3\. DNSの変更

- kanpapa.comのAレコードを新ConoHaサーバに設定
- MXレコードはとりあえず現サーバのまま。
- 新ConoHaのDNSサーバにNSを移行。

4\. その他細かい調整

- favicon.icoを現環境から新環境をコピー（忘れてました）
- サイトマップが生成されていなかったのでMovableTypeでsitemap.xmlが生成されるように設定
- メール転送の設定（/etc/aliases）
- ログ監視の設定（yum install logwatch）

およそ半日ぐらいで新ConoHaに移行が完了しました。不要なディレクトリも消えてスッキリです。まだ現ConoHaにメール環境は残してありますが、新ConoHaでpostfixの設定を行いMXを書き換えれば完了です。

今 回一番大きな変更はCentOS6からCentOS7にしたことで、MySQLがMariaDBに変わったり、Firewallがiptableから firewalldに変わったり、パッケージの起動コマンドが変わったりと細かい点が変更されていたのでやや戸惑いましたが、新しい環境に触れる良い機会 になりました。たまにはこのようなOS移行を行うと勉強になりますね。
