---
title: "LiDARが壊れました"
date: 2022-07-19
categories: 
  - "robot"
tags: 
  - "roomba"
coverImage: "slamtec_rplidar_a1m8_z.jpg"
---

最近はROS2でルンバを自律走行させるべく実験をしていますが、急にLiDARのデータが取れなくなりました。

![slamtec_rplidar_a1m8_z.jpg](images/slamtec_rplidar_a1m8_z.jpg) <!--more-->

おかしいなとWindows版のビューワーで確認したところ、なぜかデータが一か所しか取れていません。本来だと360度周囲の情報が取れるのですが。

![slamtec_rplidar_a1m8_win.png](images/slamtec_rplidar_a1m8_win.png)

いろいろいじったのですが状態に変化はありませんでした。やはりモーターで高速回転をしているため振動や衝撃などで壊れやすいのでしょう。

ただ、このLiDARのおかげでROSの入門から自律走行まで楽しむことができました。お疲れさまでした。
