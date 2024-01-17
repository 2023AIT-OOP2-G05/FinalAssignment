const btnSearch = document.querySelector("#answer-button");
btnSearch.addEventListener("click", (event) => {

    event.preventDefault();

    // ボタン押下の確認
    console.log("回答ボタンが押されました");

    // フォームの作成
    const selectAnswer = document.querySelector('.select-answer').answer;
    let yourAnswer;

    // 選択された選択肢がどれか取得
    for (let i = 0; i < selectAnswer.length; i++) {
        if (selectAnswer[i].checked) {
            // 選択された回答を代入
            yourAnswer = selectAnswer[i].value;
            break;
        }
    }

    // フォームの送信
    fetch("/checkAnswer", {
        method: "POST",
        body: yourAnswer,
    }).then(response => response.text()) // レスポンスをテキストとして取得
      .then(text => {
        if (text == "True") {
                alert("正解です！！")
            } else {
                alert("不正解です...")
            }
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