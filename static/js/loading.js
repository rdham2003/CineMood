document.getElementById("submit").onclick = function() {
    document.getElementById("form_container").style.height = "30em"
    let loadElements = document.getElementsByClassName("load");
    for (let i = 0; i < loadElements.length; i++) {
        loadElements[i].style.visibility = 'visible';
    }
};