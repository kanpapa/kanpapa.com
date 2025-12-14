---
title: "新しいConoHaサーバに移行しました"
date: 2020-05-06
categories: 
  - "server"
tags: 
  - "conoha"
coverImage: "tlstestpage.jpg"
---

このサイトが稼働しているサーバを新しいサーバに移行しました。

これまではCentOS 7でしたが、現在はCentOS 8.1で稼働中です。

CentOS 7とCentOS 8.1で変わった点をあげると以下のようなところです。

- Python3ベースに

- TLS1.3に対応

- yumがdnfに

- NTPはchronyに

- iptablesもfirewalldに

移行中にPerlモジュールのTask::Plackがうまくインストールできずにforceモードでインストールしてしまいました。他は大きな問題はなかったです。

この移行で最新の[TLS1.3](https://knowledge.sakura.ad.jp/21470/)が使えるようになり、SSL Server TestでもランクAになりました。

![tlstestpage.jpg](images/tlstestpage.jpg)

昨日の時点でIPアドレスを切り替えましたが、旧サーバーへのアクセスがなくなるまでしばらく並行稼働し、今日の時点で旧サーバへのアクセスがほぼ無くなったので、本日旧サーバーのWebサーバ（nginx）を停止しました。

```
$ sudo systemctl stop nginx$ dateWed May 6 17:17:33 JST 2020$
```

今のところ特に問題なさそうなので、旧サーバーのVPSもシャットダウンしました。

![vps_shutdown.jpg](images/vps_shutdown.jpg)

何か忘れ物があるかもしれないので、しばらくしてから削除します。

旧サーバーのVPSを作成したのは2016-08-03 22:32:18なので、約4年間の稼働でした。お疲れさまでした。
