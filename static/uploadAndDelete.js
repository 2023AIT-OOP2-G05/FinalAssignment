// 削除画像選択肢の更新
function setOption(){
    fetch("/list").then(response => {
        response.json().then((data) => {
            // データを表示させる
            const selectBody = document.querySelector("#delete-picture > select");
            // データを新しく表示したいので、子要素を全削除
            while (selectBody.firstChild) {
                selectBody.removeChild(selectBody.firstChild)
            }
            // 見出しを追加
            let firstOp = document.createElement('option');
            firstOp.innerText = "削除する画像を選択";
            selectBody.appendChild(firstOp);
            // 要素の追加
            data.forEach(elm => {
                // 選択肢の追加
                let op = document.createElement('option');
                op.innerText = elm.fileName;
                // 1行分をtableタグ内のselectへ追加する
                selectBody.appendChild(op);
            });
        });
    });
}

// ページの初期処理
document.addEventListener("DOMContentLoaded", function () {
    setOption();
});

// アップロードボタンの押下処理
const uploadBtn = document.querySelector("#upload-button");
uploadBtn.addEventListener("click", (event) => {

    event.preventDefault();

    // ボタン押下の確認
    console.log("送信ボタンが押されました");
 
    // フォームの作成
    const data = new FormData(document.getElementById('input-picture'));

    // フォームの送信
    fetch("/upload", {
        method: "POST",
        body: data,
    }).then(response => response.text()) // レスポンスをテキストとして取得
      .then(text => {
        
        // 削除画像選択肢の更新
        setOption();

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

// 削除ボタンの押下処理
const deleteBtn = document.querySelector("#delete-button");
deleteBtn.addEventListener("click", (event) => {

    event.preventDefault();

    // ボタン押下の確認
    console.log("削除ボタンが押されました");
 
    // フォームの作成
    const selectPicture = document.getElementById('select-picture');
    const num = selectPicture.selectedIndex;
    const fileName = selectPicture.options[num].innerText;
    
    console.log("delete for "+fileName);

    // フォームの送信
    fetch("/delete", {
        method: "POST",
        body: fileName,
    }).then(response => {
        // 削除画像選択肢の更新
        setOption();
        
        confirm("削除しました.");
    });
});