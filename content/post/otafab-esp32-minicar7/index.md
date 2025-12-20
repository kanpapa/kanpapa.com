---
title: "ESP32でミニカーを作る #7 マイクロマウスに挑戦（おおたfab 電子工作初心者勉強会）"
date: 2025-12-20
slug: otafab-esp32-minicar7
categories:
- electronics
tags:
- arduino
- esp32
- xiao
- otafab
- 電子工作
- otafab-esp32
image: otafab-esp32-minicar7.jpg
draft: true
---

[おおたfab](https://ot-fb.com/event)さんでは電子工作初心者勉強会を定期的に開催しています。

[前回](https://kanpapa.com/2025/08/otafab-esp32-minicar6.html)はESP32マイコンで動くミニカーで前後左右回転などの動きを実装しました。今回は超音波センサーだけでどこまでマイクロマウスに迫ることができるか試してみます。初心者勉強会なのでGoogleのGeminiにプログラムを助けてもらいながら進めます。

## Geminiはソースコードをどこまで理解できるのか

今回はGeminiの助けを借りてプログラミングしていきます。まずは[これまで作成したプログラム](https://github.com/kanpapa/esp32-minicar/blob/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_0/esp32_mouse2_move_to_4_direction_and_rolate_0.ino)を読み込ませて、仕様書をまとめてもらうことでソースコードだけでどこまで理解しているのかをためしてみます。プロンプトはシンプルなものにしました。

「このプログラムの仕様書を作成してください。」

表示された結果は素晴らしいものでソースコードのコメントも使って分析しているようです。一部を以下に示します。全文は[GitHub](https://github.com/kanpapa/esp32-minicar/blob/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_0/README.md)に登録しました。

>> **XIAO ESP32C6 Micro-Mouse Robot Control**
>>
>> このプロジェクトは、**Seeed Studio XIAO ESP32C6** を搭載した小型二輪ロボット（マイクロマウス）向けの制御プログラムです。
>> 
>> ロボットはあらかじめ定義されたパターン（前後左右・回転）で走行し、同時にバックグラウンド処理で超音波センサーによる距離計測を行い、その結果をOLEDディスプレイにリアルタイム表示します。
>> 
>> 📝 概要
>>
>> ファイル名: `esp32_mouse2_move_to_4_direction_and_rolate.ino`
>>
>> このスケッチは以下の2つのタスクを並行して実行します：
>> 1.  **動作制御 (Main Loop)**: 前進、後退、旋回、回転、停止を組み合わせた「ZIGZAG」パターンを繰り返します。
>> 2.  **距離測定と表示 (Ticker)**: `Ticker`ライブラリを使用し、0.3秒ごとに超音波センサーで距離を計測し、OLEDに数値とバーで表示します。
>> 
>> 🛠 ハードウェア構成
>>
>> * **マイコン**: Seeed Studio XIAO ESP32C6
>> * **ディスプレイ**: SSD1306 0.96インチ OLED (I2C接続)
>> * **センサー**: HC-SR04 超音波距離センサー
>> * **モータードライバ**: Hブリッジモータードライバ (2モーター制御用)
>> * **モーター**: DCモーター x 2 (左車輪・右車輪)


## OLEDに表示する内容を変更する

次に簡単な修正をお願いしてみました。OLEDには現在超音波センサーの計測結果が表示されています。これに加えて現在の移動方向を表示してもらうように指示してみました。プロンプトは以下の通りです。

「ロボットがどの動きを行っているのかOLEDに英語で表示するようにプログラムを修正してください。」

* [Ver.1 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_1)

「距離表示を一旦コメントにしておいて、動きの表示を最大限大きな文字で表示するようにしてください。動作時間は1000ミリ秒のところをすべて5000ミリ秒にしてください。」

* [Ver.2 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_2)

いずれも指示した通りにスケッチを修正してくれました。コンパイルエラーもなく満足できるものでした。

## ロボットの動きを指定してみる

次にもう少し複雑な変更をお願いしてみました。ロボットが正方形を描くようにしてもらいます。ここではまだ超音波センサーの情報は使用していません。

「今の状態はいろいろな動きをするようにしていますが、これを一旦コメントアウトしておいて、右方向に90度を４回曲がるプログラム修正してください。」

* [Ver.3 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_3)


「回転させる時間を400ミリ秒に修正し、それぞれの回転の間に1000ミリ秒直進の動作を追加して四角形を描くように移動させてください。」

* [Ver.4 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_4)

「回転の時間を600ミリ秒に修正し、直進動作を2000ミリ秒に修正してください。」

* [Ver.5 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_5)

指示を行うとその動きをスケッチに反映してくれました。

2台使って同じような動きができるかのテスト中の動画です。

{{<youtube mXTZhfzXsoA>}}

## 袋小路から脱出できるようにしてみる

「600ミリ秒で90度回転するようになりました。このロボットで迷路を脱出するアルゴリズムを実装してください。」

* [Ver.6 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_6)

「距離測定後、2秒間前進してしまいます。走行中も常に距離測定を行い、常に衝突判定をしてください。」

* [Ver.7 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_7)

「回転動作の際に、ほぼ180度回転して後ろに戻ってしまいます。修正してください。」

* [Ver.8 プロンプトと結果](https://github.com/kanpapa/esp32-minicar/tree/main/Arduino/esp32_mouse2_move_to_4_direction_and_rolate_8)

このように何度か状況を伝えてプログラムを修正していくことで目的の動作ができるようになりました。

最終版での走行動画です。

{{<youtube o7T2DnxdKjs>}}

## まとめ

ついでに今日の勉強会で行った作業をGeminiにまとめてもらいました。

「無事想定通りの動作になりました。本日の検討内容を要約してください。」

* [開発ログ: ESP32ミニカー　迷路脱出アルゴリズムの実装](https://github.com/kanpapa/esp32-minicar/blob/main/Arduino/DEVLOG.md)

また次のステップについても提案してもらいました。

「このロボットを使って迷路以外の面白そうな動作はできますか？」

* [アイデア集: 迷路探索以外の動作パターン](https://github.com/kanpapa/esp32-minicar/blob/main/Arduino/NEXTSTEP.md)


このようにGeminiを活用することで今後の勉強会も楽しいものになりそうです。
