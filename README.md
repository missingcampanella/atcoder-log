# atcoder-log
AtCoderの学習記録リポジトリです。回答コード・学んだアルゴリズム・自作ツールをまとめています。

---
 
## ツール：難易度自動分類スクリプト
 
### 概要
 
[AtCoder Problems API](https://kenkoooo.com/atcoder/resources/problem-models.json) から問題の難易度を自動取得し、ファイルを難易度別フォルダに振り分けるスクリプト。
 
### 難易度の分類基準
 
| difficulty | 色 |
|---|---|
| 〜 399 | gray |
| 400 〜 799 | brown |
| 800 〜 1199 | green |
| 1200 〜 1599 | cyan |
| 1600 〜 2399 | blue |
| 2400 〜 2799 | yellow |
| 2800 〜 3199 | orange |
| 3200 〜 | red |
| データなし | unclassified |
 
### 使い方
 
```bash
python sorter.py
```
 
`source_dir`（移動元）と `dest_base_dir`（移動先）はスクリプト末尾の `main()` で変更できます。
 
```python
if __name__ == "__main__":
    main(
        source_dir="./atcoder-sorter",
        dest_base_dir="./difficulty"
    )
```
 
### 動作環境
 
- Python 3.14.3
- `requests`（`pip install requests` でインストール）
- `pathlib`（標準ライブラリ）
---
 
## 実装時に学んだこと
 
### requests ライブラリ
 
外部APIにHTTPリクエストを送るライブラリ。
 
```python
response = requests.get("https://example.com/api/data.json")
data = response.json()  # レスポンスをdictに変換
```
 
通信失敗に備えて `try / except requests.RequestException` でエラーハンドリングする。
 
### pathlib
 
ファイルパスを扱う標準ライブラリ。文字列よりも直感的に書ける。
 
```python
from pathlib import Path
 
dir_path = Path("./problems")
 
for file in dir_path.iterdir():
    print(file.stem)   # 拡張子なしのファイル名
    print(file.name)   # 拡張子ありのファイル名
```
 
`/` 演算子でパスを連結できる。
 
```python
dest = Path("./sorted") / "gray"  # → ./sorted/gray
dest.mkdir(parents=True, exist_ok=True)  # フォルダがなければ作成
```
 
### shutil.move
 
ファイルを移動する標準ライブラリ。
 
```python
import shutil
shutil.move(str(src_path), str(dest_path))
```
 
### APIのキー形式の違いへの対処
 
ABC019以前の問題はAPIのキーが `abc019_1` 形式（`a`→`1`）になっている。
ファイル名（`abc019_a`）と一致しないため、見つからない場合は変換して再検索する処理を実装した。
 
```python
mapping = {"a": "1", "b": "2", "c": "3", "d": "4"}
```
 
---
 
## ファイル命名規則
 
```
abc001_a.py
abc123_b.cpp
```
 
`{コンテスト名}{回数}_{問題番号}.{拡張子}` の形式で統一する。
