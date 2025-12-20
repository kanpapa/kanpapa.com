---
title: 'ESP32でミニカーを作る #5 走行中に障害物を検知する（おおたfab 電子工作初心者勉強会）'
date: 2025-08-02
slug: otafab-esp32-minicar5
categories:
- electronics
tags:
- arduino
- esp32
- xiao
- otafab
- 電子工作
- otafab-esp32
image: images/otafab-esp32-minicar5-cars.jpg
---

[おおたfab](https://ot-fb.com/event)さんでは電子工作初心者勉強会を定期的に開催しています。

前回は[ESP32ミニカーのマイコン](https://kanpapa.com/2025/07/otafab-esp32-minicar4.html)に接続した超音波センサーを使用して距離を表示しました。しかし1秒間隔でしか距離が測れませんので障害物に気づくのが遅れてしまいます。今回はこの点を改良し、ミニカーを動かしながらリアルタイムで距離を計測できるようにします。これで障害物を避けることができます。

## リアルタイムで距離を計測する

前回までのプログラムは１秒間隔で距離を測って表示することしかできないので実用的ではありません。もう少し工夫をする必要があります。ここでは2通りの方法を試してみました。

### カウンタを使う方法

なぜ1秒間隔でしか計測できないのかは、メインループにdelay(500)が2か所あるので、この0.5秒×2回の間は何もできないためです。このため以下のように1秒に1回しか距離が測れません。

1. 左側に曲がるようにモーターを回す

3. 0.5秒待つ

5. 右側に曲がるようにモーターを回す

7. 0.5秒待つ

9. 距離を測る　←つまり、1秒に1回しか実行されない

11. 1.に戻る

ここで距離を測るタイミングを短くするためにメインループをもっと速くまわすようにします。この例ではループを1ミリ秒に1回とし、ループ回数をカウントする変数を用意して、その変数が特定の値になったら処理を実行することで、上記とほぼ同じ処理を実現します。

1. カウンタ変数を0に初期化する

3. カウンタ変数が０の場合は、左側に曲がるようにモーターを回す

5. カウンタ変数が500の場合は、右側に曲がるようにモーターを回す

7. カウンタ変数が333で割り切れたら距離を測る　←ここでは、333, 666, 999の3回で距離を測ります。

9. 1ミリ秒待つ

11. カウンタ変数に1加算する。1000になったら1.に戻る。

13. 2.に戻る

なお、距離を測る部分の処理時間を短くするためにデバック用の出力やインチの計算部分は削除しました。

ソースコードはこちら（esp32\_mouse5\_dest\_loop.ino)

```
//-----------------------------------------------------
// esp32_mouse5_dest_loop.ino
// 
// for XIAO ESP32C6
//
// 2025/07/29
//-----------------------------------------------------
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const int TRIG_PIN = 18;
const int ECHO_PIN = 20;

// Anything over 400 cm (23200 us pulse) is "out of range"
const unsigned int MAX_DIST = 23200;

/* XIAO ESP32C6
DRV       ESP32
---------------
AIN1 --- GPIO0
AIN2 --- GPIO1
BIN1 --- GPIO2
BIN2 --- GPIO21
*/

const int LP = 0; // AIN1   LEFT PLUS
const int LM = 1; // AIN2   LEFT MINUS
const int RP = 2; // BIN1   RIGHT MINUS
const int RM = 21; // BIN2   RIGHT PLUS

void setup()
{
  Serial.begin(9600);

  // The Trigger pin will tell the sensor to range find
  pinMode(TRIG_PIN, OUTPUT);
  digitalWrite(TRIG_PIN, LOW);

  //Set Echo pin as input to measure the duration of 
  //pulses coming back from the distance sensor
  pinMode(ECHO_PIN, INPUT);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();
  display.setTextSize(3);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("Hello, world!"));
  display.display();
  delay(2000);

  analogWrite(LP,0);
  analogWrite(LM,0);
  analogWrite(RP,0);
  analogWrite(RM,0);
}

void loop() //RUN ZIGZAG
{
  for (int count = 0; count < 1000; count++) {  
    if (count == 0) TTL();
    if (count == 500) TTR();
    if (count % 333 == 0) {
      display.clearDisplay();
      display.setTextSize(3);                 // Normal 1:1 pixel scale
      display.setTextColor(SSD1306_WHITE);    // Draw white text
      display.setCursor(0,0);                 // Start at top-left corner
      display.println(dest());                // cm値をディスプレイに表示
      display.display();
    }
    delay(1);  // 1ms
  }
}

void TTL(void) // trun to left
{
  analogWrite(LP,250);
  analogWrite(RP,100);
}

void TTR(void) // trun to right
{
  analogWrite(LP,100);
  analogWrite(RP,250);
}

float dest()
{
  unsigned long t1;
  unsigned long t2;
  unsigned long pulse_width;
  float cm;

  // Hold the trigger pin high for at least 10 us
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Wait for pulse on echo pin
  while ( digitalRead(ECHO_PIN) == 0 );

  // Measure how long the echo pin was held high (pulse width)
  // Note: the micros() counter will overflow after ~70 min
  t1 = micros();
  while ( digitalRead(ECHO_PIN) == 1);
  t2 = micros();
  pulse_width = t2 - t1;

  // Calculate distance in centimeters and inches. The constants
  // are found in the datasheet, and calculated from the assumed speed
  //of sound in air at sea level (~340 m/s).
  cm = pulse_width / 58.0;
  return(cm);
}
```

このプログラムを実行させたところモーターを動かしながら、リアルタイムで距離の表示が行えるように改善されました。動画では確認しにくいですが、ジグザグに走行しつつ、刻々と距離の値が変わっています。

{{< youtube ZeHOPXjWS54 >}}

### Tickerライブラリを使う方法

もう一つの方法としてTickerというライブラリを使用することで設定した時間ごとにあらかじめ設定した関数を呼び出すことができます。いわゆるタイマー割り込みです。

サンプルプログラムが用意されているのでそれを試してからサンプルプログラムの内容を組み込んでみます。

#### Tickerのサンプルプログラムを動かしてみる

TickerのサンプルプログラムはArduino IDEのファイル→スケッチ例→XIAO ESP32 C6のスケッチ例→Ticker→TickerBasicにあります。

このサンプルプログラム TickerBasic.ino ではsetup()で0.3秒ごとにflip()を呼び出すように設定したあとは、loop()を無限ループの状態としています。

実際に動作させるとLEDの点滅が始まり、20回点滅したあとは0.1秒ごとにflip()を呼び出すように再設定し、さらに120回点滅したあとは点滅を停止させる処理を行っています。詳細はソースコードを参照してください。

#### Tickerライブラリを組み込んでみる

TickerライブラリをTickerBasic.inoを参考にしながらミニカーのプログラムに組み込んでみました。今回は距離を求めて表示する部分を0.3秒ごとに呼び出すことにします。また、求めた距離をグローバル変数に置くことでloop()の中からいつでも最新の距離を参照できるようにしました。

ソースコードはこちら（esp32\_mouse5\_dest\_ticker.ino)

