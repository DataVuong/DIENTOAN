let idToken = "";

function handleCredentialResponse(response) {
    idToken = response.credential;
    console.log("Đăng nhập thành công!");
}

function submitReview() {
    const text = document.getElementById("reviewText").value;
    // Gợi ý: Kiểm tra đăng nhập trước khi gửi đánh giá
    if (!idToken) {
        alert("Vui lòng đăng nhập trước khi gửi đánh giá!");
        return;
    }
    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": idToken
        },
        body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = "Cảm xúc: " + (data.sentiment || data.error);
    });
}