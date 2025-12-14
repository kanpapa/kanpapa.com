---
title: "サーバをCentOS 8.1からubuntu 20.04LTSに移行しました。"
date: 2020-12-28
categories: 
  - "pc"
tags: 
  - "linux"
coverImage: "ubuntu20_04_2_lts.png"
---

[CentOS 8が来年末にEOL](https://blog.centos.org/2020/12/future-is-centos-stream/ "CentOS Project shifts focus to CentOS Stream")になるとのことなので、せっかくCentOS 8.1に移行したこのサイトをubuntu 20.04LTSに移行することにしました。

新たにVPSを立てて、ubuntu 20.04LTSをインストールし、比較確認をしながら作業を行いましたが、各種ソフトウェアのコンフィグレーションファイルの位置や設定方法が異なっているので注意が必要です。

新しいサーバで一通り動作を確認して、2020/12/18 21:34にDNSを新サーバに向けました。

今のところは問題なく動作しているようです。Mackerelでモニタリングしていると、メモリの使用量もCentOS 8よりは少ないように見えますが、MovableTypeでの再構築が少し遅くなったように感じます。このあたりは、もう少し様子を見てみたいと思います。

![ubuntu20_04_2_lts.png](images/ubuntu20_04_2_lts.png)
