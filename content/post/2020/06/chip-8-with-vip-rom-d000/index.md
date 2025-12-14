---
title: "リロケートしたVIP OS ROMでCHIP-8が動くようにしました"
date: 2020-06-21
slug: "chip-8-with-vip-rom-d000"
categories: 
  - "cosmac"
  - "cosmac-mbc"
tags: 
  - "cosmac-mbc"
image: "images/cosmac_cdp1802ace.jpg"
---

[VIP OSをROMの空きエリア$D000にリロケートし、VIP OSが動くところまで](https://kanpapa.com/cosmac/blog/2020/05/cosmac-vip-os-rom-reloc.html "       COSMAC VIP OSをROMの空きエリアに移動しました")は確認しました。次はこのリロケートしたVIP OSのROMで動くようにCHIP-8のパッチを作ります。

[前回](https://kanpapa.com/cosmac/blog/2020/04/cosmac-vip-chip-8-startup.html "COSMACでCHIP-8インタプリタを動かしてみました")はCHIP-8の起動時にレジスタの値を設定するために小さなプログラムをRAMの$6000に書き込む必要がありましたが、今回はこのプログラムはCHIP-8本体の空きエリアに収まるようにしてみました。

## CHIP-8インタプリタの改造

1. オリジナルのCHIP-8のバイナリに以下のパッチをあてます。  
    
    ```
    W0000 C0 01 F2W000A D1W010B D1W012A D1W019E 37W01A1 3FW01F2 F8 0F BB FF 01 C0 00 04
    ```
    

3. パッチを当てた状態でIntel Hexで保存しておきます。  
    
    ```
    >S0000 200
    ```
    
      
    

## CHIP-8の起動方法

1. RESETとRUN UでMCSMP20モニタを起動します。

3. 先ほどパッチを当てたCHIP-8インタプリタをLコマンドで読み込みます。

5. CHIP-8のアプリケーションプログラムを$0200から書き込みます。

7. RESETを押し、RUN Pを押すとCHIP-8インタプリタが動きます。

## パッチの内容

パッチの$0000を見るとわかりますが、レジスタの値を設定するために、CHIP-8の空き領域($01F2)に書き込んだプログラムにジャンプします。

$01F2に書き込んだプログラムは以下の通りです。

```
01F2-F8 0F    START: LDI $0F ;$0F->R11.1
01F4-BB              PHI 11
01F5-FF 01 　        SMI $01
01F7-C0 00 04        LBR $0004
```

ここは前回作成したツールと同じ動きで、レジスタに値をセットしたあとは$0004にジャンプしCHIP-8の初期化ルーチンに戻ります。

これでCOSMAC MBCでのCHIP-8の利用がかなり楽になりました。
