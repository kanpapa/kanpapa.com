---
title: "SECCON 2017 Online CTF のWrite-upをまとめました"
date: 2017-12-10
categories: 
  - "security"
tags: 
  - "seccon"
coverImage: "seccon-ctf-2017-1.png"
---

SECCON 2017 オンラインCTFに参加しました。

[去年のCTF](https://kanpapa.com/2016/12/seccon-ctf-2016-online-write-up.html "SECCON CTF 2016")と同様一人チームでのんびり取り組みましたが、今回はなんと300点問題が解けました！

解いた問題は５つで、合計で700点獲得できました。

- Run me! (Programming) 100点 826人が回答
- putchar music (Programming) 100点 429人が回答
- SHA-1 is dead (Crypto) 100点 453人が回答
- z80 (Binary) 300点 18人が回答
- Thank you for playing! (Thank you!) 100点 830人が回答

忘れないうちにWrite-upを書いておきました。

### Run me!(Programming) 100点

問題のpythonプログラムをみると、かなり深い再帰を行うプログラムのようです。このまま実行しても終わりません。

まずはプログラムの動きを確認するために最初の呼び出し元であるf(11010)の引数を変えて実行してみたところ、以下のような値になりました。

```
1 = 1
2 = 1
3 = 2
4 = 3
5 = 5
6 = 8
7 = 13
8 = 21
9 = 34
10 = 55
11 = 89
12 = 144
13 = 233
14 = 377
```

これを関数に置き換えてみると、以下のような展開になります。

```
f(0) = 0
f(1) = 1
f(2) = f(2-2) + f(2-1) = f(0) + f(1) = 0 + 1 = 1
f(3) = f(3-2) + f(3-1) = f(1) + f(2) = 1 + 1 = 2
f(4) = f(4-2) + f(4-1) = f(2) + f(3) = 1 + 2 = 3
f(5) = f(5-2) + f(5-1) = f(3) + f(4) = 2 + 3 = 5
```

ということは、ループにしてf(n)の値を配列に保存して、その値を順次使って計算すれば良さそうです。

pythonで作成したプログラムは以下のようになりました。

```
$ cat RunMe3.py 
f = [0, 1, 1]
n = 3

while True:
    f.append(f[n-2] + f[n-1])
    n += 1
    if n >= 11012:
       break

print "SECCON{" + str(f[11011])[:32] + "}"
$ python RunMe3.py
SECCON{65076140832331717667772761541872}
```

### putchar music(Programming) 100点

まずは問題のプログラムをコンパイルしました。標準出力にデータがでてくるようなので、ファイルに出力しましたがかなり巨大だったので途中で中断しました。生成されたファイルは単なるデータのようです。

```
$ ls -l output.bin-rw-rw-r-- 1 ocha ocha 2322149376 Dec  9 23:36 output.bin$ file output.binoutput.bin: data$
```

これをバイナリダンプしてみたところ、各データの数値の前後の値がそれほど変化しておらず、なにやら連続的なアナログな数値に見えました。

```
$ hexdump output.bin | more 0000000 0805 0e0b 1310 1916 1f1c 2421 2a27 302d0000010 3532 3b38 413e 4643 4c49 524f 5754 5d5b0000020 6361 6965 6f6b 7371 7977 7f7d 8583 8b870000030 918d 9593 9b99 a19f a7a5 ada9 b3af b7b70000040 bfba c3c2 cac7 cecb d6d3 dbd6 dfde e7e20000050 eae7 f2ef f6f3 fbfa 03fe 0706 0e0b 130f0000060 1b17 1f1b 2323 2b27 2f2b 3733 3b37 3f3f0000070 4743 4b4b 534f 5753 5b5b 635f 6767 6c6e0000080 766f 7c75 7d7f 8784 8d86 8e8f 9495 9e970000090 9f9c a5a6 afac b4ad b6b7 bcbd c5be c7c500000a0 cdcf d7cf ddd5 dfdf e7e5 ede7 efed f5f500000b0 fff7 fffd 0507 0f0d 150f 1717 1d1d 271f00000c0 2726 2f2e 3636 3e37 3e3f 4746 4f46 4f4e00000d0 5657 5e57 665f 6766 6f6e 776e 7677 7f7f00000e0 877f 8787 8f8f 9797 9f97 9f9f a7a7 afa700000f0 afaf b7b7 bfb7 c7bf c7c7 cfcf d7cf dedc0000100 dcd9 eadf efed edea fbf8 f8fe fefb 0c090000110 090e 0f0c 1d1a 1a1f 281d 2e2b 2b28 392f0000120 3f3d 3d39 4b3f 494d 4d4b 5b59 595f 5f5b0000130 6d69 696f 6f6d 7d7b 7b79 897d 8f8b 8b8b0000140 9b8e 9f9e 9e9a aa9f aaaf afab bbba bbbe0000150 bebe cecb cacf cfce dfda dbda eadf efeb0000160 efeb fbef ffff fffb 0bff 0b0f 0f0b 1b1b　　　　:
```

もしやと思い、このデータをaplayに流し込んでみたら・・・・。

```
$ aplay output.bin Playing raw data 'output.bin' : Unsigned 8 bit, Rate 8000 Hz, Mono
```

有名な映画音楽が流れてきました。

この問題は５分もかからなかったかもしれません。

### SHA-1 is dead(Crypto) 100点

これは以下の条件のファイルを作れという問題です。

```
file1 != file2 SHA1(file1) == SHA1(file2) SHA256(file1) <> SHA256(file2) 2017KiB < sizeof(file1) < 2018KiB 2017KiB < sizeof(file2) < 2018KiB* 1KiB = 1024 bytes
```

SHA-1が破られたということで話題になりました。まずはその記事を確認です。

https://shattered.it

ここに載っている2つのPDFがSHA-1が同じだけど、中身が違うサンプルファイルです。

でもこのファイルは大きさが小さいです。どうしようかなと思っていたところで、次のスライドを見つけました。

https://www.slideshare.net/herumi/googlesha1

なんと、違っているのは前半の一部分ということなので、先ほどのPDFファイルに適当なデータをくっつけてサイズを合わせれば良いことになります。

```
$ cat sha2.c#include int main(){   char a;   for (int i = 1; i < 2018*1024-1 ; i++){    putchar(getchar());   }}$ ./sha2 < shattered-1.pdf > a1.pdf$ ./sha2 < shattered-2.pdf > a2.pdf$ ls -l a?.pdf-rw-rw-r-- 1 ocha ocha 2066430 Dec 10 08:27 a1.pdf-rw-rw-r-- 1 ocha ocha 2066430 Dec 10 08:28 a2.pdf$$ cmp -b a1.pdf a2.pdf a1.pdf a2.pdf differ: byte 193, line 8 is 163 s 177 ^?$ cat a1.pdf | openssl sha1(stdin)= b4e859a1c9d68d2dae07b02e3d8a1bbb77fe5bff$ cat a2.pdf | openssl sha1(stdin)= b4e859a1c9d68d2dae07b02e3d8a1bbb77fe5bff$ cat a1.pdf | openssl sha256(stdin)= d8109bf9bc8dc0960b8650b4ac96223fab268a47b40d32a295dd8121dc142752$ cat a2.pdf | openssl sha256(stdin)= 86021f60a9a82dc1e617b2157fdf63fe04d1c83d7a19dbc29f2fa4c4b4f17b8b
```

できたファイルをアップロードしてフラグが取れました。

### z80(Binary) 300点

これはz80ファンとしては解かねばいうことで時間をかけて取り組みました。

JPEGの写真がたくさん入っていて、Z-80 CPUとArduino Megaが接続されたハードウェアが360度の方向から写っていました。Z-80の周辺デバイスとしてArduino Megaを使うもののようです。

この問題のハードウェアの写真をまとめてビデオにしてみました。

https://www.youtube.com/watch?v=an2iK-qTb2M

※SECCON様から掲載許可をいただきました。ありがとうございます。

Arduinoのソースをみると、実行コードらしい16進数が組み込まれていましたが、どうもZ80ぽくない数値です。

```
static unsigned char mem[memsize] = {  0x22, 0x47, 0x00, 0x3d, 0x53, 0x77, 0x23, 0x3d, 0x45, 0x77, 0x23, 0x3d, 0x43,   0x77, 0x23, 0x77, 0x23, 0xc5, 0x0c, 0x77, 0x23, 0xc5, 0xfd, 0x77, 0x23, 0x3d,   0x7b, 0x77, 0x23, 0x39, 0x44, 0x00, 0x47, 0xc5, 0x46, 0x31, 0x44, 0x00, 0x78,   0x31, 0x46, 0x00, 0xfd, 0x22, 0xf9, 0x1e, 0x00, 0xfd, 0x7b, 0xf1, 0x1e, 0x00,   0x77, 0x23, 0x39, 0x45, 0x00, 0x3e, 0x31, 0x45, 0x00, 0xc1, 0x1e, 0x00, 0x3d,   0x7d, 0x77, 0x75, 0x03, 0x0b, 0x09, };
```

多分、データバスもしくはアドレスバスの接続がわざと変えてあるのだろうと推測し、たくさんある写真を見比べたところ、データバスのD0とD1が逆に接続されているように見えました。そこで、Arduinoのソースにある16進数の下位2ビットを入れ替えてみると、見慣れたZ80の機械語がでてきました。21 xx xxとか 3E xx は一番多く使うものだと思います。

変換プログラムを作ってもよかったのですが、コードが短いので手で置き換えてZ80アセンブラのソースコードを作りました。

```
  0000     0x22, 0x47, 0x00    21 47 00         LD HL,0x0047  0003     0x3d, 0x53          3E 53            LD A,'S'  0005     0x77                77               LD (HL),A  0006     0x23,               23               INC HL  0007     0x3d, 0x45          3E 45            LD A,'E'  0009     0x77                77               LD (HL),A  000a     0x23                23               INC HL  000b     0x3d, 0x43,         3E 43            LD A,'C'  000d     0x77                77               LD (HL),A  000e     0x23                23               INC HL  000f     0x77                77               LD (HL),A  0010     0x23,               23               INC HL   0011     0xc5, 0x0c          C6 0C            ADD A,0x0c       0x43+0xc = 0x4f = 'O'  0013     0x77                77               LD (HL),A  0014     0x23                23               INC HL  0015     0xc5, 0xfd          C6 FE            ADD A,0xfe       0x4f+0xfe = 0x14d = 4d = 下位2ビット入替 = 4E = 'N'  0017     0x77                77               LD (HL),A  0018     0x23,               23               INC HL  0019     0x3d, 0x7b          3E 7B            LD A,'{'  001b     0x77             　 77               LD (HL),A  001c     0x23                23               INC HL  001d     0x39, 0x44, 0x00    3A 44 00  LOOP1: LD A,(0x0044)      A <= 0x03  0020     0x47,               47               LD B,A             B <= 0x03  0021     0xc5, 0x46          C6 45            ADD A,0x45         A <= 0x45 + 0x03   0023     0x31, 0x44, 0x00    32 44 00         LD (0x0044),A  0026     0x78,               78               LD A,B  0027     0x31, 0x46, 0x00,   32 45 00         LD (0x0045),A  002a     0xfd, 0x22,         FE 21            CP 0x21  002c     0xf9, 0x1e, 0x00,   FA 1D 00         JP M,LOOP1  002f     0xfd, 0x7b          FE 7B            CP 0x7B  0031     0xf1, 0x1e, 0x00    F2 1D 00         JP P,LOOP1  0034     0x77                77               LD (HL),A  0035     0x23                23               INC HL  0036     0x39, 0x45, 0x00,   3A 46 00         LD A,(0x0046)  0039     0x3e,               3D               DEC A  003a     0x31, 0x45, 0x00,   32 46 00         LD (0x0046),A  003d     0xc1, 0x1e, 0x00,   C2 1D 00         JP NZ,LOOP1  0040     0x3d, 0x7d          3E 7E            LD A,0x7e    　　　 下位2ビット入替で7E -> 7D = '}'     0042     0x77                77               LD (HL),A   0043     0x75,               76               HALT                停止（さすが！）  0044     0x03                03               DB 0x03  0045     0x0b                0B               DB 0x0b  0046     0x09,               0A               DB 0x0a
```

ソースコードの最初を見てみると、フラグの頭文字の"SECCON{"をメモリに書き込んでいることがわかります。書き込むときも下位２ビットを入れ替えることになります。肝心なフラグの部分は条件判断やループを使っていたので、その部分だけ簡単なプログラムを作りフラグを求めました。

```
$ cat z80.c#include int main(){  char x0044 = 0x03;  // 00000011  char x0045 = 0x0b;  // 00001011  char x0046 = 0x0a;  // 00001001 => 00001010  char a;  char b;  int hl = 0;loop1:  a = x0044;  b = a;  a = a + 0x45;  x0044 = a;  a = b;  x0045 = a;  if (a < 0x21) goto loop1;  if (a >= 0x7b) goto loop1;  printf("0x%02x - %c\n",a,a);  hl = hl + 1;  a = x0046;  a = a - 1;  x0046 = a;  if (a != 0) goto loop1;}$ ./a.out0x48 - H0x5c - \0x2b - +0x70 - p0x3f - ?0x53 - S0x22 - "  →下位2ビットを入れ替えて 0x21  !0x67 - g0x36 - 6  →下位2ビットを入れ替えて 0x35  50x4a - J  →下位2ビットを入れ替えて 0x49  I$
```

これでフラグがとれました。ちなみに下位ビットの入れ替えはmacOSの標準アプリの「計算機」で確認しながら行いました。

この問題はデータバスの２本だけが入れ替わっていたのが救いでした。アドレスバスも入れ替わっていたら追いきれませんので。

### Thank you for playing!(Thank you!) 100点

z80が終わって一息ついて次は何をやろうかなと思っていたら一番最後にこのボーナス問題がありました。フラグをそのまま入力して100点取りました。

### 総評

今回は初めて100点以外の問題が解けました。Z80＋Arduinoという楽しい問題をありがとうございました。また終盤に公開されたボーナス問題もありがたかったです。また来年もできる範囲で参加したいと思います。運営の皆様ありがとうございました。
