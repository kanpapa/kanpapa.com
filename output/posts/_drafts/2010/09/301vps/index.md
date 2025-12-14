---
title: "301リダイレクトでお引っ越しを宣言する"
date: 2010-09-29
draft: true
---

ほぼ旧レンタルサーバからさくらVPSへのサーバの移行が終わったので、301リダイレクトを設定して、旧サーバにアクセスがあっても新サーバに転送されるようにした。301リダイレクトにすることで恒久的な移動として検索エンジンが引き継いでくれるそうだ。 具体的には、.htaccessに以下の１行を書いただけ。 Redirect 301 / https://kanpapa.com/ この設定のあと旧サーバにアクセスしたら、ちゃんとkanpapa.comに遷移した。 リダイレクト確認ツールなるものがあちこちにあるので、それで確認するとこんな表示がでた。 Status : (301) Moved Permanently The Redirect is Search Engine Friendly. もっとも、telnetで試してもよい。 $ telnet xxxxxxxx.sakura.ne.jp 80 Trying 219.94.162.14... Connected to xxxxxxxx.sakura.ne.jp. Escape character is '^\]'. GET / HTTP/1.0 User-Agent: Telnet \[ja\] (Linux) Host: xxxxxxxx.sakura.ne.jp HTTP/1.1 301 Moved Permanently Date: Wed, 29 Sep 2010 15:16:22 GMT Server: Apache/1.3.42 (Unix) mod\_ssl/2.8.31 OpenSSL/0.9.8e Location: https://kanpapa.com/ Connection: close Content-Type: text/html; charset=iso-8859-1

301 Moved Permanently

# Moved Permanently

The document has moved [here](https://kanpapa.com/).

* * *

Apache/1.3.42 Server at xxxxxxxx.sakura.ne.jp Port 80

Connection closed by foreign host. $ ちゃんと301で新サーバにリダイレクトできていることがわかる。
