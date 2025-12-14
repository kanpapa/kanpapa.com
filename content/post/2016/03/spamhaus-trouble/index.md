---
title: "Spamhausのブロックリストに誤登録されて困ってしまった"
date: 2016-03-01
slug: "spamhaus-trouble"
categories: 
  - "server"
image: "images/kanpapa_twieet.png"
---

私はこのサイト（kanpapa.com）を[ConoHa VPS](https://www.conoha.jp/ "https://www.conoha.jp/")で運用しています。

VPSの状況を監視するために、Logwatchというログ監視プログラムを動かしています。このプログラムから毎日メールが届くのですが、ある日突然、このメールが届かなくなりました。

おかしいなと/var/log/maillogを確認したところ、以下のようなログが残っていました。

```
Mail from IP 133.130.113.XX was rejected due to listing in Spamhaus SBL. For details please see http://www.spamhaus.org/query/bl?ip=133.130.113.XX....

```

どうやら[Spamhaus](https://www.spamhaus.org/ "spamhaus")のSBL（Spamhaus Block List）にkanpapa.comが使っているConoHa VPSのIPレンジが登録されてしまったようなのです。

<!--more-->

つまり、このVPSが何らかの原因でSPAMサーバと間違われて、送信先のメールサーバが受信を拒否してしまったのです。

しばらくすれば解除されるかなと甘く見ていたのですが、なかなか解除されません。

やむなく、応急措置として以前試用していたGoogle Apps for Workを復活し、MXをそちらに向けることで、kanpapa.comのメールを使えるようにしました。

そうこうしているうちにSBLからは削除されました。

そしてしばらく経ち、先日、OWASP JAPANのHardeningに参加したので、そのレポートをブログを書いて、TwitterでURLを流そうとしたところ、どうしてもツイートできません。いろいろ試してみると以下のように kanpapa.com のドメインを書くとツイートできないことがわかりました。

![kanpapa_twieet.png](images/kanpapa_twieet.png)

もしかしてとSpamhausでドメインを確認したところ、

```
kanpapa.com is listed in the DBL

```

今度はドメイン名がDBL（Domain Block List）に登録されてしまったようです。この情報をTwitterが参照し、ドメインが含まれたツイートをブロックしているのではと思われます。

これでは非常に困るので、Spamhausの[Blocklist Removal Center](https://www.spamhaus.org/lookup/ "Blocklist Removal Center")からDBLからの削除をお願いしました。

フォームからカタコトの英語で入力すると、受け付けましたというメールが届きました。

DBLからの削除の対応は思ったよりも早く２時間後に以下のようなメールが到着しました。

```
Hello,
We have looked at the data for your domain and have reset the reputation
score for the domain. As a result, it is no longer listed in DBL.
To prevent future issues please read our FAQ about DBL listings:
http://www.spamhaus.org/faq/section/Spamhaus%20DBL#371
Regards,
--
The Spamhaus Project - DBL Team

```

このメールが届いてしばらくしたらTwitterにツイートできるようになりました。

しかし、えらい迷惑ですね・・。こういう間違いは。
