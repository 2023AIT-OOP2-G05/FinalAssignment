from flask import Flask, request, render_template, send_from_directory
import os, glob, json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploadsPicture'
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

selectMode = ""
selectImage = ""


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
@app.route('/uploadedList')
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
    return render_template("pictureList.html", title="アップロード済み画像", page_title="アップロード済み画像　一覧", target_files=urls)


@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# 選択されたデータを'selectData.json'に保存
@app.route('/setData', methods = ['POST'])
def setData():
    print("setData")
    selectData = request.form.to_dict()
    jsonData = list()
    jsonData.append(selectData)

    with open('selectData.json', mode="w") as f:
        # 選択されたデータを'selectData.json'に上書き
        json.dump(jsonData, f, indent=4)
    return render_template("pictureList.html")


@app.route('/test')
def test():
    print("test")
    with open('selectData.json') as f:
        # 既存のデータを読み込み
        jsonData = list(json.load(f))

    selectData = jsonData[0]
    selectData.update(image="/uploaded/" + selectData['image'])
    return render_template("test.html", data = selectData)


# http://127.0.0.1:5000/
# Frask CORS
@app.route("/")
def index():

    print("ページが読み込まれました")

    return render_template("upload.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    #app.run(debug=True)
    app.run(host="localhost",port=8888,debug=True)