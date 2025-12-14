---
title: "Logwatchの仕様変更からWebサーバへの攻撃増加を知る"
date: 2020-12-19
categories: 
  - "security"
coverImage: "logwatch_report.png"
---

現在このWebサーバをCentOS 8.1からUbuntu 20.04へ移行中です。

サーバの設定もほぼ完了したのでlogwatchというログを監査するパッケージを入れました。

![logwatch_report.png](images/logwatch_report.png)

CentOS 8.1ではLogwatch 7.4.3 (04/27/16)を使っていました。毎日、Webサーバーのログを解析して、次のようにWebサーバのエラーレスポンスコードがレポートされるようになっていました。

```
Requests with error response codes   400 Bad Request      null: 12 Time(s)      /: 1 Time(s)　　：
```

このレポートをみると、外部からどのようなWebアクセス試行（攻撃？）があるのかがわかります。

Ubuntu 20.04ではLogwatch 7.5.2 (07/22/19)にバージョンがあがったためか、これまでのようなエラーレスポンスコードがレポートされなくなってしまいました。

Logwatchのソースをみたところ、HTTPのエラーレスポンスコードを表示する処理が変更されていて、詳細レベルがLow($detail=0)の場合はこの処理がスキップされるようになっていました。

```
##  List error response codes#if (keys %needs_exam and ($detail or $a5xx_resp)) {   print "\nRequests with error response codes\n";      :
```

CentOS 8.1の古いLogwatch 7.4.3ではこのチェックがないので常にレポートされます。

```
##  List error response codes#if (keys %needs_exam) {   print "\nRequests with error response codes\n";      :
```

logwatch.confで詳細レベルをHighやMidに設定することで、以前と同様なエラーレポートが出力され問題は解決したのですが、2016年の時点では許容できていたアクセス試行の回数が、2019年では許容できる量を超えてしまい、Lowでは表示しないように仕様が変更されてしまったわけです。

インターネットに公開されているWebサーバに対する攻撃が増加しているのが、このようなところからも読み取れます。
