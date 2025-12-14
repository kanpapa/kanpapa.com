---
title: "MFTokyo2020用にCOSMAC MBCのROMをチューニングしました"
date: 2020-09-20
categories: 
  - "cosmac"
  - "cosmac-mbc"
tags: 
  - "cosmac-mbc"
  - "maker-faire"
  - "mft2020"
coverImage: "memory_map_for_mft2020.png"
---

Maker Faire Tokyo 2020用にCOSMAC MBCに載せているROMをチューニングしました。展示ではCOSMAC VIP OSとCHIP-8を使うことになるので、これらが短時間で使えるようにしました。

変更点は以下の通りです。

- [MCSMP20からCOSMAC VIP OSを起動する](https://kanpapa.com/cosmac/blog/2020/08/cosmac-interrupt-enable-tips.html "COSMACで割り込み許可にしたい場合はどうするか？")ために割り込みを許可する命令をD200に置きました。
- [CHIP-8のイメージデータ](https://kanpapa.com/cosmac/blog/2020/06/CHIP-8-with-VIP-ROM-D000.html "リロケートしたVIP OS ROMでCHIP-8が動くようにしました")を$E000-$E1FFにおきました。このデータをモニタで$0000のRAMエリアに転送すればCHIP-8インタプリタの配置が終わります。

チューニングしたメモリマップは以下のようになりました。

![memory_map_for_mft2020.png](images/memory_map_for_mft2020.png)

<!--more-->

この結果、次の手順でデモができるようになります。

1. RESETする
2. RUN-UでMCSMP20を動かす
3. CHIP-8のイメージ($E000-)をRAM($0000)にモニタコマンドで転送する。  
    
    ```
    >TE000 0000 0200
    ```
    
4. MCSMP20で$D200から実行し、割り込み許可状態にしてCOSMAC VIP OSを起動する。  
    
    ```
    >RD200
    ```
    
5. COSMAC VIP OSでCHIP-8のアプリケーションプログラムを$0200から書き込む。
6. RESETする
7. RUN-PでCHIP-8インタプリタを起動し、CHIP-8アプリケーションが動く。
8. 入力ミスの場合は、RESET、RUN-Uで4.からやり直し
9. もし、CHIP-8インタプリタがこわれた場合は1.からやり直し

これで最低限の準備はできましたが、まだまだROMは空いているので、いろんなアプリケーションを詰め込んでみようかなと思います。
