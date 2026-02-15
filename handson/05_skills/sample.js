// ==================================
// Sample Code for Code Review Skill
// 意図的にいくつかの問題を含んでいます
// ==================================

// ユーザー認証関数
function authenticateUser(username, password) {
    // ⚠️ 問題: ハードコードされた認証情報
    const adminPassword = "admin123";

    if (username === "admin" && password === adminPassword) {
        return true;
    }

    // データベースクエリ（脆弱なパターン）
    // ⚠️ 問題: SQLインジェクションの可能性
    const query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

    console.log("実行クエリ: " + query);

    return false;
}

// ユーザー情報を表示
function displayUserInfo(userData) {
    // ⚠️ 問題: XSS脆弱性
    document.getElementById("user-info").innerHTML = userData.name;

    // ⚠️ 問題: 不明瞭な変数名
    var x = userData.age;
    var y = userData.email;

    console.log(x, y);
}

// ✅ 良い例: 適切なエラーハンドリング
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("データ取得エラー:", error);
        throw error;
    }
}

// エクスポート
module.exports = {
    authenticateUser,
    displayUserInfo,
    fetchData
};
