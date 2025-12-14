---
title: "MC68EZ328 DragonOne SBCでuClinuxを動かす(4) ～start_kernelを追う～"
date: 2021-05-22
slug: "mc68ez328-dragonone-sbc-uclinux-part4"
categories: 
  - "mc68ez328"
  - "retrocomputing"
tags: 
  - "mc68ez328"
image: "images/mc68ez328_dragonone_sbc_uclinux_part4_vscode.png"
---

start\_kernelでようやくLinux kernelに入ってきました。細かいところはざっとながしてフィーリングでカーネルのソースを眺めます。

![](images/mc68ez328_dragonone_sbc_uclinux_part4_vscode-1024x603.png)

### start\_kernelを紐解く

start\_kernelはinit/main.cにあります。printkでLinuxのバナーを表示しています。

```
asmlinkage void __init start_kernel(void)
{
char * command_line;
extern char saved_command_line[];
/*
* Interrupts are still disabled. Do necessary setups, then
* enable them
*/
lock_kernel();
printk(linux_banner);

```

こんな表示ですね。

```
Linux version 2.4.34.5-uc0 (ocha@M715Q-TINY) (gcc version 4.7.2 (GCC) ) #49 Sat May 22 22:05:45 JST 2021

```

その次にCPUアーキテクチャ用の設定を行っています。ここは関連がありそうなので追ってみます。

```
	setup_arch(&command_line);

```

### setup\_archを紐解く

setup\_arch()をみてみます。この関数はarch/m68knommu/kernel/setup.cにあります。このあたりはコードとデータのアドレスを変数に設定しているようです。

```
void setup_arch(char **cmdline_p)
{
memory_start = PAGE_ALIGN(_ramstart);
memory_end = _ramend; /* by now the stack is part of the init task */
init_mm.start_code = (unsigned long) &_stext;
init_mm.end_code = (unsigned long) &_etext;
init_mm.end_data = (unsigned long) &_edata;
init_mm.brk = (unsigned long) 0;

```

次のconfig\_BSP()はarch/m68knommu/platform/68EZ328/config.cにあります。

```
	config_BSP(&command_line[0], sizeof(command_line));

```

config\_BSP()ではprintkで68EZ328のバナーを表示したあとにUCSIMMの情報を取得して、コマンドラインに載せていますが、ここは自作ボードですのでコメントにして、コマンドラインには文字列の終端の0だけ入れました。その後各種エントリポイントを設定しているようですが、mountには関係ないので飛ばします。

```
void config_BSP(char *command, int len)
{
unsigned char *p;
printk("\n68EZ328 DragonBallEZ support (C) 1999 Rt-Control, Inc\n");
#ifdef CONFIG_UCSIMM
/*
printk("uCsimm serial string [%s]\n",getserialnum());
p = cs8900a_hwaddr = gethwaddr(0);
printk("uCsimm hwaddr %.2x:%.2x:%.2x:%.2x:%.2x:%.2x\n",
p[0],
p[1],
p[2],
p[3],
p[4],
p[5]);
p = getbenv("APPEND");
if (p) strcpy(p,command);
else command[0] = 0;
*/
command[0] = 0;
#endif
mach_sched_init      = BSP_sched_init;
mach_tick            = BSP_tick;
mach_gettimeoffset   = BSP_gettimeoffset;
mach_gettod          = BSP_gettod;
mach_hwclk           = NULL;
mach_set_clock_mmss  = NULL;
// mach_mksound         = NULL;
mach_reset           = BSP_reset;
// mach_debug_init      = NULL;
config_M68EZ328_irq();
}

```

再びsetup\_arch()にもどります。このあたりはバナーですね。

```
	printk("\r\nuClinux/" CPU "\n");
printk("Flat model support (C) 1998,1999 Kenneth Albanowski, D. Jeff Dionne\n");

```

実際はこんな表示になります。

```
uClinux/MC68EZ328
Flat model support (C) 1998,1999 Kenneth Albanowski, D. Jeff Dionne

```

次は重要な部分です。今問題となっているルートデバイスを作っています。

```
	ROOT_DEV = MKDEV(BLKMEM_MAJOR,0);

```

BLKMEM\_MAJORはdrivers/block/blkmem.cで定義されていて、31です。

```
#define	BLKMEM_MAJOR 31

```

Documentation/devices.txtには以下の記述があります。これで/dev/rom0だとわかります

```
 31 block	ROM/flash memory card
0 = /dev/rom0		First ROM card (rw)
...

```

さて、setup\_archのソースに戻ります。ここはコマンドラインを保存していますね。

```
	/* Keep a copy of command line */
　　　　*cmdline_p = &command_line[0];
memcpy(saved_command_line, command_line, sizeof(saved_command_line));
saved_command_line[sizeof(saved_command_line)-1] = 0;

```

次はメモリ管理で何かやっているようですが、今のトラブルとは関係なさそうなので飛ばします。

```
	/*
* give all the memory to the bootmap allocator,  tell it to put the
* boot mem_map at the start of memory
*/
bootmap_size = init_bootmem_node(
NODE_DATA(0),
memory_start >> PAGE_SHIFT, /* map goes here */
PAGE_OFFSET >> PAGE_SHIFT,	/* 0 on coldfire */
memory_end >> PAGE_SHIFT);
/*
* free the usable memory,  we have to make sure we do not free
* the bootmem bitmap so we then reserve it after freeing it :-)
*/
free_bootmem(memory_start, memory_end - memory_start);
reserve_bootmem(memory_start, bootmap_size);
/*
* get kmalloc into gear
*/
paging_init();
}

```

これでsetup\_arch()は終わりです。romfsに関連した部分が見つかったのは収穫です。

ふたたび、start\_kernelにもどります。（続く）
