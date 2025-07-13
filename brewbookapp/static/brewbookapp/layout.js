document.addEventListener("DOMContentLoaded", function() {
    hideAlert();
    editDrink();
    stopVideos();
    toggleLike();
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
function toggleLike(button) {
    const drinkId = button.dataset.drinkId;
    const card = document.getElementById("drinkCard" + drinkId);
    const icon = button.querySelector('.bi');
    let liked = button.dataset.liked === 'true';

    if (liked) {
        // Update UI for unlike
        card.dataset.liked = 'false';
        button.dataset.liked = 'false';
        icon.classList.remove("bi-heart-fill");
        icon.classList.add("bi-heart");

        // Send request to backend
        fetch(`/unlike/${drinkId}/`)
            .then(response => response.json())
            .then(result => console.log(result))
            .catch(error => console.error("Unlike error:", error));
    } else {
        // Update UI for like
        card.dataset.liked = 'true';
        button.dataset.liked = 'true';
        icon.classList.remove("bi-heart");
        icon.classList.add("bi-heart-fill");

        // Send request to backend
        fetch(`/like/${drinkId}/`)
            .then(response => response.json())
            .then(result => console.log(result))
            .catch(error => console.error("Like error:", error));
    }
}
