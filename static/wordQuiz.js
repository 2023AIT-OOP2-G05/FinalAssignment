document.getElementById('answer-button').addEventListener('click', function(event) {
    // 選択された回答を取得
    event.preventDefault();
    var selectedAnswer = document.querySelector('input[name="answer"]:checked');

    // 選択されたラジオボタンのvalueを取得
    var selectedValue = selectedAnswer ? selectedAnswer.value : null;

    // 選択されたラジオボタンのvalueをコンソールに出力
    console.log("選択された回答のvalue: ", selectedValue);

    // ここで取得したvalueを使って他の処理を行うか、サーバーに送信するなどの操作を行います。
    // 例: fetchを使用してサーバーにデータを送信する
    fetch("/checkAnswer2", {
        method: "POST",
        body: JSON.stringify({ answer: selectedValue }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        // サーバーからの応答を処理


        // 例: 応答が正解の場合、アラートを表示
        if (data === 0) {
            alert("正解です！");
        } else if (data === 1) {
            alert("不正解です！");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});