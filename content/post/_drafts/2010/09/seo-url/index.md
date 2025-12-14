---
title: "URLを正規化してみた"
date: 2010-09-29
slug: "seo-url"
draft: true
---

SEO対策としてURLを正規化してみました。 たとえば、以下の３つのURLはすべて同じページを表示します。 https://kanpapa.com/index.html http://www.kanpapa.com/index.html https://kanpapa.com/ どのURLが来ても https://kanpapa.com/ に301でリダイレクトすることで、検索エンジンにhttps://kanpapa.com/ だけを覚えさせることができます。 また、xxxxx/index.html というアクセスがあっても、xxxxx/ に集約することもできます。 ここではapache.confにその設定を書いてみました。 RewriteEngine On RewriteBase /var/www/html RewriteCond %{THE\_REQUEST} ^.\*/index.html RewriteRule ^(.\*)index.html$ https://kanpapa.com/$1 \[R=301,L\] RewriteCond %{HTTP\_HOST} ^www.kanpapa\\.com RewriteRule ^(.\*)$ https://kanpapa.com/$1 \[R=301,L\] このように設定を追記して、/usr/sbin/apachectl restart でapacheを再起動しました。

この設定で、xxxxxx/index.html でアクセスがあった場合は xxxxxx/ に301でリダイレクトされ、http://www.kanpapa.com/ でアクセスがあった場合は、https://kanpapa.com/ に301でリダイレクトされるようになりました。
