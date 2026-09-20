---
title: 'Arduino UNO Qでモーションセンサーを使ってみた'
date: 2026-09-19T09:43:15+09:00
slug: 'arduino-uno-q-mpu6050-webui'
tags: [Arduino, UnoQ, MPU6050, AppLab, WebUI, IMU]
categories: [Electronics]
image: 'arduino-uno-q-mpu6050.jpg'
---

## はじめに

前回はArduino App LabのBrickを使って[LEDの点灯状態をブラウザにリアルタイム表示する実験](/2026/09/arduino-uno-q-blink-led-webui.html)を行いました。  
今回は手持ちの6軸慣性センサー **MPU6050（GY-521モジュール）** をUNO QにI2Cで接続し、慣性センサーの状態をブラウザにリアルタイム表示してみます。

![今回接続するMPU6050(GY-521モジュール)](mpu6050-gy-521-module.jpg)

全体の処理分担と構成方針は以下のようにシンプルにしました。

- **MCU側（sketch）**：MPU6050から生データを読み取り、姿勢角（roll / pitch / yaw）まで計算する
- **Python側（Linux側）**：Bridge経由でその計算結果を受け取り、WebUI（Socket.IO）へ配信する

100Hz程度の等間隔サンプリングが必須となる積分処理を、Linux側のスケジューラによる揺れから切り離したかったのが主な理由です。

## ハードウェア構成

GY-521モジュール（MPU6050搭載）をUNO Qに接続します。

| MPU6050 | UNO Q | 備考 |
|---|---|---|
| VCC | 3V3 | UNO QのGPIOは5Vトレラントではないため3.3Vを供給 |
| GND | GND | |
| SDA | SDA（D20）| ※従来のArduino UnoでのA4ではなく、D20に接続（詳細は後述） |
| SCL | SCL（D21）| ※従来のArduino UnoでのA5ではなく、D21に接続（詳細は後述） |
| AD0 | GND または未接続 | 未接続でも内部プルダウンによりI2Cアドレスは `0x68` |

MPU6050の設定パラメータは、DLPF 44Hz、±250dps、±2g といった標準的な値にしています。加速度センサから算出した絶対角と、ジャイロセンサの積分値を相補フィルタ（α=0.98）でブレンドして roll / pitch を求めました。なお、yawに関しては地磁気センサがないためジャイロ積分のみ（ドリフトを含む相対値）としています。

## MPU6050のスケッチライブラリの追加

スケッチを書く前にArduinoのMPU6050のライブラリをインストールします。すでに有名なセンサーであれば便利なライブラリが揃っており、Arduino App Labでも利用できます。

Arduino App LabのAdd Sketch Libraryのアイコンをクリックするとライブラリのリストが表示されます。今回は`Adafruit MPU6050`を使用しました。

![Sketch Librariesの画面](add-arduino-mpu6050-library.png)

ライブラリが追加されると`Sketch Libraries`に表示されます。

![Sketch Librariesの画面](sketch-libraries-mpu6050.png)

## I2Cが繋がらない

配線を済ませてsketchを書き込み、生値を読んでみたところLOGでは加速度もジャイロもすべて0しか返ってきていません。

```
[4:57:08 PM] WHO_AM_I=0xFF  acc=(0.0, 0.0, 0.0)  gyr=(0.0, 0.0, 0.0)
[4:57:06 PM] WHO_AM_I=0xFF  acc=(0.0, 0.0, 0.0)  gyr=(0.0, 0.0, 0.0)
[4:57:03 PM] WHO_AM_I=0xFF  acc=(0.0, 0.0, 0.0)  gyr=(0.0, 0.0, 0.0)
```

ここから原因究明のための切り分け作業を行いました。

