---
title: "Movable Type 4.24にアップグレードしました"
date: 2009-02-28
categories: 
  - "server"
tags: 
  - "movable-type"
---

セキュリティアップデートが公開されていましたので、Movable Type 4.24 にアップグレードしました。 手順は前回と同様です。 $ cd ~ $ unzip MT-4\_24-ja.zip $ cd ~/www $ cd mt $ cp mt-config.cgi ~/MT-4.24-ja/. $ cd plugins/ $ cp -rp iMT ~/MT-4.24-ja/plugins/. $ cp HatenaAuth.pl ~/MT-4.24-ja/plugins/. $ cd ../mt-static/plugins/ $ cp -rp iMT ~/MT-4.24-ja/mt-static/plugins/. $ cd ~/www $ mv mt mt.old $ mv ~/MT-4.24-ja/ ~/www/mt $ mv mt.old/ ~/mt.old.20090228 あとは、ダッシュボードにアクセスすると、自動的にアップグレードが始まります。 無事更新が完了しました。
