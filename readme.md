# DISCORDでのTRPG用DICE_BOT

## 初回
`pip install -r requirements.txt`

## 実行
`python dice.py`


## 準備
* tokens.py
    - BOT_TOKEN
        + DISCORDのBOTのtoken

## コマンドと動作例
* ダイスロール
    * /d → 1d100を自動で降る
    * /d 2d6 → 2d6を自動で降る
    
    * /ダイス → 1d100を自動で降る
    * /ダイス 2d6 → 2d6を自動で降る
        - 全角、半角のスペースに対応

* KP用ダイス
    * /hd →　自分以外プレイヤーの1d100を行って、DMで送ってくる
    * /hd 2d6 →　自分以外プレイヤーの2d6を行って、DMで送ってくる
        - ※ボットの起動後、プレイヤーがbotのいるチャンネルでチャットすることで、プレイヤーを認識する
        - ※DMで打っても反応するので、KP用の機能

* 対抗ロール
    * /cr 能動　受動
    * /cr 12 16 → 1d100を自動で降る
    * /cr 12 16 2d100 → 2d100を自動で降る