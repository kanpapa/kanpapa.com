---
title: "Movable Type 4.26にアップグレードしました"
date: 2009-06-17
slug: "movable-type-426"
categories: 
  - "server"
tags: 
  - "movable-type"
---

アップグレードはいつもの方法で問題なかったです。

```
$ unzip MT-4_26-ja.zip
$ cd www
$ cd mt
$ cp mt-config.cgi ~/MT-4.26-ja/.
$ cd plugins/
$ cp -rp iMT ~/MT-4.26-ja/plugins/.
$ cd ../mt-static/plugins/
$ cp -rp iMT ~/MT-4.26-ja/mt-static/plugins/.
$ cd ~/www
$ mv mt mt.old
$ mv ~/MT-4.26-ja/ ~/www/mt
$ mv mt.old ~/mt.old.20090618
```

あとは、ダッシュボードにアクセスすると、自動的にアップグレードが始まります。  
無事4.26に更新が完了しました。
