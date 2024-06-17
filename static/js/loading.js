document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("submit").onclick = function() {
        console.log(document.getElementById("cityBox").textContent);
        console.log(document.getElementById("countryBox").textContent);
        let loadElements = document.getElementsByClassName("load");
        // if (document.getElementById("cityBox").textContent != "" && document.getElementById("countryBox").textContent != ""){
            document.getElementById("form_container").style.height = "30em";
            for (let i = 0; i < loadElements.length; i++) {
                loadElements[i].style.visibility = 'visible';
            }
        // }
    }
});