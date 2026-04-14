let token = "";

// 🔐 LOGIN + SHOW TOKEN
function login() {
    fetch("http://172.20.2.18:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: "admin" })
    })
    .then(res => res.json())
    .then(data => {
        token = data.token;

        // 🔥 SHOW TOKEN IN UI
        document.getElementById("tokenBox").innerText = token;

        console.log("JWT TOKEN:", token);
        alert("Login successful");
    })
    .catch(err => console.log(err));
}


// 🔥 SEND REQUEST (UPDATED)
function send() {
    const name = document.getElementById("name").value;

    fetch("http://172.20.2.18:5000/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": token
        },
        body: JSON.stringify({ name: name })
    })
    .then(res => res.json())
    .then(data => {

        // 🔥 SHOW FULL RESPONSE (message + counter + uuid)
        document.getElementById("result").innerHTML =
            "Message: " + data.message +
            "<br>Request #: " + data.request_number +
            "<br>UUID: " + data.request_id;   // ✅ NEW

    })
    .catch(err => {
        document.getElementById("result").innerText =
            "Error: " + err;
    });
}