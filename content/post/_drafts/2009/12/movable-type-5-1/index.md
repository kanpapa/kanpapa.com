---
title: "Movable Type 5への移行を断念"
date: 2009-12-12
slug: "movable-type-5-1"
tags: 
  - "mysql"
draft: true
---

MySQLをバージョンアップして苦労してMovable Type 5に移行しましたが、再構築で「Wide character in subroutine entry」のエラーがどうしても直らないので、残念ながらMovable Type 4に戻すことにしました。

ブログによっては再構築のエラーにならないものもあるので、私のコンテンツの問題なのだとは思いますが、エラーの原因箇所がよくわからずお手上げの状態です。エラーのときはもう少し役に立つエラーメッセージを残してほしいものです。

  

Movable Type 4への戻しは以下のように行いました。

  

1. Movable Type 5に移行してから書いたブログをエクスポートしておく。
2. Movable Type 5のシステムをすっぱり削除
3. MySQLのDBも一旦削除し、空のDBを作っておく
4. Movable Type 4をインストールし、初期設定をおこなう。My First blogができる。
5. Movable Type 4の最終バックアップから復元を行う。importに展開して、復元で読み込み。
6. Movable Type 4の再構築ができることを確認。ようやく再構築できた
7. 必要なプラグインを再度インストール
8. Movable Type 5にしてから書いたブログ記事だけをインポート
9. いろいろ微調整
10. 復旧完了！

本当にバックアップは重要ですね。つくづくそう思いました。
