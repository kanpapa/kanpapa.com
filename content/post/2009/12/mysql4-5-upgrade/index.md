---
title: "MySQLを4.0から5.1にバージョンアップしました"
date: 2009-12-01
slug: "mysql4-5-upgrade"
categories: 
  - "server"
tags: 
  - "movable-type"
  - "mysql"
---

Movable Type 5がMySQL 5.x系しか使えないということで、Movable Type 4のままでまずはMySQLをバージョンアップすることにしました。  
さくらインターネットのサーバを使っているので、手順は以下の通り。

1. MySQL Adminが提供されているので、まずはこれでエクスポート
2. エクスポートしたファイルをさくらのサーバにbackup1.sqlというファイル名でコピー
3. コピーしたファイルの文字コードがUTF-8になっていることを確認
4. さくらサーバのコンパネでMySQL 4のDBをばっさり削除
5. さくらサーバのコンパネでMySQL 5のDBを作成
6. 先ほどエクスポートしたSQLファイルの頭にある「CREATE DATABASE DB名」の行をコメントにする。→DBを設定したときにすでにできてるから。
7. USE DB名の直後に以下の３行を追加
  
SET character\_set\_client = utf8;  
SET character\_set\_connection = utf8;  
SET character\_set\_results = utf8;  
  
13. mysqlコマンドでDBに接続し、以下のコマンドでロード
  
mysql> alter database DB名 character set utf8;  
mysql> \\. backup1.sql  

  
無事移行が完了しました。Movable Type 5への移行はまた次の機会に。
