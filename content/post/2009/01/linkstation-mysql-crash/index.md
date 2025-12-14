---
title: "LinkStationのDebianでMySQLがクラッシュする"
date: 2009-01-20
slug: "linkstation-mysql-crash"
categories: 
  - "server"
tags: 
  - "debian"
  - "linkstation"
  - "movable-type"
  - "mysql"
  - "玄箱"
---

LinkStationにhackkitでdebian(etch)をインストールしていますが、これにMovable Typeのオープンソース版をインストールしてみました。

セットアップは問題なくできたのですが、使っていると突然「エラーが発生しました」と表示されます。どうやらMySQLと通信できないときがあるようです。

Connection error: Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (111)

![linkstation_mysql_crash_20090121082811.jpg](images/linkstation_mysql_crash_20090121082811.jpg)

おかしいなぁとsyslogをみたところ、見事にMySQLが落ちてました。

```
Jan 20 20:55:56 hackkit mysqld[1291]: mysqld got signal 11;
Jan 20 20:55:56 hackkit mysqld[1291]: This could be because you hit a bug. It is also possible that this binary?
Jan 20 20:55:56 hackkit mysqld[1291]: or one of the libraries it was linked against is corrupt, improperly built,
Jan 20 20:55:56 hackkit mysqld[1291]: or misconfigured. This error can also be caused by malfunctioning hardware.
Jan 20 20:55:56 hackkit mysqld[1291]: We will try our best to scrape up some info that will hopefully help diagnose
Jan 20 20:55:56 hackkit mysqld[1291]: the problem, but since we have already crashed, something is definitely wrong
Jan 20 20:55:56 hackkit mysqld[1291]: and this may fail.
Jan 20 20:55:56 hackkit mysqld[1291]:?
Jan 20 20:55:56 hackkit mysqld[1291]: key_buffer_size=16777216
Jan 20 20:55:56 hackkit mysqld[1291]: read_buffer_size=131072
Jan 20 20:55:56 hackkit mysqld[1291]: max_used_connections=1
Jan 20 20:55:56 hackkit mysqld[1291]: max_connections=100
Jan 20 20:55:56 hackkit mysqld[1291]: threads_connected=1
Jan 20 20:55:56 hackkit mysqld[1291]: It is possible that mysqld could use up to?
Jan 20 20:55:56 hackkit mysqld[1291]: key_buffer_size + (read_buffer_size + sort_buffer_size)*max_connections = 233983 K
Jan 20 20:55:56 hackkit mysqld[1291]: bytes of memory
Jan 20 20:55:56 hackkit mysqld[1291]: Hope that's ok; if not, decrease some variables in the equation.
Jan 20 20:55:56 hackkit mysqld[1291]:?

```

メモリが少ないからかなぁと、max\_connectionsを100から10にしてみましたけど、状況は変わらず。なんだろなぁ〜。

でも、LS-HGLでのMovable Type 4は結構重くて実用にはならないかもという感触でした。ちゃんと動くようになれば少しは速くなるかな？
