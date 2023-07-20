// Add the 'show' class to images when they are at least 50% visible
function showImagesOnScroll() {
  var imagesToShow = document.querySelectorAll('img.show-from-bottom');
  imagesToShow.forEach(function (image) {
    if (isImageMoreThan50PercentVisible(image)) {
      image.classList.add('show');
    }
  });
}

// Check if an image is visible in the viewport
function isImageInViewport(image) {
  var rect = image.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Check if an image is at least 50% visible
function isImageMoreThan50PercentVisible(image) {
  var rect = image.getBoundingClientRect();
  var viewportHeight = window.innerHeight || document.documentElement.clientHeight;
  var visibleHeight = Math.max(0, Math.min(rect.bottom, viewportHeight) - Math.max(rect.top, 0));
  var imageHeight = rect.height;
  return (visibleHeight / imageHeight) >= 0.05;
}

// Call the showImagesOnScroll function when the user scrolls
window.addEventListener('scroll', showImagesOnScroll);