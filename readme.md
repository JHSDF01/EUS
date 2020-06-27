# Enoden Unyo Simulator 取扱説明書

## 本プログラムについて

本製品　Enoden Unyo Simulator（以下、EUSと記載する）は、江ノ電運用から電車の在線位置を予想し、その後の運用変化に注目する、江ノ電運用監視ソフトウェアです。

## EUSの前提パッケージ

本製品では、ランタイムとして、Python 3.8を使用して動作確認を行っております。
また、起動用バッチファイルがWindows OSに依存します。Linux対応の予定は現状ありません。

## EUSの導入方法
EUSフォルダを任意のフォルダに配置します。


## EUSの実行方法
EUS_main.py がメインのファイルです。

### EUSのシミュレーションモードについて

EUSには現在シミュレーションモードが4種類あります。
|番号|曜日|モード|
|---|---|---|
|0|平日|出庫から入庫予測|
|1|休日|出庫から入庫予測|
|2|平日|日中から入庫予測|
|3|休日|日中から入庫予測|

- モード0と1では、早朝の車庫の在線状況から当日深夜の入庫までをシミュレートします。
- モード2と3では、日中11時の在線状況から当日深夜の入庫までをシミュレートします。

### EUSの起動方法とオプションについて
いかに起動オプションを示します。

```
py .\EUS_main.py 5 24 0.1 0
#　5時から24時まで、0.1秒ごと(10FPS)でアニメーション表示を行う。ダイヤは平日用を用いる。
```

```
py .\EUS_main.py 11 12 0.5 1
#　11時から12時まで、0.5秒ごと(2FPS)でアニメーション表示を行う。ダイヤは休日用を用いる。
```

```
py .\EUS_main.py 23 24 0.1 2
#　23時から24時まで、0.5秒ごと(2FPS)でアニメーション表示を行う。
ダイヤは平日用を用いて、日中運用から夜間入庫を予測する。
```


これを実行することで起動できます。

batファイルを実行することで、簡単に実行できます。


### 運用情報のロードおよびセーブ

データの保存は全て、```EUS\save```に配置されます。

#### 保存されるデータ一覧
- 出庫時点の車両の配置
- 入庫時点での車両の配置
- 午前11時時点での江ノ電運用（入力用JSON）
- 午前11時時点での江ノ電運用（出力用txt）

### 江ノ電運用シミュレーションのより具体的な方法

#### 運用予想の実行方法

複数のシミュレーションモードを使い分けることにより、数日後の江ノ電運用を予想します。
予想には、以下のような順番で、シミュレーションとセーブデータの移行を繰り返します。（Windowsのみ）
@import "EUS_holiday_simulate_20200622.bat" (line_begin =　0  line_end = 　5)

#### 運用予想の制約
運用予想では、観測される事実に基づいたシミュレーションを行っているため、
極楽寺検車区の出庫車両をトレースできていません。
そのため、現在は、入庫時間が最も短くなるような入出庫運用をシミュレーションに使用しています。
これは現状不正確なアルゴリズムであり、江ノ電運用を完全にシミュレートできるものではありません。

## EUSの削除方法
EUSフォルダをフォルダごと削除することで完了します。
