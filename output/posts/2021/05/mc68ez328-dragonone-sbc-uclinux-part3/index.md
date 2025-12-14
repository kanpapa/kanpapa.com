---
title: "MC68EZ328 DragonOne SBCでuClinuxを動かす(3) ～bootから追う～"
date: 2021-05-22
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
coverImage: "mc68ez328_dragonone_sbc_uclinux_part3_debug.png"
---

[前回 initが読み込めないで停止する状態](https://kanpapa.com/2021/05/mc68ez328-dragonone-sbc-uclinux-part2.html "MC68EZ328 DragonOne SBCでuClinuxが起動しました（2）～initはどこだ？～")でしたが、まだ進捗がでていません。

printkで入出力パラメタやerrnoなどを表示して追っていますが、おかしいパラメタやerrnoもみつからずやや手詰まりになっています。

![](images/mc68ez328_dragonone_sbc_uclinux_part3_debug.png)

そこで、bootからinitの起動までソースをざっと追ってみることにします。

<!--more-->

### リセット直後のCPUの初期化ルーチン

リセットすると、$00000000にフラッシュメモリが配置されます。フラッシュメモリの$00000000から4バイトはスタックポインタの初期値、$00000004から4バイトはプログラム開始アドレスが書き込まれています。CPUはこれらの値を読み込み動き始めます。

リセット後に動作するプログラムは、arch/m68knommu/platform/68EZ328/ucsimm/crt0\_rom.Sの\_startから動きます。まずはステータスレジスタを設定しています。

```
    .text
_start:
_stext: movew #0x2700,%sr

```

このあと、UARTの設定、PLLの設定を行い、PLLが安定するまで少しループで待ちます。

```
    movew   #0x0800, 0xfffff906		/* Ignore CTS */
movew   #0x010b, 0xfffff902		/* BAUD to 9600 */
movew   #0xe100, 0xfffff900		/* enable */
movew   #0x2400, 0xfffff200		/* PLLCR */
movew   #0x0123, 0xfffff202		/* PLLFSR */
moveq   #0, %d0
movew   #16384, %d0         	/* PLL settle wait loop */
_pll_settle:
subw    #1, %d0
bne     _pll_settle

```

続いて、フラッシュメモリを$10000000に配置、DRAMは$00000000に配置するなどのCPUの設定を行います。

```
    moveb   #0x00,   0xfffffb0b     /* Watchdog off */
moveb   #0x10,   0xfffff000     /* SCR */
moveb   #0x00,   0xfffff40b     /* enable chip select */
moveb   #0x00,   0xfffff423     /* enable /DWE */
moveb   #0x08,   0xfffffd0d     /* disable hardmap */
moveb   #0x07,   0xfffffd0f     /* level 7 interrupt clear */
movew   #0x8000, 0xfffff100     /* FLASH at 0x10000000 */
movew   #0x01ed, 0xfffff110     /* 8Meg, 16bit, enable, 0ws */
movew   #0x8f00, 0xfffffc00     /* DRAM configuration */
movew   #0x8667, 0xfffffc02     /* DRAM control */
movew   #0x0000, 0xfffff106     /* DRAM at 0x00000000 */
movew   #0x068d, 0xfffff116     /* 8Meg, 16bit, enable, 0ws */
moveb   #0x40,   0xfffff300     /* IVR */
movel   #0x007FFFFF, %d0        /* IMR */
movel   %d0, 0xfffff304
moveb   0xfffff42b, %d0
andb    #0xe0, %d0
moveb   %d0, 0xfffff42b
movew   #0x8000, 0xFFFFF102		/* CSB */
movew   #0x0190, 0xFFFFF112		/* disable eth + DPRAM - KH */

```

### 変数領域の初期化

次はフラッシュメモリにあるデータセグメント(data)のデータをRAMにコピーします。これは初期値を持つ変数の値の内容になります。

```
	/* Copy data segment from ROM to RAM */
moveal	#__data_rom_start, %a0
moveal	#_sdata, %a1
moveal	#_edata, %a2
/* Copy %a0 to %a1 until %a1 == %a2 */
1:	movel	%a0@+, %a1@+
cmpal	%a1, %a2
bhi	1b

```

続いて初期値を持たない変数のエリア(bss)を0で埋めます。

```
	moveal	#_sbss, %a0
moveal	#_ebss, %a1
/* Copy 0 to %a0 until %a0 == %a1 */
1:
clrl	%a0@+
cmpal	%a0, %a1
bhi	1b

```

グローバル変数の値を設定し、スタックポインタを設定します。

```
        movel   #_sdata, %d0
movel   %d0,    _rambase
movel   #_ebss,  %d0
movel   %d0,    _ramstart
movel	#__ramend-CONFIG_MEMORY_RESERVE*0x100000, %d0
movel	%d0,	_ramend
movel	#__ramvec,	%d0
movel	%d0,	_ramvec
/*
* load the current task pointer and stack
*/
lea     init_task_union,%a0
movel   %a0, _current_task
lea     0x2000(%a0),%sp

```

### カーネルの起動

最後にカーネルを動かします。戻ってきたら再度動かすように無限ループになっています。

```
1:	jsr	start_kernel
bra 1b

```

ここから先はLinux kernelに入ります。以降はC言語で書かれているのでやや読みやすくなります。（続く）
