---
title: "COSMAC MBC CPUボード Rev. 0.2の基板を発注しました。"
date: 2019-11-03
categories: 
  - "cosmac"
tags: 
  - "cosmac-mbc"
coverImage: "cosmac_mbc_cpu_rev02_3dview.jpg"
---

COSMAC MBC CPUボード Rev.0.2の基板を[FusionPCB](https://www.fusionpcb.jp/ "FusionPCB")に発注しました。

今回のCPU基板 Rev.0.2では以下の点を改良しています。

- シリアル接続の信号が正しくなるようにインバーターを通しました。
- シリアル接続コネクタを一般的な配置にしました。
- 拡張ボードに合わせて拡張コネクタ仕様を見直しました。
- S5をスライドスイッチからオリジナルのようにトグルスイッチに変更しました。
- 各スイッチは横向き実装可能なパターンにしました。適合スイッチは以下を想定しています。
    - プッシュスイッチ　型番：APE1F-6M-10-ZまたはAPE1F-5M-10-Z（日本電産コパル電子）
    - トグルスイッチ　型番：2MS1-T1-B2-M6-S-E（Linkman）
- SRAMは256Kbitに変更し、秋月のSOP2 SRAMも実装できるように表面実装パターンも追加しました。表面実装基板は初発注です。
- オリジナルに存在する信号（~EXT\_WAIT, ~EXT\_CLEAR, ~STOP, ~XTAL）のコネクタを追加しました。
- パスコンを配置しました。
- その他、細かい点を修正しました。

FusionPCB発注時のガーバービューアー画面は以下のようになりました。

![cosmac_mbc_rev02_gerber_viewer.jpg](images/cosmac_mbc_rev02_gerber_viewer.jpg)

実装イメージの3D画像です。ちょっとシルクがスイッチにかかってしまっているかも・・。

![cosmac_mbc_cpu_rev02_3dview.jpg](images/cosmac_mbc_cpu_rev02_3dview.jpg)

到着は来週になるでしょうが、楽しみです。
