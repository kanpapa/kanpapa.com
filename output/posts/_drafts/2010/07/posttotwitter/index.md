---
title: "PostToTwitterプラグインをインストールしてみた"
date: 2010-07-18
draft: true
---

PostToTwitterプラグイン 2.0.0をインストールしてみました。

うまく動くかな。

  

手順は以下の通り。

  

> $ ls
> 
> MTOS-5.02-ja.zip  PostToTwitter-2.0.0.zip
> 
> $ unzip PostToTwitter-2.0.0.zip 
> 
> Archive:  PostToTwitter-2.0.0.zip
> 
>    creating: PostToTwitter/
> 
>    creating: PostToTwitter/docs/
> 
>   inflating: PostToTwitter/docs/info1.png  
> 
>   inflating: PostToTwitter/docs/info2.png  
> 
>   inflating: PostToTwitter/docs/mtdocs.css  
> 
>   inflating: PostToTwitter/docs/post\_to\_twitter.html  
> 
>   inflating: PostToTwitter/docs/preview.png  
> 
>   inflating: PostToTwitter/docs/setting1.png  
> 
>   inflating: PostToTwitter/docs/setting2.png  
> 
>   inflating: PostToTwitter/docs/setting3.png  
> 
>   inflating: PostToTwitter/docs/setting4.png  
> 
>   inflating: PostToTwitter/docs/setting5.png  
> 
>    creating: PostToTwitter/plugins/
> 
>    creating: PostToTwitter/plugins/PostToTwitter/
> 
>    creating: PostToTwitter/plugins/PostToTwitter/lib/
> 
>    creating: PostToTwitter/plugins/PostToTwitter/lib/PostToTwitter/
> 
>    creating: PostToTwitter/plugins/PostToTwitter/lib/PostToTwitter/L10N/
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/lib/PostToTwitter/L10N/en\_us.pm  
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/lib/PostToTwitter/L10N/ja.pm  
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/lib/PostToTwitter/L10N.pm  
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/post\_to\_twitter.pl  
> 
>    creating: PostToTwitter/plugins/PostToTwitter/tmpl/
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/tmpl/blog\_config.tmpl  
> 
>   inflating: PostToTwitter/plugins/PostToTwitter/tmpl/message\_format.tmpl  
> 
> $ cd PostToTwitter
> 
> $ ls
> 
> docs  plugins
> 
> $ cd plugins/
> 
> $ ls -l 
> 
> PostToTwitter
> 
> $ sudo mv PostToTwitter /var/www/cgi-bin/mt/plugins/.
> 
> $ 

  

あとは、プラグインに PostToTwitterが表示されていればインストールはOK。

プラグインの設定でtwitterのIDとパスワードを設定すれば完了です。
