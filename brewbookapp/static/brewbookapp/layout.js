document.addEventListener("DOMContentLoaded", function() {
    hideAlert();
    editDrink();
    stopVideos();
})

function hideAlert(){
    const alertBox = document.getElementById("drink-added");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.display = 'none';
        }, 3000);
    }
}

function editDrink() {
    const editBtns = document.querySelectorAll(".edit-drink")
    editBtns.forEach( btn => {
        btn.onclick = function(){
            const drinkId = this.dataset.drinkId
            window.location.href = "/edit_drink/" + drinkId + "/";
        };
    })
}

function stopVideos(){
    const modals = document.querySelectorAll(".modal")
    modals.forEach(modal =>{
        modal.addEventListener("hidden.bs.modal", function(){
            const iframes = modal.querySelectorAll("iframe");
            iframes.forEach(iframe => {
                const src = iframe.src;
                iframe.src = "";
                iframe.src = src;
            })
            const vidoes = modal.querySelectorAll("video");
            vidoes.forEach(video => {
                video.pause();
                video.currentTime = 0;
            })
        })
    })

}