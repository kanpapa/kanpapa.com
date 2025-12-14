---
title: "MovableTypeからWordPressに移行する方法"
date: 2024-01-28
categories: 
  - "server"
tags: 
  - "cms"
  - "movable-type"
  - "wordpress"
coverImage: "migrate-movabletype-to-wordpress1.png"
---

これまでCMSとしてMovableTypeを利用してきましたが、OSのアップグレードと同時にWordPressに移行しましたので、その移行例をまとめておきました。今回はマルチサイト構成で運営しています。

## WordPressのテスト環境の準備

MovableTypeとWordPressではコンテンツの管理方法が全く違います。MovableTypeは静的なコンテンツを生成し、WordPressは動的にコンテンツを生成します。このあたりの動きを確認するために、PCのDockerでWordPressを動かしてコンテンツの移行を試してみることにしました。

WordPressの初期設定はあちこちで紹介されていますので、ここでは省略します。また、今回はテストなので、httpsではなくhttpで動かしています。なお、画像の移行作業ぐらいからは本番サーバーに近づけるために、VMWareのUbuntuで作業を進めました。

## MovableTypeの記事をWordpressにインポート

MovableTypeでエクスポートした記事データをWordPressにインポートするプラグインが提供されていますので、まずはこれを使ってみます。ダッシュボードのツールにあるMovable Type と TypePadインポーターをインストールして使いました。

https://ja.wordpress.org/plugins/movabletype-importer

エクスポートしたデータ自体は問題なく取り込めましたが、これは記事だけですので、画像データをどうするかは別に考えないといけないようです。

## テーマを設定する

ブログ用にテーマを設定します。Cocoonというテーマがよく使われているようなのでまずはこれにしてみました。なかなかかっこいい外観になりました。

https://wp-cocoon.com

## 記事のURLを旧ブログと同じにする

これまでのMovableTypeでは以下のようなURLになっていました。

```
https://kanpapa.com/today/2023/11/mini-pupper-2-5-legs-assembly.html
```

ところがWordPressでは以下のようになってしまいました。

```
http://192.168.0.109:9080/2023/11/06/mini-pupper-2-5-legs-assembly/
```

これを修正するにはパーマリンクを設定します。管理メニュー→ダッシュボード→設定→パーマリンクのカスタム構造で以下のように設定します。

```
/%year%/%monthnum%/%postname%.html
```

この設定を行うことで、MovabelTypeと同じURLにできました。

```
http://192.168.0.109:9080/2023/11/mini-pupper-2-5-legs-assembly.html
```

## 画像ファイルのインポート

これまでのMovableTypeではサイトトップの直下にimagesというディレクトリを作り、その中に画像ファイルを格納していました。URLは以下のようになります。

```
https://kanpapa.com/today/images/MP2_5_leg_parts1.jpg
```

WordPressだとメディアライブラリにアップロードすると、以下のようにwp-contentのuploadsに年月ごとに格納されるようです。

```
http://192.168.0.109:9080/wp-content/uploads/2023/11/DVME_CPU2_board1.jpg
```

まずは、現在稼働しているサーバから画像関係のディレクトリをバックアップしたものをサーバー上にコピーして、以下の場所に配置しました。これでURLで直接アクセスができる状態になっています。

```
/var/www/html/wp-content/uploads/cosmac/images
/var/www/html/wp-content/uploads/cosmac/assets_c
/var/www/html/wp-content/uploads/today/images
/var/www/html/wp-content/uploads/today/assets_c
```

次に上記のディレクトリから、Add From Serverプラグインで画像データをメディアライブラリに一括インポートをしました。ファイル数が多く、一回ではできなかったので複数回に分けて行いました。

https://ja.wordpress.org/plugins/add-from-server

このようにすることで、画像データは旧ブログに近いURLでアクセスもできますし、メディアライブラリにも存在する状態になります。旧コンテンツの画像URLは/wp-content/uploads/today/imagesに書き換えることで画像データのリンク切れを防ぎ、徐々にメディアライブラリの画像に入れ替えていく方法を取りました。