```
//-----------------------------------------------------
// esp32_mouse5_dest_ticker.ino
// 
// for XIAO ESP32C6
//
// 2025/07/29
//-----------------------------------------------------
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#include <Ticker.h>
Ticker flipper;

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const int TRIG_PIN = 18;
const int ECHO_PIN = 20;

// Anything over 400 cm (23200 us pulse) is "out of range"
const unsigned int MAX_DIST = 23200;

/* XIAO ESP32C6
DRV      ESP32
---------------
AIN1 --- GPIO0
AIN2 --- GPIO1
BIN1 --- GPIO2
BIN2 --- GPIO21
*/

const int LP = 0; // AIN1   LEFT PLUS
const int LM = 1; // AIN2   LEFT MINUS
const int RP = 2; // BIN1   RIGHT MINUS
const int RM = 21; // BIN2   RIGHT PLUS

float cm = 0.0;    // 最新の距離を保持するグローバル変数

void setup()
{
  Serial.begin(9600);

  // The Trigger pin will tell the sensor to range find
  pinMode(TRIG_PIN, OUTPUT);
  digitalWrite(TRIG_PIN, LOW);

  //Set Echo pin as input to measure the duration of 
  //pulses coming back from the distance sensor
  pinMode(ECHO_PIN, INPUT);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();
  display.setTextSize(3);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("Hello, world!"));
  display.display();
  delay(2000);

  analogWrite(LP,0);
  analogWrite(LM,0);
  analogWrite(RP,0);
  analogWrite(RM,0);

  // flip the pin every 0.3s
  flipper.attach(0.3, flip);         // 0.3秒おきにflip関数を呼び出すように設定
}

void loop() //RUN ZIGZAG
{
  TTL();
  delay(500);
  TTR();
  delay(500);
}

void flip() {
  cm = dest();                            // 距離を取得してグローバル変数に入れる

  display.clearDisplay();                 // OLED画面をクリアする
  display.setTextSize(3);                 // 文字サイズを3にする
  display.setTextColor(SSD1306_WHITE);    // 文字の色を白にする
  display.setCursor(0,0);                 // カーソルを左上隅に設定する
  display.println(cm);                    // 距離をディスプレイに表示
  display.display();
}

void TTL(void) // trun to left
{
  analogWrite(LP,250);
  analogWrite(RP,100);
}

void TTR(void) // trun to right
{
  analogWrite(LP,100);
  analogWrite(RP,250);
}

float dest()
{
  unsigned long t1;
  unsigned long t2;
  unsigned long pulse_width;
  float dest_cm;

  // Hold the trigger pin high for at least 10 us
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Wait for pulse on echo pin
  while ( digitalRead(ECHO_PIN) == 0 );

  // Measure how long the echo pin was held high (pulse width)
  // Note: the micros() counter will overflow after ~70 min
  t1 = micros();
  while ( digitalRead(ECHO_PIN) == 1);
  t2 = micros();
  pulse_width = t2 - t1;

  // Calculate distance in centimeters and inches. The constants
  // are found in the datasheet, and calculated from the assumed speed
  //of sound in air at sea level (~340 m/s).
  dest_cm = pulse_width / 58.0;
  return(dest_cm);
}
```

このプログラムを実行させたところカウンタのときと同様にリアルタイムで距離が表示されるように改善されました。

{{< youtube vbxXOHe1Cao >}}

## 障害物を検知してみる

応用例として障害物との距離が10cm以下になったら停止するようにしました。ソースコードの変更箇所はloop()に距離の判断を加え、STOP()という関数を新しく作りモーターを止めるようにしています。

```
void loop() //RUN ZIGZAG
{
  TTL();
  delay(500);
  TTR();
  delay(500);

  if (cm < 10.0) STOP();
}

void STOP(void)
{
  analogWrite(LP,0);
  analogWrite(RP,0);

  while(1);
}
```

このプログラムでのテスト走行の動画です。ジグザグで走っているところに障害物を置いてみます。

{{< youtube vzfJDs_re5o >}}

直前で停止してくれました。かなりギリギリなので停止する距離やモーターの速度などは調整する必要がありそうです。また、このコードは確実に停止するように一回STOPしたらその後は無限ループとしています。

## 次回

これまではジグザグに前進するだけでしたが、距離センサーの値を使って障害物を避けながらあちこち動き回る車に拡張することを試してみます。
