document.addEventListener("DOMContentLoaded", function() {
    hideAlert();
})

function hideAlert(){
    const alertBox = document.getElementById("drink-added");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.display = 'none';
        }, 3000);
    }
}