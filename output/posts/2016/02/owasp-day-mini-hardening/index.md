---
title: "OWASP DAYのMini Hardeningに参加してみた"
date: 2016-02-28
categories: 
  - "security"
coverImage: "mini_hardening.png"
---

OWASP DAY in TOKYO 2016 Spring!!でMini Hardeningがあるということで申し込みをしたところ、運良く参加することができました。

![mini_hardening.png](images/mini_hardening.png) <!--more-->

#### 前日にトラブル発生

事前準備として会場にインターネット環境は無く、WiFiの輻輳を避けるために、USBテザリングでインターネットに接続してほしいとのことでした。

前日の夜にMacBook AirにNexus5xを接続しUSBテザリングの確認をしたところ、NoRNDISがEl Capitanだと動かないことが判明しました。やむなくYosemiteにダウングレードを始め、当日の９時ぐらいにようやくUSBテザリングできるようになりました。これには焦りました。

#### Mini Hardeningの環境にアクセス

同じチームだった方が詳細をまとめているので細かい点はこちらに譲ります。さすがよくまとまっています。

[OWASP DAY 2016 Spring MINI Hardening writeup(?)](http://yuta1024.hateblo.jp/entry/2016/02/28/000112 "OWASP DAY 2016 Spring MINI Hardening writeup(?)")

システム構成はこんな感じでした。

![network_minihard.png](images/network_minihard.png)

まず踏み台サーバーにログイン。

```
Kanpapa-no-iMac:~ kanpapa$ ssh -iteam.pem ec2-user@XX.XX.XX.XXX
:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'team.pem' are too open.
　：
bad permissions: ignore key: team.pem
Permission denied (publickey).
$

```

ありゃ、パーミッションが未設定だ。パーミッションを直して再びトライ。

```
Kanpapa-no-iMac:~ kanpapa$ chmod 400 team.pem
Kanpapa-no-iMac:~ kanpapa$ ssh -iteam.pem ec2-user@XX.XX.XX.XXX
:
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$

```

ようやく踏み台にログインできました。ここから、目的のサーバにログイン。

```
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ ssh unyou@i-lamp.hardmini.local
unyou@i-lamp.hardmini.local's password:
Last login: Sat Feb 27 14:02:40 2016 from 172.31.109.30
-bash-4.1$

```

ログインできました。

#### システムのログを確認する

まずログイン履歴を見たところ、vnyouとかマニュアルに無いアカウントがあります。これは怪しい。

```
-bash-4.1$ last
unyou    pts/2        172.31.109.30    Sat Feb 27 14:05   still logged in
unyou    pts/1        172.31.109.30    Sat Feb 27 14:03   still logged in
unyou    pts/0        172.31.109.30    Sat Feb 27 14:02   still logged in
hardmini pts/0        172.31.23.210    Sat Feb 27 12:15 - 12:15  (00:00)
hardmini pts/0        172.31.19.198    Sat Feb 27 11:39 - 11:39  (00:00)
reboot   system boot  2.6.32-431.29.2. Sat Feb 27 11:37 - 14:09  (02:32)
vnyou    pts/0        172.31.13.204    Fri May 22 23:34 - 23:36  (00:01)
vnyou    pts/0        172.31.13.204    Fri May 22 23:29 - 23:30  (00:00)
ken      pts/0        172.31.13.204    Fri May 22 23:28 - 23:29  (00:01)
wwwadmin pts/0        172.31.13.204    Fri May 22 23:27 - 23:28  (00:00)
hardmini pts/0        172.31.23.211    Fri May 22 22:37 - 22:37  (00:00)
hardmini pts/0        172.31.23.211    Thu May 21 01:42 - 01:53  (00:10)
hardmini pts/0        172.31.23.211    Mon May 18 02:00 - 02:44  (00:44)
reboot   system boot  2.6.32-431.29.2. Sun May 17 22:43 - 23:58 (5+01:14)

```

また、/var/logをみたところ、secureログがやたら大きいようにみえます。これも怪しい。

```
-rw------- 1 root  root     36369  2月 27 14:05 2016 secure
-rw-------. 1 root  root  55983044  3月  1 12:02 2015 secure-20150301
-rw-------. 1 root  root  55538852  5月 18 02:44 2015 secure-20150518
-rw------- 1 root  root    908366  2月 27 12:17 2016 secure-20160227

```

といろいろ気付く点はありましたが、私以外のメンバーがいち早くこれらを見つけて穴を塞いでいったため残念ながらお役に立てませんでした。

#### ポートフォワードでWebページを監視

サービス監視としてWordPressのWebサイトが正常に動作しているかを確認したかったので、ポートフォワードでWebページを確認しました。

URLは、http://team-i.hardmini.local/wp/wordpress/ とのことなので、ローカルのMacの/etc/hostsに以下のように追加しました。

```
# for Mini Hardening
127.0.0.1	team-i.hardmini.local

```

次にMacでターミナルをもう１画面立ち上げて、ポートフォワードの設定を行いました。

```
Kanpapa-no-iMac:~ kanpapa$ sudo ssh xxx.xxx.xxx.xxx(踏み台のIP) -l ec2-user(踏み台のuser) -i team.pem -L 80:172.31.109.20(WWWサーバのIP):80
Password: xxxxxxxxx
Last login: Sat Feb 27 05:24:39 2016 from .....
:
[ec2-user@ip-YYY-YYY-YYY-YYY ~]$

```

この状態で、MacのWebブラウザから、http://team-i.hardmini.local/wp/wordpress/ にアクセスすることで、WordPressのページを見ることができました。時々このページをアクセスすることで正常にサイトが動いていることを確認しま した。

![hardening_webpage.png](images/hardening_webpage.png)

#### どうしてもFTPが動作しない

残るFTPがどうしても動きません。実は最近はFTPは使ったことがなく、いつもscpを使っています。他のメンバーも同じ状況でした。ここが動けばオールブルーにできたのですが。結局時間切れでした。

#### 実際に経験した感想

今回はMini Hardeningで競技時間も１時間しかなく、とにかく穴を塞ぐ作業に終始しました。

運営側がわざとログを残してくれたおかげで、痕跡から追いやすかったですが、サービスの稼働状況に関わらず、怪しいところはどんどん閉じたり、怪しいファイルも即刻削除とワイルドな対応になりました。本来であれば、どのようなインシデントが起こったかの情報の保全が必要でしょう。

実際の商用サービスでプロの侵入者が同様なことを行ったとしたら、ログなどの痕跡も綺麗に消すでしょうし、今回のようなワイルドな対応ではサービスに影響がでる可能性もあり、状況把握と分析に膨大な時間がかかると思われます。ログを他のサーバでも保管しておくなどの事前対策の重要性を実感することができました。

また機会がありましたら参加してみたいですが、画面サイズはMacBook Airでは狭いかもしれません。MacBook Proが欲しいなぁ。
