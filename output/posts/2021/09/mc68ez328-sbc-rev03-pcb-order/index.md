---
title: "MC68EZ328 SBC Rev.0.3基板を発注しました"
date: 2021-09-21
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
coverImage: "dragonone_rev03_20210919.png"
---

先日製作した[MC68EZ328 SBC LANボード](https://kanpapa.com/2021/09/mc68ez328-dragonone-sbc-uclinux-network5.html "MC68EZ328 SBC LANを専用基板で製作しました")がスマートに実装できるように、MC68EZ328 SBC Rev.0.3基板を設計して[ALLPCB](https://www.allpcb.com/ "ALLPCB")さんに発注しました。

![](images/dragonone_rev03_20210919.png)

以下の点を改善しています。

- DRAM周りの回路ミスを修正（ジャンパー修正が不要になりました）
- LANボードを接続できるように専用コネクタの増設と基板固定穴の追加
- 標準DCコネクタの実装
- 一部パスコンなどをSMD実装に変更

この時点ですでに基板は完成して発送待ちのようです。早ければ来週の頭には到着すると思いますので楽しみです。

なお、GitHub.comのkanpapa-patch-1 ブランチにKiCadデータ含めてcommitしておきました。Rev0.3の動作確認ができたらmainブランチにマージします。

- [kanpapa/MC68EZ328: MC68EZ328 DragonOne SBC. (github.com)](https://github.com/kanpapa/MC68EZ328)
