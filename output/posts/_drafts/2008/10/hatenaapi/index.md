---
title: "hatena認証APIをたたいてみる"
date: 2008-10-17
draft: true
---

どうもhatena認証プラグインの設定は間違っていないようなので、手動でhatena認証APIをたたいてみることにした。  
  
1\. perlを使ってMD5 hexをとる。  
  
Macintosh:~ ocha$ perl  
use Digest::MD5 qw(md5\_hex);  
print Digest::MD5::md5\_hex("秘密鍵api\_keyAPIキー");  
^D  ←コントロールD  
7e1b97b3a0fe32cfd2ba13c7852cc143Macintosh:~ ocha$  
  
できたシグネチャの文字列は　7e1b97b3a0fe32cfd2ba13c7852cc143　です。  
  
2\. これをapi\_sigとしてクエリーに積む。  
  
http://auth.hatena.ne.jp/auth?api\_key=APIキー&api\_sig=7e1b97b3a0fe32cfd2ba13c7852cc143  
  
3\. hatena認証画面がでた！  
  
方式は問題ないみたいです。ではソースの検証に入ります。
