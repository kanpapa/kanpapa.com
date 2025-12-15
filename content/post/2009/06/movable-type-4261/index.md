---
title: "Movable Type 4.261にアップグレードしました"
date: 2009-06-19
slug: "movable-type-4261"
categories: 
  - "server"
---

このまえアップグレードしたばかりなのに、また更新がありました。

- [Movable Type 4.261 の出荷を開始します](http://www.movabletype.jp/blog/movable_type_4261.html)

バージョンは4.261になります。  
アップグレードはいつもの方法で問題なかったです。

```
$ unzip MT-4_261-ja.zip
$ cd www
$ cd mt
$ cp mt-config.cgi ~/MT-4.261-ja/.
$ cd plugins/
$ cp -rp iMT ~/MT-4.261-ja/plugins/.
$ cd ../mt-static/plugins/
$ cp -rp iMT ~/MT-4.261-ja/mt-static/plugins/.
$ cd ~/www
$ mv mt mt.old
$ mv ~/MT-4.261-ja/ ~/www/mt
$ mv mt.old ~/mt.old.20090619
```

あとは、ダッシュボードにアクセスすると、自動的にアップグレードが始まります。  
無事4.261に更新が完了しました。
