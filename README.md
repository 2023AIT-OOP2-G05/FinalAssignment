# アプリ名

## 担当箇所

担当今井<br>
・チェックボックスの作成と選択画像の保存<br>
・各ページのレイアウト作成<br>
・問題ページの作成(一つ作成させておく)<br>
・アップロードページとTopページの変更<br>
・アップロード画像の消去機能のレイアウト作成<br>

担当都築<br>
・アップロード部分の作成、保存
・アップロード画像の消去機能の作成<br>
・ボタンと画像を一致させる判定の作成<br>
・問題ランダム選択機能作成<br>
・画像処理関数の再構成<br>

画像処理問題の解説ページ作成

担当山口<br>
・正誤ページの作成(学習できるように単語の意味をつける)<br>
・全体のcssの作成<br>

担当高野<br>
・正誤ページの作成(学習できるように単語の意味をつける)<br>
・発表資料の作成の作成<br>

画像処理問題作成

担当いざわ<br>
・写真基礎単語問題の作成<br>
・単語問題と全体のcssの作成

担当すぎやま<br>
・画像処理の関数作成(色抜き問題)
・単語問題と全体のcssの作成

担当田川<br>
・画像処理の関数作成(写真基礎問題)
・単語問題と全体のcssの作成

## ディレクトリ構造


## 画像処理の番号分け
担当すぎやま<br>
 色抜き問題<br>　　　
0 青抜き　blueCut.py<br>
1 赤抜き　redCut.py<br>
2 緑抜き　greenCut.py<br>
3 青赤半分 blueRedHalf.py<br>
4 青緑半分 blueGreenHalf.py<br>
5 赤緑半分 redCut.py<br>

担当たがわ<br>
写真基礎問題<br>
0 色温度　  colorTemperature.py<br>
1 色被り補正  colorCastCorrection.py<br>
2 彩度 saturation.py<br>
3 露光量 exposureAmount.py<br>
4 コントラスト contrast.py<br>
5 ハイライト　highlight.py<br>

# 問題（クイズ）のページ
## 画像選択とレベル（ジャンル)選択ページ<br>
・選択された画像と選択されたレベルがわかるように保存？する<br>
・
## 問題のページ<br>
・ランダムで問題を表示する（二値化やグレースケールの画像を準備）<br>
・選択された画像（画像処理済み）とボタンの正誤<br>
・<br>
## 解説ページの作成<br>
・単語の意味を載せる<br>
例　二値化　　二値化処理は、分析対象の画像を白と黒の2色のみに変換する画像処理です。二値化処理によって画像と背景の境界を明確化させることで、処理速度を向上させるだけでなく、品質検査などのさまざまな分析を行うことも可能です。
・<br>
・次の問題に行けるボタンを設置する（未定）



