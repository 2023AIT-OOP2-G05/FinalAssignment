const btnSearch = document.querySelector("#upload-button");
btnSearch.addEventListener("click", (event) => {

    event.preventDefault();

    // ボタン押下の確認
    console.log("送信ボタンが押されました");
 
    // フォームの作成
    const data = new FormData(document.getElementById('input-picture'));

    // フォームの送信
    fetch("/picture", {
        method: "POST",
        body: data,
    }).then(response => response.text()) // レスポンスをテキストとして取得
      .then(text => {
        /*
            画像を保存した後の処理について、
            .jsでは行わない？
        */  
        if (text == "Key"){
            console.log("キーがありません");
            alert("送信中にエラーが発生しました.\n管理者へお問い合わせください.");
        } else if (text == "None"){
            console.log("ファイルが指定されていません");
            alert("ファイルが指定されていません.");
        } else if (text == "Success"){
            console.log("送信が完了しました");
            confirm("送信が完了しました.");
        }
    });
})