---
title: M5Paperで2020年から2021年への年越しをしてみました
date: 2021-01-01
slug: m5paper-newyear2021
categories:
- electronics
tags:
- m5stack
- 書き初め
image: images/m5paper_newyear2021.jpeg
---

あけましておめでとうございます。  
去年は[COSMACとTVディスプレイ回路で2020年の書き初め](https://kanpapa.com/2020/01/cosmac-tv-newyear2020.html "COSMACとTVディスプレイ回路で2020年の書き初めをしてみた")をしましたが、今年は最近購入した[M5Paper](https://www.switch-science.com/catalog/6749/?gclid=CjwKCAiAirb_BRBNEiwALHlnDzriTDCRUfqy6PTcpHEVW6BQQn6Oky4GWj35h5MslqxRq-XvnxdOlhoCGZYQAvD_BwE "M5Paper")で年越しをしてみました。  
M5Paperはまだ発売されて間もなく、Arduinoのライブラリにもつい最近登録された状態であまり事例がありません。メーカーから提供されている[API仕様](https://docs.m5stack.com/#/en/arduino/arduino_home_page?id=m5paper_api "Arduino IDE")をみながら、[サンプルプログラム](https://github.com/m5stack/M5EPD "M5EPD")を組み合わせて、試行錯誤でプログラミングしてみました。

今回作成した年越しプログラムは時計のように時刻を表示して、年を越した瞬間に画像を表示するという単純なものです。  
せっかくの電子ペーパーなので、TrueTypeフォントをSDカードに入れて、ピッタリくるフォントを表示してみました。

年を越した直後のM5Paperの画面です。

![m5paper_newyear2021.jpeg](images/m5paper_newyear2021.jpeg)

年越しの瞬間をYouTubeに載せておきました。

{{< youtube fbHZ5_Al60k >}}

プログラムはかなり適当に作成したものですが、GitHubに登録しておきました。

- [M5EPD\_HappyNewYear2021.ino](https://github.com/kanpapa/M5EPD/blob/main/M5EPD_HappyNewYear2021/M5EPD_HappyNewYear2021.ino "M5EPD_HappyNewYear2021.ino")

無事年を越すことができました。

本年もよろしくお願いします。
