from flask import Flask, request, render_template, send_from_directory
import os, glob, json

import processors

import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploadsPicture'
# 回答用のエンドポイントを追加
app.config['PROCESSED_FOLDER'] = './processedPicture'

app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# selectMode = ""
# selectImage = ""


@app.route("/picture", methods=["POST"])
def getPicture():

    # ボタン押下の確認メッセージ
    print("送信ボタンが押された")

    # 送られてきたキーが正しいか確認
    if "original-picture" not in request.files:
        print("キーが含まれていません")
        return "Key"
    
    file = request.files['original-picture']

    # ファイルが指定されているか確認
    if file.filename == "":
        print("ファイルが指定されていない")
        return "None"
    
    # ファイルの保存
    # (プロジェクトディレクトリ内のディレクトリ「uploads-picture/」に保存している)
    file.save("uploadsPicture/" + file.filename)
    
    # 保存が成功
    return "Success"


# アップロード済み画像一覧
@app.route('/')
def uploaded_list():
    files = glob.glob("./uploadsPicture/*")  # ./uploadsPicture/以下のファイルをすべて取得
    urls = []
    index = 0
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/uploaded/" + os.path.basename(file),
            "index": index
        })
        index = index + 1
    return render_template("pictureList.html", title="アップロード済み画像", page_title="画像処理クイズ", target_files=urls)

# 変換前画像用エンドポイント
@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 変換後画像用エンドポイント
@app.route('/processed/<path:filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

# 選択されたデータを'selectData.json'に保存
@app.route('/setData', methods = ['POST'])
def setData():
    print("setData")
    selectData = request.form.to_dict()

# 都築が追加 (変更の必要あり) ----↓-
    
    # 変換前画像のファイル名を取得
    filePath = selectData["image"]

    # いったんここで画像処理を行うようにしてみる(randomとかで、行う画像処理を決定？)
    outputPath = processors.gray("uploadsPicture/" +filePath) # grayの引数は、変換前画像の所在地

    # 問題の生成は

    # num = random.randint(0,1)
    # if num == 0:
    #     outputPath = processors.binaly("uploadsPicture/" +filePath)
    # elif num == 1:
    #     outputPath = processors.gray("uploadsPicture/" +filePath)
    
    # とかになるだろうか？

    # 画像処理後のファイル名をjsonに追加
    selectData["question"] = outputPath[0]
    selectData["idNum"] = outputPath[1]

# 都築が追加--------------------↑-

    # jsonデータの書き込み
    jsonData = list()
    jsonData.append(selectData)

    with open('selectData.json', mode="w") as f:
        # 選択されたデータを'selectData.json'に上書き
        json.dump(jsonData, f, indent=4)
    return render_template("pictureList.html")

# クイズページの表示
@app.route('/test')
def test():
    print("test")
    with open('selectData.json') as f:
        # 既存のデータを読み込み
        jsonData = list(json.load(f))

    selectData = jsonData[0]
    # 変換前画像パスを追加
    selectData.update(image="/uploaded/" + selectData['image'])
    # 変換後の画像パスを追加
    selectData.update(question="/processed/" + selectData['question'])
    return render_template("test.html", data = selectData)

# 回答の正誤を判定
@app.route("/checkAnswer", methods=["POST"])
def check():
    # 回答を取得
    answer = request.data.decode("utf-8")

    with open('selectData.json') as f:
        # 既存のデータを読み込み
        jsonData = list(json.load(f))
    
    selectData = jsonData[0]

    # おそらく、この部分の返り値はresult.htmlのような、解説ページ等になると思われる
    if (answer == selectData["idNum"]):
        return "True"
    else:
        return "False"


# http://127.0.0.1:5000/
# Flask CORS
@app.route("/uploadedList")
def index():

    print("ページが読み込まれました")

    return render_template("upload.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    #app.run(debug=True)
    app.run(host="localhost",port=8888,debug=True)