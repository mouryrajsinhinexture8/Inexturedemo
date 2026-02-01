const prompt = require("prompt-sync")();

function loginCheck() {
    let username = prompt("Enter Username: ");
    let password = prompt("Enter Password: ");

    if (username == "admin" && password == "1234") {
        console.log("login successful");
    } else {
        console.log("invalid credentials");
    }
}

loginCheck();
