from flask import Flask, request, render_template, send_from_directory, jsonify
from flask import redirect, url_for

import os, glob, json

import processors

import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploadsPicture'
# 回答用のエンドポイントを追加
app.config['PROCESSED_FOLDER'] = './processedPicture'
# 解説用のエンドポイントを追加
app.config['EXPLANATION_FOLDER'] = './explanationPicture'

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


# 選択されたデータを'selectData.json'に保存
@app.route('/setData', methods = ['POST'])
def setData():
    print("setData")
    selectData = request.form.to_dict()
    
    # 変換前画像のファイル名を取得
    fileName = selectData["image"]

    # アップロード画像にアクセスするためのファイルパスを作成
    filepath = "uploadsPicture/" +fileName

    # int型のモード識別用変数
    mode = int(selectData["mode"]) #元はstr

    # processors戻り値を保持する変数(tuple型)
    outputPath = None

    # 画像処理後の画像を保存するディレクトリを初期化
    processors.deleteOneImage("./processedPicture")

    # ファイルの画像保存先パスを作成
    savePath = "./processedPicture/"

    if mode == 1:
        # Cut系
        # 問題をランダムに選ぶためのrandom変数
        num = random.randint(0,5)
        match num:
            case 0:
                outputPath = processors.blue(filepath, savePath)
            case 1:
                outputPath = processors.red(filepath, savePath)
            case 2:
                outputPath = processors.green(filepath, savePath)
            case 3:
                outputPath = processors.blueRed(filepath, savePath)
            case 4:
                outputPath = processors.blueGreen(filepath, savePath)
            case 5:
                outputPath = processors.redGreen(filepath, savePath)
    elif mode == 2:
        # Color系
        # 問題をランダムに選ぶためのrandom変数
        num = random.randint(0,5)
        match num:
            case 0:
                outputPath = processors.colorTemperature(filepath, savePath)
            case 1:
                outputPath = processors.colorCastCorrection(filepath, savePath)
            case 2:
                outputPath = processors.saturation(filepath, savePath)
            case 3:
                outputPath = processors.exposureAmount(filepath, savePath)
            case 4:
                outputPath = processors.contrast(filepath, savePath)
            case 5:
                outputPath = processors.highlight(filepath, savePath)
    elif mode == 3:
        # 文章問題ページへ遷移...？
        # return redirect(url_for('wordquiz'))
        pass

    # 画像処理後のファイル名をjsonに追加
    selectData["question"] = outputPath[0]
    selectData["idNum"] = str(outputPath[1])

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

    # 解答欄の選択肢を追加
    if selectData['mode'] == "1":
        selectData['sample'] = ["青抜き", "赤抜き", "緑抜き", "青赤半分", "青緑半分", "赤緑半分"]
    elif selectData['mode'] == "2":
        selectData['sample'] = ["色温度", "色被り補正", "彩度", "露光量", "コントラスト", "ハイライト"]
    return render_template("test.html", data = selectData)

#単語問題のページ
@app.route('/wordquiz')
def wordquiz():
    #jsonファイルの読み込み
    with open('quiz.json') as f:
        json_data = json.load(f)
    #どの問題を選ぶか
    #解答の選択肢を選ぶ
    quesnum = random.randint(0,5)
    ansnum1 = quesnum
    ansnum2 = quesnum
    while(ansnum1==quesnum or ansnum2==quesnum or ansnum1==ansnum2):
        ansnum1 = random.randint(0,5)
        ansnum2 = random.randint(0,5)

    #並べ替え前の選択肢を配列化
    cleandata = [json_data[quesnum]['question'], json_data[ansnum1]['question'], json_data[ansnum2]['question']]
    
    #選択肢の並べ替え
    num1 = random.randint(0,2)
    num2 = num1
    num3 = num1
    while(num1==num2 or num2==num3 or num3==num1):
        num1 = random.randint(0,2)
        num2 = random.randint(0,2)
        num3 = random.randint(0,2)
    #問題選択肢を送るために辞書式にぶちこむ
    data = {'question':json_data[quesnum]['ans'], 'ans1':cleandata[num1], 'ans2':cleandata[num2],'ans3':cleandata[num3]}

    return render_template('quizForm.html',data=data)

