---
title: "WordPressからGitHub Pages(Hugo)への移行を行いました"
date: '2025-12-15T17:25:45+09:00'
slug: migration-to-hugo
description: "Geminiのおかげでたった2日間で2000件の記事を持つWordPressからHugoへ移行が完了しました"
categories:
    - "Server"
tags:
    - "Hugo"
    - "WordPress"
    - "Migration"
    - "GitHub Pages"
image: "migration-to-hugo-eyecatch.jpg"
draft: false
---

このブログサイトはAWSの[LightSail](https://docs.aws.amazon.com/ja_jp/lightsail/)でWordPressを動かして運用していました。これによりAWSのいろいろな機能もあわせて体験することができていました。

## 現行サイトの課題

これまでのサイトはAWSのCloudwatchなどで負荷やディスク容量を監視していますが、数日に何回かCPUとネットワークの負荷が上昇し、アラートが飛んできます。多分クロールやログイン試行といった事象でアクセスが急増するのが原因のようです。

最低限のスペックで動かしているため止むを得ないのですが、以前のMovableTypeのときはジェネレートに時間はかかるものの、通常時は軽量だったことを思い出しました。

また、最近の円安が少し気になってきました。AWSの利用料金は当然ドル建てですので今後がやや不安です。

## 静的Webサイトへの移行

これらの課題やそろそろ新しい環境も試したいということで、以前少し試した[Hugo](https://gohugo.io/)を使った静的サイトの運用に移行できないかと考え始めました。

Geminiにこの計画を相談したところ、全く問題なく遂行できそうなので、作業に着手しました。移行先としてはGithub Pagesをおすすめされました。これまでのようにサーバのログを直接確認することができなくなるので、[Google Analytics](https://developers.google.com/analytics?hl=ja)や[Google Search Console](https://search.google.com/search-console/about?hl=ja)などを活用することになります。

## WordPressからHugoへの移行記録（2日間）

たった2日間でLightSail(WordPress)から[GitHub Pages](https://docs.github.com/ja/pages)(Hugo)への移行、そして[Cloudflare](https://www.cloudflare.com/ja-jp/)で管理している独自ドメインの切替までを行うことができました。以下はその作業ログです。

### フェーズ 1：初期構築とコンテンツ移行
| No. | 実施内容 | 詳細 |
| :--- | :--- | :--- |
| 1 | **Hugoプロジェクト構築** | Gitリポジトリ設定、Hugoインストール、テーマ「Stack」の導入。 |
| 2 | **コンテンツインポート** | WordPressからエクスポートした記事をMarkdown形式で配置。 |
| 3 | **サイト構造の整理** | メニュー、Aboutページ、Linksページの整備。不要なタグの一括整理。 |
| 4 | **アセットパス調整** | `baseURL`の設定とfaviconなどのパス修正。 |

### フェーズ 2：機能強化とリダイレクト対策
| No. | 実施内容 | 詳細 |
| :--- | :--- | :--- |
| 5 | **Google Analytics導入** | GA4トラッキングコードの埋め込みと動作確認。 |
| 6 | **フッター自動化** | 著作権表示の年号を自動更新するようにテンプレート調整。 |
| 7 | **リダイレクト設計** | 旧URL構造からの移行計画策定。サブディレクトリ環境での挙動検証。 |
| 8 | **リダイレクト実装** | GitHub Pagesの仕様に合わせ、絶対URLを使用したクライアントサイドリダイレクト（HTML生成）を採用しデプロイ。 |

### フェーズ 3：独自ドメイン移行と仕上げ
| No. | 実施内容 | 詳細 |
| :--- | :--- | :--- |
| 9 | **DNS設定変更** | CloudflareにてAレコード/CNAMEを変更し、GitHub Pagesへ接続。 |
| 10 | **独自ドメイン適用** | `CNAME`ファイル配置、GitHub設定変更。`baseURL`を `https://kanpapa.com/` に最終確定。 |
| 11 | **SEO移行手続き** | [Google Search Console](https://search.google.com/search-console/about?hl=ja)にて新プロパティ登録、サイトマップ送信、アドレス変更申請を実施。 |
| 12 | **旧資産の整理** | 旧WordPressサイトマップの削除と参照停止。完全移行完了。 |


## まとめ

結論としてはGeminiのおかげで昨日と今日の２日間で20年間で2000件近くの記事を持っているWordPressのサイトを無事にGitHub Pagesに移行することができました。

この作業において様々な問題がでてきたのですが、Geminiに確認しながら、必要となったツールも開発してもらい短期間で完了することができました。

２日間の作業記録もGeminiにまとめてもらったものです。移行の妨げとなった問題やどのように対応したのかの詳細についてはまた別の機会にまとめることにします。

移行後のサイトは少し調整中のところもありますが、これは年内目処に修正していきます。この作業もGeminiに協力してもらう予定です。
