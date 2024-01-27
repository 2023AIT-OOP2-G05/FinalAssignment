const btnSearch = document.querySelector("#answer-button");
btnSearch.addEventListener("click", (event) => {

    event.preventDefault();

    // ボタン押下の確認
    console.log("回答ボタンが押されました");

    // フォームの作成
    const selectAnswer = document.querySelector('.select-answer').answer;
    //let yourAnswer;
    const yourAnswer = new FormData()

    // 選択された選択肢がどれか取得
    for (let i = 0; i < selectAnswer.length; i++) {
        if (selectAnswer[i].checked) {
            // 選択された回答を代入
            //yourAnswer = selectAnswer[i].value;
            yourAnswer.append("selectId", selectAnswer[i].value)
            console.log(...yourAnswer)
            break;
        }
    }

    // フォームの送信
    fetch("/checkAnswer", {
        method: "POST",
        body: yourAnswer,
    }).then(response => {
        response.json().then((data) => {
            console.log(data)
            if (data.result == "True") {
                alert("正解です！！")
            } else {
                alert("不正解です...")
            }
        })
        location.href = "/answerPage"
    });
    

    // 選択された選択肢がどれか取得
    //selectAnswer = document.querySelector('.select-answer').answer

    // console.log(selectAnswer)
    // let yourAnswer = "";

    // // 選択された選択肢がどれか取得
    // for (let i = 0; i < selectAnswer.length; i++) {
    //     if (selectAnswer[i].checked) {
    //         // 選択された回答を代入
    //         yourAnswer = selectAnswer[i].value;
    //         break;
    //     }
    // }
    // console.log("あなたの回答 -> ", yourAnswer)

    // // 正誤判定をおこない、結果に合わせたアラートを表示
    // if (answer == yourAnswer) {
    //     alert("正解です！！")
    // } else {
    //     alert("不正解です...")
    // }
})