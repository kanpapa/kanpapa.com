---
title: "Movable Type 4.25にアップグレードしました"
date: 2009-04-01
slug: "movable-type-425"
categories: 
  - "server"
---

いろいろと新機能が追加されているようです。 これから試してみます。 アップグレードはいつもの方法で問題なかったです。 $ unzip MT-4\_25-ja.zip $ cd www $ cd mt $ cp mt-config.cgi ~/MT-4.25-ja/. $ cd plugins/ $ cp -rp iMT ~/MT-4.25-ja/plugins/. $ cp HatenaAuth.pl ~/MT-4.25-ja/plugins/. $ cd ../mt-static/plugins/ $ cp -rp iMT ~/MT-4.25-ja/mt-static/plugins/. $ cd ~/www $ mv mt mt.old $ mv ~/MT-4.25-ja/ ~/www/mt $ mv mt.old ~/mt.old.20090401 あとは、ダッシュボードにアクセスすると、自動的にアップグレードが始まります。 無事4.25に更新が完了しました。