1. GY-521モジュールの電源LEDは点灯している → 電源供給は正常
2. テスターによるI2Cラインの導通確認 → 配線・接触自体には問題なし
3. [Uno Qのピンアウト](https://docs.arduino.cc/resources/pinouts/ABX00162-full-pinout.pdf)を見直したところ、D20/D21に別のI2Cポート(I2C2)の記載があったため、配線をD20/D21コネクタ側へ差し替えたところ、無事にセンサーの値が返ってきました。

```
[5:01:16 PM] WHO_AM_I=0x68  acc=(0.213, -0.409, 9.977)  gyr=(-2.908, 0.802, -0.191)
[5:01:10 PM] WHO_AM_I=0x68  acc=(0.186, -0.427, 9.972)  gyr=(-3.0, 0.779, -0.145)
[5:01:05 PM] キャリブレーション完了 (bias gx=-2.78 gy=0.748 gz=-0.17 deg/s)
[5:01:04 PM] キャリブレーション開始… 基板を静止させてください
[5:01:01 PM] 接続しました。UNO Q を静止させてからキャリブレーションしてください。
```

> UNO QではA4/A5(I2C3)とD20/D21(I2C2)とQwiic(I2C4)はそれぞれ独立したI2Cインターフェースです。I2Cが認識されないときは、従来のArduino感覚で`A4`/`A5`を使うのではなく、もう一つの`SDA`/`SCL`（数字の付いていないピン）に接続して確認してみてください。

![I2Cで通信できるようになったArduino Uno QとMPU6050](arduino-uno-q-mpu6050.jpg)

## Bridge APIの設計

MCUとPython（Linux）間の通信は、メソッド名やデータ型を厳密に固定して設計しました。ここが1文字でも異なると、例外エラーも出ずに無言で通信が失敗してしまうため注意が必要です。

**MCU → Python（push）**

MCU側で相補フィルタ処理を施した姿勢角などの計算結果を、Linux（Python）側へ定期配信（ストリーミング）するAPIです。MCUからの片方向通知のため、4つの値をダイレクトに引数として渡しています。

| メソッド名 | 説明　| 引数 | 配信周期 |
|---|---|---|---|
| `imu_data` | 算出済みの姿勢角と温度をまとめて通知  | `roll, pitch, yaw, temp` (float×4) | 20Hz (50ms間隔) |


```python
# Python側の受信ハンドラ例
Bridge.provide("imu_data", on_imu_data)

def on_imu_data(roll: float, pitch: float, yaw: float, temp: float):
```

**Python → MCU（call）**

Python側からMCUの処理をオンデマンドで実行するAPIです。App LabのBridge内部で使われている msgpack-RPC の仕様上、「戻り値として単一の値しか返せない」 ため、複数の戻り値はすべてJSON文字列にエンコードして返却しています。また、引数を取らない処理でもRPC仕様に合わせてダミー引数（dummy: int）を渡すようにしています。

| メソッド名 | 説明 |  引数 | 戻り値（JSON文字列） |
|---|---|---|---|
| `imu_calibrate` | 静止状態でのバイアス測定・補正を実行 | samples: int (サンプリング数) | バイアス値 `{"bias_gx": -2.78, ...}` |
| `imu_reset_yaw` | ドリフトしたYaw角を 0 にリセット | dummy: int (0) | 実行結果 `{"ok":true}` |
| `imu_read_raw` | センサー値（加速度・角速度）を即時取得 |dummy: int (0) | 測定値　`{"ax": ..., "gx": ...}` |

```python
# Python側の同期呼び出し例
res = json.loads(Bridge.call("imu_calibrate", 500, timeout=10)) # 500サンプルでキャリブレーション

Bridge.call("imu_reset_yaw", 0, timeout=5)  # 引数不要な処理もダミーの0を渡して呼ぶ
```

## WebUI表示とCSS 3Dによる姿勢の可視化

WebUI-HTML Brickを使用し、Python側からSocket.IO経由で送られてくる姿勢データをブラウザ上でリアルタイム表示します。

今回はThree.jsなどの重い3Dライブラリは使わず、CSSの3Dトランスフォーム（perspective と rotateX/Y/Z） だけで、センサーの動きと画面内の板が滑らかに連動する軽量な3Dビューアを構築しました。

### HTML / CSSの構造
親要素に perspective（視点・奥行き感）を指定し、子要素に preserve-3d を指定することで、ブラウザ空間に擬似的な3Dプレーンを作成します。

HTML
```html
<!-- 3D表示エリアのHTML -->
<div class="scene3d">
  <div id="board" class="board3d">
    <span>UNO Q</span>
  </div>
</div>
```

CSS
```css
/* 3D空間の定義 */
.scene3d {
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 700px;  /* 奥行き感を指定 */
}

/* 傾ける板のスタイル */
.board3d {
  position: relative;
  width: 160px;
  height: 90px;
  transform-style: preserve-3d;
  transition: transform 0.08s linear; /* imu_updateの間隔(約100ms)に合わせて滑らかに */
  transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
}
```
### JavaScript（Socket.IO受信と姿勢反映）

Python側から10Hz周期でbroadcast配信される imu_update イベントを受信し、バー表示の数値更新と同時に、CSSの transform プロパティを直接書き換えて板を回転させます。

```javaScript
const socket = io();
const board = document.getElementById('board');

socket.on('imu_update', (data) => {
  // 1. 数値・バー表示の更新
  document.getElementById('val-roll').textContent = data.roll.toFixed(1);
  document.getElementById('val-pitch').textContent = data.pitch.toFixed(1);
  document.getElementById('val-yaw').textContent = data.yaw.toFixed(1);

  // 2. CSS 3Dトランスフォームの適用
  // ※回転軸とモジュールの向きを合わせるため、pitchは正負を反転させています
  board.style.transform = 
    `rotateZ(${data.roll}deg) rotateX(${-data.pitch}deg) rotateY(${data.yaw}deg)`;
});
```

### 実装のポイント

- 回転軸の整合（座標合わせ）：画面上の板の見え方と実際のセンサーモジュールの傾きを一致させるため、ピッチ角にマイナス符号（-data.pitch）を当てています。
- transition によるスムージング：Socket.IOの配信周期（約10Hz）に合わせて transition: transform 0.08s linear; を効かせることで、カクつきのない滑らかな追従アニメーションを実現しました。
- 徹底した型の管理：前回のLチカ実験で遭遇した「文字列と真偽値の型不一致」の教訓を踏まえ、受信する角度データはすべて数値型（Number）として厳密に扱い、画面表示時のみ .toFixed(1) でフォーマットしています。

## 完成したWebUI

MPU6050モジュールを手で傾けると、WebUI画面内の板が連動してリアルタイムに同じ方向へ傾いてくれます。CSSの3Dトランスフォームだけでここまで手軽に視覚化できるのは、嬉しい発見でした。

![完成したWebUI](arduino-uno-q-mpu6050-imu-monitor.png)

{{< youtube _hpNdtfZpAQ >}}


## まとめ

- MPU6050（GY-521）自体のI2C制御や相補フィルタ計算は定番の手法で問題なく動作し、Arduino IDEでおなじみのライブラリもスケッチで利用できました。
- 今回最大のハードルは、UNO QのI2Cピン配置が従来のArduinoシールド配置（A4/A5）とは異なっていたことでした。
- Bridge経由でPython側にデバッグ情報を中継し、WebUIに表示することで、デバッグをスムーズに行うことができました。
- Bridge APIを定義する際は、メソッド名と型をあらかじめ仕様書として固めておくことで手戻りを防げます。
- CSSの3Dトランスフォームで、センサデータの表示を立体的に表現できました。

今回のスケッチおよびPythonスクリプト一式は、[GitHubリポジトリ](https://github.com/kanpapa/mpu6050-monitor) に公開しています。
