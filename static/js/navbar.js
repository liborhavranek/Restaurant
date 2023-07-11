document.addEventListener("DOMContentLoaded", function() {
    const animateItems = document.querySelectorAll(".animate-slide");
    animateItems.forEach(function(item) {
        item.classList.add("show");
    });
});