## 画像データのURLの書き換え

旧コンテンツの画像のコンテンツにアクセスするためには、記事中のURLを書き換えなければなりません。以下のようなソースがあった場合は

```
<p><a href="https://kanpapa.com/today/assets_c/2018/11/cosmac_book1-2970.html"><img fetchpriority="high" decoding="async" src="https://kanpapa.com/today/assets_c/2018/11/cosmac_book1-thumb-autox428-2970.jpg" alt="cosmac_book1.jpg" class="mt-image-none" width="320" height="428" /></a></p>
```

以下のようにURLを書き換える必要があります。

```
<p><a href="https://192.168.0.224/wp-content/uploads/today/assets_c/2018/11/cosmac_book1-2970.html"><img fetchpriority="high" decoding="async" src="https://192.168.0.224/wp-content/uploads/today/assets_c/2018/11/cosmac_book1-thumb-autox428-2970.jpg" alt="cosmac_book1.jpg" class="mt-image-none" width="320" height="428" /></a></p>
```

ここではサイト内のURLやテキストの一括変換を行えるSearch Regexプラグインを使いました。

https://ja.wordpress.org/plugins/search-regex

インポート先のURLが4種類あるので、以下の4パターンについて置換を行いました。（テスト環境のため置換後はhttpになっています。）

|  | **検索文字列** | **置換後** |
| --- | --- | --- |
| **パターン1** | https://kanpapa.com/today/assets\_c/ | http://192.168.0.224/wp-content/uploads/today/assets\_c/ |
| **パターン2** | https://kanpapa.com/today/images/ | http://192.168.0.224/wp-content/uploads/today/images/ |
| **パターン3** | https://kanpapa.com/cosmac/assets\_c/ | http://192.168.0.224/wp-content/uploads/cosmac/assets\_c/ |
| **パターン4** | https://kanpapa.com/cosmac/images/ | http://192.168.0.224/wp-content/uploads/cosmac/images/ |

## アンダーバーとハイフンの問題

WordPressに移行した記事をチェックしてみたところ、オリジナルのブログURLと今回作成したブログURLが異なることがあり、リンク切れがあることがわかりました。

旧ブログのURL　https://kanpapa.com/today/2013/09/mbed**\-**lpc1114fn28.html  
新ブログのURL　https://192.168.0.224/today/2013/09/mbed**\_**lpc1114fn28.html

MovableTypeではDBデータに含まれているアンダーバーがハイフンに自動変換されてURLが作成されているようです。移行先のWordPressではDBデータの値がそのまま使用されているようです。SEO的に記事のURLは保持したいところです。Regexで記事中のURLだけアンダーバーをハイフンに書き換えることができれば良いのですが、どうも記事中のURLだけを書き換えるのは難しそうです。そこでmySQLのデータを直接変更できないかを考えてみます。

## WordPressのDBを修正する

mySQLAdminなどUIベースのツールを入れておくとDBの管理が楽なのですが、インストールしていないので、CUIで確認したところ、wp\_2\_postsテーブルのpost\_nameとguid、wp\_2\_termsテーブルのslugでアンダーバーをハイフンに置換すれば良さそうです。まずは作業前には必ずmySQLのDBバックアップを行っておきます。

```
$ mysqldump -h localhost -u root -p --databases wordpress > wordpress_dump_12150722.sql
```

次にアンダーバーが含まれている記事のレコードを指定して確認します。

```
$ mysql -u root -p
Enter password: 
MariaDB [(none)]> use wordpress
MariaDB [wordpress]> select ID,post_name,guid from wp_2_posts where ID = 300;
+-----+-----------------------------+---------------------------------------------------------------------+
| ID  | post_name                   | guid                                                                |
+-----+-----------------------------+---------------------------------------------------------------------+
| 300 | passwordmaster3_311_leopard | http://192.168.0.224/today/2007/10/31/passwordmaster3_311_leopard/ |
+-----+-----------------------------+---------------------------------------------------------------------+
1 row in set (0.000 sec)

MariaDB [wordpress]>
```

