---
title: "weather:bitにOLEDを接続してみた"
date: 2017-12-15
categories: 
  - "electronics"
tags: 
  - "micro-bit"
coverImage: "weatherbit_oled.jpg"
---

この記事は[microbit Advent Calendar 2017](https://qiita.com/advent-calendar/2017/microbit "microbit Advent Calendar 2017")と[Mbed Advent Calendar 2017](https://qiita.com/advent-calendar/2017/mbed "Mbed Advent Calendar")の16日目の記事です。

[weather:bit](https://www.switch-science.com/catalog/3383/ "weather:bit")にはI2C PORTがあります。micro:bitとBME280の接続に使われているI2Cポートがそのまま出力されているようです。

![weatherbit_i2c.jpg](images/weatherbit_i2c.jpg)

せっかくなのでここにI2Cのデバイスを接続してみました。

I2Cで接続できる表示デバイスをつければ、温度、湿度、気圧が表示できて見やすくなるのではと思い、手元にあった秋月電子の[0.96インチ 128×64ドット有機ELディスプレイ(OLED)](http://akizukidenshi.com/catalog/g/gP-12031/ "０．９６インチ　１２８×６４ドット有機ＥＬディスプレイ（ＯＬＥＤ）")をスルーホール用のジャンパー線でI2Cに接続してみました。

![](images/weatherbit_oled.jpg)

このOLEDの制御チップはSSD1306で標準的なデバイスなのでJavaScript Blocks Editorでも追加パッケージがありました。

早速接続してJavaScript Blocks Editerでプログラムを作りました。パッケージの追加によってOLEDとWeatherbitが選択できるようになります。

![weatherbit_oled1.png](images/weatherbit_oled1.png)

このプログラムは[前回作成したBME280のプログラム](https://kanpapa.com/2017/12/microbit-weatherbit.html "weather:bitを使ってみた")にOLEDの表示部分を追加したものになりますが、これを動かしたところどうも動きがおかしく、OLEDにランダムなパターンが表示され、LEDも表示されなくなりプログラムも途中で停止しているように見えます。

![weatherbit_oled_error.jpg](images/weatherbit_oled_error.jpg)

おかしいなと、BME280の「start weather monitoring」のブロックをはずすと、OLED、LED共に正常に表示されます。

どうも何かが干渉しているように見えたので、mbedのオンライン開発環境でプログラムを作ってみました。

![microbit_mbed_compiler.png](images/microbit_mbed_compiler.png)  
[micro:bitのDALライブラリ](https://os.mbed.com/platforms/Microbit/#micro-bit-device-abstraction-layer-dal "micro:bit DAL")に加え、OLEDとBME280のライブラリは以下のものをつかいました。

- Wim Huiskampさんの[SSD1308\_128x64\_I2C](https://os.mbed.com/users/wim/code/SSD1308_128x64_I2C/ "SSD1308_128x64_I2C")

- Toyomasa Wataraiさんの[BME280](https://os.mbed.com/users/MACRUM/code/BME280/ "BME280")

mbedでのプログラムは以下のようになりました。各機能の動作確認をするためのテストコードもはいっています。

```
#include "MicroBit.h"
#include "mbed_logo.h"
#include "SSD1308.h"  // https://os.mbed.com/users/wim/code/SSD1308_128x64_I2C/
#include "BME280.h"   // https://os.mbed.com/users/MACRUM/code/BME280/

MicroBit uBit;
MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 

// Instantiate OLED SSD1306
// I2C address 0x78
SSD1308 oled = SSD1308(i2c, SSD1308_SA0);

// I2C address 0x76(default)
// Instantiate BME280 sensor
BME280 sensor = BME280(i2c);
     
int main() {
    // Initialise the micro:bit runtime.
    uBit.init();
    
    // micro:bit LED test
    uBit.display.scroll("HELLO WORLD! :)");
    
    // OLED test
    oled.writeString(0, 0, "Hello World !");
   
    oled.fillDisplay(0xAA);
    oled.setDisplayOff();
    wait(1);   
    oled.setDisplayOn();
 
    // weather info display
    while (1) {
        oled.clearDisplay();
        oled.setDisplayInverse();
        wait(0.5);
        oled.setDisplayNormal();                                         
 
        oled.writeBitmap((uint8_t*) mbed_logo);
        wait(1);
    
        oled.clearDisplay();
        oled.printf("%2.2f degC, %04.2f hPa, %2.2f %%\n", sensor.getTemperature(), sensor.getPressure(), sensor.getHumidity());
        wait(10);
    }
} //main
```

これをコンパイルして、micro:bitにダウンロードして実行したところ、正常に動作しました。

![](images/weatherbit_oled_ok.jpg)

今回作成したプログラムはmbedのサイトに公開しておきました。

https://os.mbed.com/users/kanpapa/code/microbit\_weatherbit\_oled

まだJavascript Block Editorは多少の不具合が残っているのかもしれませんが、手軽に使えるので今後の改良を期待します。
