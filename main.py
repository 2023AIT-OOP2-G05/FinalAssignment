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

#現在アップロードされている画像の一覧を取得
@app.route("/list", methods=["GET"])
def getPicture():

    files = glob.glob("./uploadsPicture/*")  # ./uploadsPicture/以下のファイルをすべて取得
    urls = []
    index = 0
    for file in files:
        urls.append({
            "fileName": os.path.basename(file),
        })
        index = index + 1

    print(urls)

    return urls

# 画像の保存を行う
@app.route("/upload", methods=["POST"])
def uploadPicture():

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

# 画像の削除を行う
@app.route("/delete", methods=["POST"])
def deletePicture():

    print("削除ボタン押下")
    
    # 削除ファイル名を取得
    answer = request.data.decode("utf-8")

    # ファイルが存在する場合のみ、削除を実行
    if os.path.exists("uploadsPicture/" + answer) :
        os.remove("uploadsPicture/" + answer)
    else:
        print("No_Such_File")

    return "deleted"

    # files = glob.glob("./uploadsPicture/*")  # ./uploadsPicture/以下のファイルをすべて取得
    # urls = []
    # index = 0
    # for file in files:
    #     urls.append({
    #         "filename": os.path.basename(file),
    #         "url": "/uploaded/" + os.path.basename(file),
    #         "index": index
    #     })
    #     index = index + 1
    # return render_template("pictureList.html", title="アップロード済み画像", page_title="画像処理クイズ", target_files=urls)


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
    fileName = selectData["image"]

    # int型のモード識別用変数
    mode = int(selectData["mode"]) #元はstr

    # 問題をランダムに選ぶためのrandom変数
    num = random.randint(0,1)

    # processors戻り値を保持する変数(tuple型)
    outputPath = None

    if mode == 1:
        # Cut系
        match num:
            case 0:
                outputPath = processors.blue("uploadsPicture/" +fileName)
            case 1:
                outputPath = processors.red("uploadsPicture/" +fileName)
            case 2:
                outputPath = processors.green("uploadsPicture/" +fileName)
            case 3:
                outputPath = processors.blueRed("uploadsPicture/" +fileName)
            case 4:
                outputPath = processors.blueGreen("uploadsPicture/" +fileName)
            case 5:
                outputPath = processors.redGreen("uploadsPicture/" +fileName)
    elif mode == 2:
        # Color系
        match num:
            case 6:
                outputPath = processors.colorTemperature("uploadsPicture/" +fileName)
            case 7:
                outputPath = processors.colorCastCorrection("uploadsPicture/" +fileName)
            case 8:
                outputPath = processors.saturation("uploadsPicture/" +fileName)
            case 9:
                outputPath = processors.exposureAmount("uploadsPicture/" +fileName)
            case 10:
                outputPath = processors.contrast("uploadsPicture/" +fileName)
            case 11:
                outputPath = processors.highlight("uploadsPicture/" +fileName)
    elif mode == 3:
        # 文章問題ページへ遷移...？
        pass

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
    
    render_template


# http://127.0.0.1:5000/
# Flask CORS
@app.route("/upAndDel")
def index():

    print("ページが読み込まれました")

    return render_template("uploadAndDelete.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
    #app.run(host="localhost",port=8888,debug=True)