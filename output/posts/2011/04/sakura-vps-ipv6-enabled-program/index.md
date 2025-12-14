---
title: "さくらのVPSでIPv6 Enabled Programに登録しました"
date: 2011-04-29
categories: 
  - "pc"
---

我が家はYahoo! BB IPv6 トライアルモニターに参加していますので、IPv6でのアクセスができるのですが、このサイトもIPv6対応にしてIPv6で使えるようにしてみました。  
さらに、[IPv6 Enabled Program](http://www.ipv6forum.com/ipv6_enabled/)というものがありましたのでこのサイトを登録しました。  
このサイトのIPv6 対応はさくらで6rdという仕組みがあるので、それを使っています。  
対応方法は以下のページに書かれています。

- [さくらインターネット研究所 6rd設定方法（CentOS5.5編）](http://research.sakura.ad.jp/6rd-trial/6rd-trial-centos55/)

この内容に加えて、/etc/sysconfig/network でIPv6の初期値がnoになっていますので、以下のように修正します。

```
NETWORKING_IPV6=yes
```

この時点でIPv6アドレス指定でアクセスすることができるようになりました。  

```
http://[2001:e41:3b6a:ad76::1]/
```

次にDNSにIPv6用のAAAAレコードを追加します。  
kanpapa.com には AAAAレコードを追加し、v6.kanpapa.comにはAAAAレコードのみを追加してあります。  
変更後にapacheのログを見ながらアクセスしてみましたが、我が家の環境からではkanpapa.comにはIP v4で、v6.kanpapa.comにはIP v6で接続することができました。  
この状態で、IPv6 Enabled Programに登録申請を行います。primaryテストは終わればWWWサイトに張ることができるバッジがもらえます。この時点ではtestingの表示になりますが、数日後にIPv6 Enabledと表示がかわりました。  
これで2011年6月8日の[World IPv6 Day](http://www.attn.jp/worldipv6day/)の対応は完了です。
