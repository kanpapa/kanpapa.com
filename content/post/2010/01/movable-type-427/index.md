---
title: "Movable Type 4.27にアップグレードしました"
date: 2010-01-08
slug: "movable-type-427"
categories: 
  - "server"
---

Movable Type 4.27 の出荷が開始されましたので、アップグレードしました。 Movable Type 5.01 も出荷されていますが、とりあえずは現状のものをアップグレードということで。 アップグレードはいつもの方法で問題なかったです。 $ unzip MT-4\_27-ja.zip $ cd www $ cd mt $ cp mt-config.cgi ~/MT-4.27-ja/. $ cd plugins/ $ cp -rp iMT ~/MT-4.27-ja/plugins/. $ cp -rp PostToTwitter ~/MT-4.27-ja/plugins/. $ cd ../mt-static/plugins/ $ cp -rp iMT ~/MT-4.27-ja/mt-static/plugins/. $ cd ~/www $ mv mt mt.old $ mv ~/MT-4.27-ja/ ~/www/mt $ mv mt.old ~/mt.old.20100109 あとは、ダッシュボードにアクセスすると、自動的にアップグレードが始まります。 無事4.27に更新が完了しました。