試しにこの記事のURLにパッチをあててみます。

```
MariaDB [(none)]> use wordpress;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [wordpress]> update wp_2_posts set post_name = 'passwordmaster3-311-leopard' where ID=300;
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [wordpress]> update wp_2_posts set guid = 'http://192.168.0.224/today/2007/10/31/passwordmaster3-311-leopard/' where ID=300;
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [wordpress]> select ID,post_name,guid from wp_2_posts where ID = 300;
+-----+-----------------------------+---------------------------------------------------------------------+
| ID  | post_name                   | guid                                                                |
+-----+-----------------------------+---------------------------------------------------------------------+
| 300 | passwordmaster3-311-leopard | http://192.168.0.224/today/2007/10/31/passwordmaster3-311-leopard/ |
+-----+-----------------------------+---------------------------------------------------------------------+
1 row in set (0.001 sec)

MariaDB [wordpress]>
```

これで記事のURLに含まれたアンダーバーをハイフンに置換できました。今回は1件の記事だけにパッチを当てましたが、すべての記事にパッチを当てなければならないので、pythonでプログラムを書きました。

```
#!/usr/bin/python3

import mysql.connector

# データベースの接続情報を設定
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'xxxxxxxxx',
    'database': 'wordpress'
}

# MySQLに接続
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 対象のテーブル名とカラム名を指定
table_name = 'wp_2_posts'
column_name = 'post_name'

# データの取得と変更
query = f"SELECT ID,{column_name} FROM {table_name}"
cursor.execute(query)

for row in cursor.fetchall():
	print(row)
	if '__' not in row[1]:
		# 変更するカラムのデータを取り出しアンダーバーをハイフンに置換する
		updated_value = row[1].replace('_', '-')

		# データの変更があるか？
		if row[1] != updated_value:
			print(row[1])
			print(updated_value)

    	    # Update record
    	    update_query = f"UPDATE {table_name} SET {column_name} = %s WHERE ID = %s"
    	    cursor.execute(update_query, (updated_value, row[0]))

# 変更をコミット
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()
```

このプログラムを実行することで記事中のURLに含まれるアンダーバーはハイフンに置換できました。table\_nameとcolumn\_nameは以下のように指定して都度実行しました。

| **table\_name** | **column\_name** |
| --- | --- |
| wp\_2\_posts | post\_name |
| wp\_2\_posts | guid |
| wp\_2\_terms | slug |

## カテゴリURLのリダイレクト対応

次にわかった問題はカテゴリのURLの違いです。旧サイトではトップの直下にカテゴリができています。

```
https://kanpapa.com/today/robot/mini-pupper-2/
```

WordPressでは以下のようにトップディレクトリの直下にcategoryがあり、その配下にカテゴリが配置されます。

```
https://192.168.0.224/today/category/robot/mini-pupper-2
```

旧サイトのURLにアクセスがあったら、新サイトのURLにリダイレクトしてあげれば良さそうです。リダイレクトを行ってくれるプラグインRedirectionで旧URLから新URLへのリダイレクトを行いました。今回の場合は以下のように設定しています。

| **ソース URL** | ^/today/robot/(.\*) | 正規表現、スラッシュ無視、大文字小文字の区別なし |
| --- | --- | --- |
| **ターゲット URL** | /today/category/robot/$1 |  |
| **グループ** | 転送ルール |  |

他の旧URLでも必要に応じてこのプラグインでリダイレクトを行っています。

## 残りは手修正で

ここまでの作業でほぼコンテンツにはアクセスできるようになりましたが、アイキャッチ画像の設定やカテゴリの見直しなど、まだ終わっていないところがあります。直近2年分については修正が完了していますので、残りのコンテンツは時間を見つけて修正を進めていきます。
