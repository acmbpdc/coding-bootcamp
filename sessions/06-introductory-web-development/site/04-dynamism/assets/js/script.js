var main = "https://avatars1.githubusercontent.com/u/38982451?s=460&v=4";
var other = "https://66.media.tumblr.com/35d3a02f4691f8c2c75fbc4ef3365988/tumblr_p1ja1iqXyS1wkxnj3o9_1280.png";

function changeImage() {
    if (document.getElementById("profile").src == other) {
        document.getElementById("profile").src = main;
    } else {
        document.getElementById("profile").src = other;
    }
}
