---
title: "MC68EZ328 DragonOne SBCでDRAMが動かなくて悩み中"
date: 2021-04-25
slug: "mc68ez328-dragonone-sbc-dram-test"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/dragonone_sbc_dram_only1.jpg"
---

[メモリダンプができるようになったDragonOne SBC](https://kanpapa.com/2021/04/mc68ez328-dragonone-sbc-memorydump.html "MC68EZ328 DragonOne SBCでメモリダンプができました")にメモリを接続してみます。

### DRAMを接続しよう

MC68EZ328で本格的なプログラムを動かすためには外部にメモリを接続しなければなりません。DragonOne SBCでは4Mx16bit EDO DRAMを搭載していますのでこれを使います。

リセット直後ではDRAMは使用できない状態なので、CPUに内蔵されているDRAMコントローラを設定してメモリの配置とリフレッシュ動作をするようにしなければなりません。この設定はCPUの内部レジスタに値を書き込む必要がありますが、これもブートローダーで行うことができます。

ブートローダーで設定する内容もDragonOneのホームページに登録されているのでそれを使えばすぐ動くと思ったのですが、そううまくはいきませんでした。

<!--more-->

### ブートローダーで初期設定

DragonOneのサイトには以下の設定ファイルが登録されています。ファイル名はinit.bです。ブートローダー用のbレコードです。この内容をブートローダーで書き込みます。

```
$ python3 loadb.py init.binit.bFFFFF1180130  emucs init 4-8 not needed without emuchipFFFFF0000110  SCR init 3-2FFFFFB0B0100  Disable WD 13-5FFFFF42B0103  enable clko 7-12FFFFF40B0100  set as dedicated chip selects 7-4FFFFF4230100  enable *DWE 7-11FFFFFD0D0108  disable hardmap 15-6 $0000 is $fffcFFFFFD0F0107  clear level 7 interrupt 15-8FFFFF100028000 CSA at 10000000FFFFF1100201ED 8 x 1M - KHFFFFF102028000 CSBFFFFF112020190 disable eth + DPRAM - KHFFFFFC00028F00 DRAM Config at $0 14-6FFFFFC02028667 DRAM ControlFFFFF106020000 CSD init at 0 -- RAS0 4M-6M, RAS1 6M-8M 4-4FFFFF11602068D enable DRAM cs - KHFFFFF3000140   IVRFFFFF30404007FFFFF IMRSend end.$ 
```

正常にレジスタに書き込まれたかダンプしてみます。

```
$ python3 mdump.py FFFFF100 40FFFFF100 0040FFFFF100 80 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 FFFFF110 01 ED 01 90 00 00 06 8D 00 30 00 00 00 00 00 00 FFFFF120 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FFFFF130 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 end.$ 
```

$FFFFF100には$8000、$FFFFF110には$01EDとinit.bと一致しており正常に書き込めているようです。

### DRAMにアクセスできるか確認

この状態でDRAMが$00000000～$007FFFFFに配置されているはずなのですが、電源投入直後のダンプの内容から変化がありません。

```
$ python3 mdump.py 00000000 4000000000 004000000000 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00000010 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00000020 FF FF FF FF FF FF FF FF FF FF 00 FF FF FF FF FF 00000030 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF end.$
```

試しに書き込んでみます。

```
$ python3 loadb.py test4.btest4.b000000001047474747474747474747474747474747000000101047474747474747474747474747474747000000201047474747474747474747474747474747000000301047474747474747474747474747474747Send end.$
```

もう一度ダンプしましたが、残念ながら変化なしです。

```
$ python3 mdump.py 00000000 4000000000 004000000000 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00000010 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00000020 FF FF FF FF FF FF FF FF FF FF 00 FF FF FF FF FF 00000030 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF end.$ 
```

ここで手詰まりになってしまいました。

### シンプルな回路で試してみる

ここはシンプルな回路でためしてみようと先日製作したCPU基板にDRAMをはんだ付けした基板を作りました。CPUとDRAMしか載っていないので、他のパーツの影響は受けません。

![dragonone_sbc_dram_only1.jpg](images/dragonone_sbc_dram_only1.jpg)

確認したのは以下のポイントです。制御信号の確認はミニオシロで行っています。

- CPUとDRAMの導通は問題なし。
- DRAMのアドレス帯に書き込んだ場合 DWE にLOWパルスが確認できる。DRAM以外のアドレスへ書き込んだ場合はパルスは発生しない。
- RAS/CASはリセット直後はHIGHの状態で、DRAMコントローラの初期設定をした直後から定期的にLOWパルスが確認できる。

信号的に問題は無さそうに見えるのですが、残念ながら状況は変わりませんでした。今思えば制御系信号がロジアナに簡単に接続できるようにヘッダピンに引き出しておくべきでした。

これまでの実験結果をGitHubにコミットしておきました。

https://github.com/kanpapa/MC68EZ328

何か単純な見落としのような気もするので、少し冷却期間をあけてから見直してみます。次の手としてはDRAMにワイヤーをはんだ付けして、その信号をロジアナで確認することになりそうです。
