# from flask import Flask, request, render_template, jsonify
# import random # ランダムデータ作成のためのライブラリ
# import json

# app = Flask(__name__)
# app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# @app.route('/')
# def index():
#     #jsonファイルの読み込み
#     with open('quiz.json') as f:
#         json_data = json.load(f)
#     #どの問題を選ぶか
#     #解答の選択肢を選ぶ
#     quesnum = random.randint(0,5)
#     ansnum1 = quesnum
#     ansnum2 = quesnum
#     while(ansnum1==quesnum or ansnum2==quesnum or ansnum1==ansnum2):
#         ansnum1 = random.randint(0,5)
#         ansnum2 = random.randint(0,5)

#     #並べ替え前の選択肢を配列化
#     cleandata = [json_data[quesnum]['question'], json_data[ansnum1]['question'], json_data[ansnum2]['question']]
    
#     #選択肢の並べ替え
#     num1 = random.randint(0,2)
#     num2 = num1
#     num3 = num1
#     while(num1==num2 or num2==num3 or num3==num1):
#         num1 = random.randint(0,2)
#         num2 = random.randint(0,2)
#         num3 = random.randint(0,2)
#     #問題選択肢を送るために辞書式にぶちこむ
#     data = {'question':json_data[quesnum]['ans'], 'ans1':cleandata[num1], 'ans2':cleandata[num2],'ans3':cleandata[num3]}

#     return render_template('quizForm.html',data=data)



# if __name__ == '__main__':
#     app.run()