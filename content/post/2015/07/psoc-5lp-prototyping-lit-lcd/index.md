---
title: "PSoC 5LP Prototyping Kitを動かしてみた（電圧計&amp;LCD編）"
date: 2015-07-12
slug: "psoc-5lp-prototyping-lit-lcd"
categories: 
  - "electronics"
image: "images/psoc_adc_lcd.jpg"
---

前回、PSoC 5LP Prototyping KitでLチカを行いましたが、CY8CKIT-059のサンプルとして用意されているADCとUARTを使った電圧計を動かしてみます。

サンプルプロジェクトを開きます。

![adc_uart_prj.PNG](images/adc_uart_prj.png) <!--more-->

TopDesignを開くと、ADCとUARTのコンポーネントが登録されており、この状態でビルドしてターゲットに書き込むと、電圧の数値がUART経由で表示できます。私の場合はTeraTermでUARTに接続しました。

![adc_uart01.PNG](images/adc_uart01.png)

UART経由でコマンドを入力することで、連続して計測したり、サンプリングして計測することができます。

ここで折角GPIO端子がたくさんあるので、電圧のLCD表示ができないかなと思いコンポーネントを探したところ、手持ちのLCD(HD44780)に適合するコンポーネントがありました。これをTopDesignにくみこみます。

![adc_uart_lcd_design.png](images/adc_uart_lcd_design.png)

次にPSoCのどのポートにLCDを接続するかを設定します。今回はP2\[0-6\]を使っています。こちらも図で確認できます。

![lcd_psoc_port.png](images/lcd_psoc_port.png)

LCDコンポーネットをクリックしたところ、ユーザ定義文字を定義する機能もあるようです。 ついでなのでカタカナ、ひらがなをデザインしてみました。

![lcd_user_defined.png](images/lcd_user_defined.png)

ここで設定したユーザ定義文字はLCD\_CustChars.cにフォントデータとして自動生成されます。

![lcd_customfonts_src.png](images/lcd_customfonts_src.png)

ここまで出来たら、main.cでLCDにも表示するように書き換えます。

ユーザ定義文字の表示は自動生成されたフォント名をLCD\_PutChar()に指定するだけです。

![lcd_font_putchar.png](images/lcd_font_putchar.png)

電圧表示はUARTに出力している文字列をそのままLCD\_PrintString()に渡すだけでお手軽です。

![lcd_adc_main.png](images/lcd_adc_main.png)

完成したものはこちらです。ユーザ定義文字もADCからの電圧もLCDに表示されています。

![psoc_adc_lcd.jpg](images/psoc_adc_lcd.jpg)

LCD表示についてはサンプルプログラムがありましたので、そちらを参考にすることで簡単に組み込むことができました。

他にもいろいろなデバイスがサポートされていますので、今後試していきたいと思います。
