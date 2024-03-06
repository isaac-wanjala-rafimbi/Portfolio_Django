const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle("active");    
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () =>{
hamburger.classList.remove("active");
navMenu.classList.remove("active");
}))

// Testimonials carousel
$(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    items: 1,
    dots: true,
    loop: true,
});


(jQuery);
