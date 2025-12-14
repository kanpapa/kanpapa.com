---
title: "Swiperを使ってCOSMAC研究会のトップページの画像をスライド表示にしてみました。"
date: 2020-05-31
categories: 
  - "server"
tags: 
  - "movable-type"
coverImage: "cosmac_lab_swiper.jpg"
---

[COSMAC研究会](https://kanpapa.com/cosmac/ "COSMAC研究会")のトップページの画像がずっと同じままだったのですが、最近のCOSMAC VIPの画像も一緒に表示したいなということでスライダーを使って画像を表示するようにしてみました。なお、MovableTypeのテーマは「Eiger 1.6」を使用しています。

![cosmac_lab_swiper.jpg](images/cosmac_lab_swiper.jpg)

今回はスライダーはSwiperを使ってみました。GitHubに最新版が登録されていますのでこれを使います。

- [Swiper - The Most Moden Mobile Touch Slider](https://swiperjs.com/ "Swiper - The Most Moden Mobile Touch Slider")

この手のスライダーアプリはjQueryのようなJavaScriptライブラリが必要な場合が多いのですが、このSwiperは単体で動作するため、既存のMovableTypeの環境にも影響を与えないだろうということで使ってみました。

### Swiperのダウンロード

今回はswiper-5.4.1を使用しました。公式サイトからダウンロードしたZIPファイルを展開すると、多数のファイルが含まれていますが、サイトに組み込むのは以下の２つのファイルです。

- swiper-5.4.1/package/css/swiper.min.css

- swiper-5.4.1/package/js/swiper.min.js

### Swiperのcssとjsの設置

COSMAC研究会のサイトはMovableTypeを使用していますので、以下のように設置しました。

デザイン→テンプレート→インデックステンプレートで以下の２つのインデックステンプレートを作成します。

- テンプレート名：swiper.min.css

- テンプレートの内容：swiper.min.cssをそのままコピペ

- 出力ファイル名：swiper.min.css

- テンプレートの種類：スタイルシート(styles)

- 公開：スタティック(既定)

- テンプレート名：swiper.min.js

- テンプレートの内容：swiper.min.jsをそのままコピペ

- 出力ファイル名：swiper.min.js

- テンプレートの種類：JavaScript(javascript)

- 公開：スタティック(既定)

これで保存と再構築を行えば、swiperのcssとjsが設置されます。

### インデックスページ(index.html)の修正

(1) インデックスページにSwiperのファイルを組み込みます。の直前にswiper.min.cssを配置します。

```
  <link rel="stylesheet" href="swiper.min.css">
</head>
```

(2) 最初に組み込まれている「メインイメージ」のモジュールを「メインスライド」に書き換えます。この「メインスライド」モジュールは後で登録します。

(変更前)

```
 </header>
 <mt:Include module="メインイメージ">
 <div class="content">
```

(変更後)

```
 </header>
 <mt:Include module="メインスライド">
 <div class="content">
```

(3) の直前に以下の記述を追加します。細かいパラメタの内容は公式サイトでご確認ください。

```
  <script src="swiper.min.js"></script>
  <script>
     var swiper = new Swiper('.swiper-container', {
       navigation: {
         nextEl: '.swiper-button-next',
         prevEl: '.swiper-button-prev',
       },
       loop: true,
       autoplay: {
         delay: 3000,
         disableOnInteraction: true
       },
       pagination: {
         el: '.swiper-pagination',
         type: 'bullets',
         clickable: true,
       }
     });
   </script>
```

### スタイルシート(style.css)の設定

既存のスタイルシート(style.css)にSwiperの表示領域の大きさを示すクラス属性を追加します。私の場合は以下を追加しました。

```
.swiper-container {
width: 600px;
height: 300px;
}
```

### メインスライドモジュールの作成

デザイン→テンプレート→テンプレートモジュールで、新規モジュールを作成します。

- テンプレート名：メインスライド

- モジュール本体：

```
<div id="mainimage">
 <!-- Slider main container -->
 <div class="swiper-container">
 <!-- Additional required wrapper -->
 <div class="swiper-wrapper">
 <!-- Slides -->
 <div class="swiper-slide">
<mt:Assets type="image" tag="@SITE_SLIDE_IMAGE1" limit="1">
 <img src="<$mt:AssetThumbnailURL encode_html="1">">
</mt:Assets>
 </div>
 <div class="swiper-slide">
<mt:Assets type="image" tag="@SITE_SLIDE_IMAGE2" limit="1">
 <img src="<$mt:AssetThumbnailURL encode_html="1">">
</mt:Assets>
 </div>
 <div class="swiper-slide">
<mt:Assets type="image" tag="@SITE_SLIDE_IMAGE3" limit="1">
 <img src="<$mt:AssetThumbnailURL encode_html="1">">
</mt:Assets>
 </div>
 <div class="swiper-slide">
<mt:Assets type="image" tag="@SITE_SLIDE_IMAGE4" limit="1">
 <img src="<$mt:AssetThumbnailURL encode_html="1">">
</mt:Assets>
 </div>
 </div>
 
 <!-- If we need pagination -->
 <div class="swiper-pagination"></div>

<!-- If we need navigation buttons -->
 <div class="swiper-button-prev"></div>
 <div class="swiper-button-next"></div>

<!-- If we need scrollbar -->
 <div class="swiper-scrollbar"></div>
 </div>
</div>
```

### スライド表示する画像の指定

スライダーで表示したいアセット画像に@SITE\_SLIDE\_IMAGE1～4のタグをつけると、その画像がスライダーで表示されます。

### 動作確認

組み込んだサイトにアクセスして表示を確認します。

### 終わりに

MovableTypeは初心者なので、もっと良い組み込みかたがあると思いますが、一応これで動きましたという記録になります。
