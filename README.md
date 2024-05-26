# DALL·E 3
## 画像生成AI
OpneAI社の画像生成AI'DALL·E 3'の使い方  
Pythonバージョン
## 仮想環境について
これはおまけ情報(仮想環境について)
```
python3 -m venv .venv
deactivate
```
## 画像生成の方法
1. 仮想環境に入る  
    ```
    . .venv/bin/activate
    ```
1. main.py がプログラム本体なので開く
1. プロンプトを入れて保存する
1. zshなどから
    ```
    python3 main.py
    ```
    を実行する
1. 生成された画像のURLがpythonよりprintされるのでそちらを開く
1. ブラウザが立ち上がるので表示された画像を保存

## 注意点
- OSの環境変数にOpenAIのシークレットキーを保存しておく  
変数名は”OPENAI_API_KEY_for_DALLE3”  
この際venvの仮想環境内からzshより
    ```
    export OPENAI_API_KEY_for_DALLE3='ここにシークレットキー'
    ```
    で設定すれば仮想環境内の環境変数に設定できるので安心  
    またターミナルから下記コマンドで環境変数一覧を確認できる
    ```
    printenv
    ```
## DALL·E 2の画像から画像生成について
img2img.pyに、元画像とマスク画像のセットを記述して、変更内容のプロンプトを書く。  
生成された画像はDALL·E 2なので精度が低い。。  
サンプルとしてjkフォルダを作ってそこにjkの絵が入っている。