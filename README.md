# What's this
香川GoToEatキャンペーンのページ(https://www.kagawa-gotoeat.com)にある使えるお店リストをJSON形式で全部取ってくるだけのプログラムです。

# requirements
python3 と BeautifulSoup4が必要です。
python3が既にインストールされた環境なら次のコマンドでセットアップができます。
```
pip install -r  requirements.txt
```

# How to use
環境変数`BASE_URL`にお食事券が使える店のURLを指定して main.py を実行してください。

Unix環境ならだいたい次のコマンドで使えるはず

```
BASE_URL=https://www.kagawa-gotoeat.com/gtes/store-list python3 main.py
```

# options
出力されるJSON文字列はデフォルトでは改行等がありませんが、`-i`または`--indent`オプションで数値を指定すると、整形した文字列を出力します。