# 回答の正誤を判定
@app.route("/checkAnswer", methods=["POST"])
def check():
    # 回答を取得
    # answer = request.data.decode("utf-8")
    selectData = request.form.to_dict()

    print("セレクトデータ")
    print(selectData)

    with open('selectData.json') as f:
        # 既存のデータを読み込み
        jsonData = list(json.load(f))
    
    # 押されたボタンの識別番号
    jsonData[0]['selectId'] = selectData["selectId"]

    print("jsonデータ")
    print(jsonData)

    # 正誤判定（正解:"True", 不正解:"False"）
    if jsonData[0]["idNum"] == selectData["selectId"]:
        jsonData[0]["result"] = "True"
        print("トゥルー")
    else:
        jsonData[0]["result"] = "False"
        print("フォルス")

    # 変換前画像のファイル名を取得
    fileName = jsonData[0]["image"]

    # アップロード画像にアクセスするためのファイルパスを作成
    filePath = "uploadsPicture/" +fileName

    # 画像処理後の画像を保存するディレクトリを初期化
    processors.deleteOneImage("./explanationPicture")

    # ファイルの画像保存先パスを作成
    savePath = "./explanationPicture/"

    # processors戻り値を保持する変数(tuple型)
    outputPath = None

    print("jsonデータの型")
    print(type(jsonData))

    if jsonData[0]["mode"] == "1":
        # Cut系
        match selectData["selectId"]:
            case "0":
                outputPath = processors.blue(filePath, savePath)
            case "1":
                outputPath = processors.red(filePath, savePath)
            case "2":
                outputPath = processors.green(filePath, savePath)
            case "3":
                outputPath = processors.blueRed(filePath, savePath)
            case "4":
                outputPath = processors.blueGreen(filePath, savePath)
            case "5":
                outputPath = processors.redGreen(filePath, savePath)
    elif jsonData[0]["mode"] == "2":
        # Color系
        match selectData["selectId"]:
            case "0":
                outputPath = processors.colorTemperature(filePath, savePath)
            case "1":
                outputPath = processors.colorCastCorrection(filePath, savePath)
            case "2":
                outputPath = processors.saturation(filePath, savePath)
            case "3":
                outputPath = processors.exposureAmount(filePath, savePath)
            case "4":
                outputPath = processors.contrast(filePath, savePath)
            case "5":
                outputPath = processors.highlight(filePath, savePath)
    elif jsonData[0]["mode"] == "3":
        # 文章問題ページへ遷移...？
        # return redirect(url_for('wordquiz'))
        pass

    # 画像処理後のファイル名をjsonに追加
    jsonData[0]["explanation"] = outputPath[0]

    print("ここ")
    print(jsonData)

    with open('selectData.json', mode="w") as f:
        # 選択されたデータを'selectData.json'に上書き
        json.dump(jsonData, f, indent=4)

    return jsonify(jsonData[0])


# 解説ページ
@app.route('/answerPage')
def answerPage():
    with open('selectData.json') as f:
        # 既存のデータを読み込み
        jsonData = list(json.load(f))
    with open('answer.json') as f:
        # 既存のデータを読み込み
        answerData = list(json.load(f))
    mode = jsonData[0]["mode"]
    selectId = jsonData[0]["selectId"]
    print("mode -> ",mode)
    print("id -> ",selectId)

    selectData = jsonData[0]
    # 変換前画像パスを追加
    selectData.update(image="/uploaded/" + selectData['image'])
    # 変換後の画像パスを追加
    selectData.update(explanation="/explanation/" + selectData['explanation'])
    selectData['anstitle'] = answerData[0][mode][selectId]['anstitle']
    selectData['anscontent'] = answerData[0][mode][selectId]['anscontent']
    return render_template("answerPageLayout.html", data=selectData)


# http://127.0.0.1:5000/
# Flask CORS
@app.route("/upAndDel")
def index():
    print("ページが読み込まれました")
    return render_template("uploadAndDelete.html")


# 変換前画像用エンドポイント
@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 変換後画像用エンドポイント
@app.route('/processed/<path:filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

# 解説用画像画像用エンドポイント
@app.route('/explanation/<path:filename>')
def explanation_file(filename):
    return send_from_directory(app.config['EXPLANATION_FOLDER'], filename)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    #app.run(debug=True)
    app.run(host="localhost",port=8888,debug=True)