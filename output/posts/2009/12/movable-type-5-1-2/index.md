---
title: "Movable Type 5 移行に向けての重大な問題"
date: 2009-12-01
categories: 
  - "server"
tags: 
  - "movable-type"
  - "mysql"
---

そろそろMovable Type 5にアップグレードしようかなと、ドキュメントを読んで、サーバの設定に取りかかったところ、重大な問題を発見してしまいました。 なんと、今使っているDBはMySQL 4.0だったのです。Movable Type 5はMySQL 5.0が必須とのことで、私が使っているサイトはMySQL 4.0からMySQL 5.0に切り替えるにはデータベースを一旦削除しなければならないようです。 これはちと怖いとはいえ、おもしろくなってまいりました。
