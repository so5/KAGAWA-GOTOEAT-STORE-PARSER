# What's this
香川GoToEatキャンペーンのページ (https://www.kagawa-gotoeat.com) で公開されている、お食事券が使える店舗リストをJSON形式で出力するだけのプログラムです。

# requirements
python3 と BeautifulSoup4が必要です。
python3が既にインストールされた環境なら次のコマンドでセットアップができます。
```
pip install -r  requirements.txt
```

# How to use
環境変数`BASE_URL`にお食事券が使える店舗リストのURLを指定して main.py を実行してください。

Unix環境ならだいたい次のコマンドで使えるはず

```
BASE_URL=https://www.kagawa-gotoeat.com/gtes/store-list python3 main.py
```

# options
出力されるJSON文字列はデフォルトでは改行等がありませんが、`-i`または`--indent`オプションで数値を指定すると、整形した文字列を出力します。

# output
店舗情報は次のプロパティを持ちます。

- name: 店舗名
- map_url: google map上でのその店舗のURL
- address: 住所
- TEL: 電話番号
- area: 香川GoToEatキャンペーンぺーじでの住所区分
- genre: 登録されている料理ジャンル

香川GoToEatキャンペーンのページで検索した際に表示される内容をそのまま出力しているだけですが、店舗名に含まれる全角スペースは半角スペースに変換しています。

# Disclaimer
本プログラムは香川GoToEatキャンペーンのウェブサイトにて公開されている情報を取得し、整形して出力する機能のみを提供しています。表示される内容の正確性については保証するものではありません。

