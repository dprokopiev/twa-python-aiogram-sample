let telegram = window.Telegram.WebApp;
let sendButton = document.getElementById("send");
let showButton = document.getElementById("show");

sendButton.addEventListener("click", () => {
    window.location.href = "/send"
});

showButton.addEventListener("click", () => {
    window.location.href = "/photos"
});