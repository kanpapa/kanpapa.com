---
title: "LinkStationにConcrete5をいれてみる。"
date: 2009-01-24
slug: "linkstationconcrete5"
categories: 
  - "pc"
tags: 
  - "cms"
  - "debian"
  - "linkstation"
  - "linux"
  - "mysql"
---

LinkStationのDebianにインストールしたMovable Type 4がいまいちだったので、他にいい素材がないか探していたら、今評判のCMSとして[Concrete5](http://www.concrete5.org/)というのを見つけたので、LinkStationのDebianにインストールしてみました。

$ sudo apt-get install apache mysql-server php5 php5-mysql libapache-mod-php5 php5-gd

$ cd ~

$ unzip concrete5.2.0RC2.zip

$ sudo mv concrete5.2.0RC2 /var/www/concrete5

$ cd /var/www/concrete5

$ sudo chmod 777 config files

$ cd concrete/libraries/3rdparty

$ sudo chmod 755 htmldiff.py?

$ mysql -u root -p

Enter password:?

mysql> create database concrete default character set utf8;

Query OK, 1 row affected (0.01 sec)

mysql> grant all on concrete.\* to conuser@localhost identified by 'password';

Query OK, 0 rows affected (0.05 sec)

mysql> FLUSH PRIVILEGES;

Query OK, 0 rows affected (0.00 sec)

mysql> quit

Bye

$?

あとは、http://192.168.3.xxx/concrete5/ でセットアップ開始。

システム環境に問題があった場合は、左側の画面に表示されるのでつぶしていきます。

システム環境に問題が無くなったら、右側の画面でサイト名やメアド、MySQLのDB情報を設定するだけ。

気になるスピードですが、まあなんとかなるかなぁという感じでした。

i18N版も開発が進んでいるようなので、そちらも試してみたいと思います。
