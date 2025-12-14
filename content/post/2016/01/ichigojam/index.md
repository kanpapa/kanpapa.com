---
title: "IchigoJamをブレッドボードから専用基板に載せ替えてみた"
date: 2016-01-03
slug: "ichigojam"
categories: 
  - "electronics"
image: "images/ichigojam_02.jpg"
---

秋月電子で[IchigoJam U用プリント基板（通販コード P-10037）](http://akizukidenshi.com/catalog/g/gP-10037/ "IchigoJam U用プリント基板")が売られていたので思わず２枚買ってしまいました。手持ちの部品で２台ぐらいは作れると思いましたので。

![ichigojam_00.jpg](images/ichigojam_00.jpg) <!--more-->

以前にIchigoJamをブレッドボードに組んでそのままになっていたのでこの専用基板に載せ替えてみました。

![ichigojam_01.jpg](images/ichigojam_01.jpg)

12MHzのXTALは手持ちがなかったのですが、それ以外は手持ちのパーツを使って実装しました。

![ichigojam_02.jpg](images/ichigojam_02.jpg)

ただし、ブレッドボードで使っていた[3.3Vレギュレーター（XC6202P332TH）](http://akizukidenshi.com/catalog/g/gI-09119/ "XC6202")の足がこの基板の配置とは合っていなかったので、足を少し折り曲げて無理やり合わせています。手持ちのパーツを使うときはこのような点に気をつける必要があります。ちなみにレギューレーターの接続を間違えるとすごく熱くなってパシッと音がして壊れます・・・。

![ichigojam_03.jpg](images/ichigojam_03.jpg)

無事動作も確認し、ついでにファームウェアをアップデートしておきました。

![ichigojam_04.jpg](images/ichigojam_04.jpg)

これで最新版のIchigoJamの完成です。
