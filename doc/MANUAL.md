# kanpapa.com（Hugo）記事作成マニュアル

新サイト（Hugo + GitHub Pages）における記事の作成から公開までの手順書です。

## 0. 準備
作業を開始する前に、必ずローカルリポジトリを最新の状態にします。

```bash
# リポジトリのディレクトリへ移動（パスは環境に合わせて変更してください）
cd ~/kanpapa.com

# リモートの変更を取り込む
git pull origin main
```

## 1. 記事ファイルの作成
Hugoのコマンドを使用して、記事の雛形（Markdownファイル）を生成します。

```bash
# 書式: hugo new content post/[ディレクトリ名]/index.md
# 例:
hugo new content post/my-new-article/index.md
```

Note: ディレクトリ名はそのままURLの一部（スラッグ）になります。日本語のディレクトリ名は避け、英数字（ハイフン区切り）を設定します。

## 2. 記事の執筆・編集
生成された .md ファイルをテキストエディタ（VS Codeなど）で開きます。 ファイルの先頭には Front Matter（設定領域）がテンプレートarchetypes/post.mdで設定されているので、適切な内容に編集し、その下に本文をMarkdownで記述します。

```Markdown
+++
date = '2025-12-29T11:28:12+09:00'
title = '投稿テスト7'
slug = 'test7'
image = 'test7.jpg'
categories = ["electronics", "retrocomputing"]
tags = ["arduino", "esp32"]
draft = true
+++

（ここから本文をMarkdownで記述）

## 見出し
本文テキスト...
```
* draft: true のままだと下書き扱いとなり、本番サイトには表示されません。
* image: 記事一覧やSNSシェア時に表示されるサムネイル画像を指定します。

## 3. 画像の挿入
画像の管理方法は構成により異なりますが、基本的には以下のいずれかになります。

本サイトではPage Bundleを基本形とします。

* Page Bundle（記事フォルダ）利用の場合:
  * 画像配置場所: .md ファイルと同じディレクトリ
  * Markdown記述: `![説明](gazou.jpg)`

* staticフォルダ利用の場合:

  * 画像配置場所: static/images/gazou.jpg
  * Markdown記述: `![説明](/images/gazou.jpg)`

* 画像サイズが小さい場合:

  * 画像サイズが小さいと拡大表示をしようとしてぼんやりした画像になることがあります。その場合は以下で画像を挿入すると改善されます。
  * Markdown記述: `{{< figure src="gazou.png" width="467px" height="285px" caption="説明">}}`

## 4. YouTube動画の埋め込み
Hugo標準のショートコードを使用することで、簡単にYouTube動画を埋め込むことができます。
HTMLのiframeタグを直接書くよりも、スマホ表示などで崩れにくいため推奨されます。

### 書式
`{{< youtube [動画ID] >}}`

### 動画IDとは？
YouTubeのURLが `https://www.youtube.com/watch?v=AbCdEfGhIjK` の場合、
`v=` の後ろにある `AbCdEfGhIjK` の部分が動画IDです。

### 記述例
```markdown
動画での動作デモです。

{{< youtube AbCdEfGhIjK >}}
```

## 5. ローカルでのプレビュー
記事を書いている途中で、実際の表示を確認します。

```Bash
# -D オプションで下書き(draft: true)も含めて表示
hugo server -D
```

* ブラウザで http://localhost:1313 にアクセスして確認します。

* 確認終了時はターミナルで Ctrl + C を押してサーバーを停止します。

## 6. 公開（デプロイ）
記事が完成したら、以下の手順で公開します。

1. 下書きの解除: 記事ファイル内の draft: true を draft: false に変更します。

1. Gitへのプッシュ: 変更をコミットし、GitHubへプッシュします。

```Bash
git add .
git commit -m "Add new article: [記事タイトル]"
git push origin main
```

GitHub Actionsが設定されていので、プッシュから数分後に自動的に本番サイト（kanpapa.com）へ反映されます。

## Tips
* 抜粋（Excerpt）の指定: 記事一覧に表示される要約文を明示的に区切りたい場合は、本文中に `` を挿入してください。

* URL確認: プレビュー時にURL構造が意図通りか確認することをお勧めします。
