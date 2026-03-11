// Carousel functionality for home page
let currentSlide = 0;
let slides = [];
let indicators = [];
let autoSlideInterval;

document.addEventListener('DOMContentLoaded', function() {
    slides = document.querySelectorAll('.carousel-slide');
    indicators = document.querySelectorAll('.indicator');

    // Dynamic year: always show current year in carousel (e.g. 2026)
    var yearEls = document.querySelectorAll('.year-overlay');
    var currentYear = new Date().getFullYear();
    yearEls.forEach(function(el) { el.textContent = currentYear; });

    if (slides.length > 0) {
        showSlide(0);
        startAutoSlide();
    }
});

function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => {
        slide.classList.remove('active');
    });
    
    // Remove active from all indicators
    indicators.forEach(indicator => {
        indicator.classList.remove('active');
    });
    
    // Show current slide
    if (slides[index]) {
        slides[index].classList.add('active');
    }
    
    // Activate current indicator
    if (indicators[index]) {
        indicators[index].classList.add('active');
    }
    
    currentSlide = index;
}

function changeSlide(direction) {
    let newIndex = currentSlide + direction;
    
    if (newIndex < 0) {
        newIndex = slides.length - 1;
    } else if (newIndex >= slides.length) {
        newIndex = 0;
    }
    
    showSlide(newIndex);
    resetAutoSlide();
}

function goToSlide(index) {
    showSlide(index);
    resetAutoSlide();
}

function startAutoSlide() {
    if (slides.length > 1) {
        autoSlideInterval = setInterval(() => {
            changeSlide(1);
        }, 5000); // Change slide every 5 seconds
    }
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    startAutoSlide();
}

// Pause on hover
const carouselSection = document.querySelector('.carousel-section');
if (carouselSection) {
    carouselSection.addEventListener('mouseenter', () => {
        clearInterval(autoSlideInterval);
    });
    
    carouselSection.addEventListener('mouseleave', () => {
        startAutoSlide();
    });
}

// Touch swipe support for mobile
let touchStartX = 0;
let touchEndX = 0;

if (carouselSection) {
    carouselSection.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    carouselSection.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });
}

function handleSwipe() {
    if (touchEndX < touchStartX - 50) {
        changeSlide(1); // Swipe left - next slide
    }
    if (touchEndX > touchStartX + 50) {
        changeSlide(-1); // Swipe right - previous slide
    }
}
