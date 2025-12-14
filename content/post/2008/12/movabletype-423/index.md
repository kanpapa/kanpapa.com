---
title: "MovableType 4.23にアップグレードしました"
date: 2008-12-03
slug: "movabletype-423"
categories: 
  - "server"
tags: 
  - "movable-type"
---

XSS脆弱性が見つかったということなので、4.23にアップグレードしました。

手順は前回と同じです。

  

  

> $ cd

> $?unzip MT-4\_23-ja.zip

> $ cd ~/www  
> $ cd mt  
> $ cp mt-config.cgi ~/MT-4.23-ja/.  
> $ cd plugins/  
> $ cp -rp iMT ~/MT-4.23-ja/plugins/.  
> $?cp HatenaAuth.pl ~/MT-4.23-ja/plugins/.  
> $ cd ../mt-static/plugins/  
> $?cp -rp iMT ~/MT-4.23-ja/mt-static/plugins/.

> $ cd ~/www

> $ mv mt mt.old

> $ mv ~/MT-4.23-ja ~/www/mt

> $ mv mt.old ~/mt.old.20081203

>
