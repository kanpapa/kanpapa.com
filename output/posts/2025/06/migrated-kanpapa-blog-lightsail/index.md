---
title: "ブログサイトをAmazon Lightsailに移行しました"
date: 2025-06-17
categories: 
  - "server"
tags: 
  - "aws"
  - "conoha"
  - "lightsail"
  - "wordpress"
coverImage: "amazon-lightsail-topview1.png"
---

久しぶりにブログサイトを移行しました。移行先はAmazon LightsailというVPSです。

https://kanpapa.com

## サイト移行による変更点

今回のサイト移行による変更点は以下の通りです。

|  | 旧サイト | 新サイト |
| --- | --- | --- |
| クラウド基盤 | [ConoHa VPS](https://www.conoha.jp/vps/) (1GB RAM, 2 vCPU, 100GB SSD, 転送量無制限) | [Amazon Lightsail](https://aws.amazon.com/jp/lightsail/) (1GB RAM, 2 vCPU, 40GB SSD, 転送量2TBまで) |
| CMS | WordPress (自前で構築) | WordPress 6.8.1 (bitnami) |
| Webサーバ | Nginx | Apache 8.2.28 (bitnami) |
| WordPress構成 | マルチサイト | シングルサイト |
| サーバー監視 | [mackerel](https://mackerel.io/) | [Amazon Cloudwatch](https://aws.amazon.com/jp/cloudwatch/) |
| 課題と解決案 | 旧CMSの名残の大量のカテゴリと不要なコンテンツで管理に課題 | カテゴリを減らし、タグを活用。不要なコンテンツは整理して一掃 |

CMSはWordPressのままで変わりないのですが、違うプラットフォームも使ってみたかったので、ConoHa VPSからAWS Lightsailに変更しています。この機会に旧CMSで使用していた不要なコンテンツを一掃し、マルチサイトだったものをシングルサイトに統合しています。これに伴いURLが変更になっていますが、適切なリダイレクトを設定してリンク切れにならないようにしています。

まだログを見ながら調整している状態ですので、一部おかしいところがあるかもしれませんが、その点はご了承ください。

## コストと使い勝手を見極めたい

現時点ではAmazon Lightsailの90日間の無料使用枠で稼働していますが、90日間でしっかり評価して継続かConoHaに戻るかを見極めたいと思います。価格面ではConoHaが有利ですが、コンソール機能など管理機能のレスポンスはLightsailが良さそうな感じです。

## github.ioもお試し中

なお、静的サイトである[COSMAC研究会](https://kanpapa.github.io/cosmac-lab)のサイトはgithub.ioに移行しています。こちらは[Hugo](https://gohugo.io/)でジェネレートしているのですが、こちらのサイトもいろいろお試し中です。

https://kanpapa.github.io/cosmac-lab
