from flask import Flask, request, render_template

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


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