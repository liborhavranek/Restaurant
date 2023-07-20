// Add the 'show' class to elements when they come into view
function showContentOnScroll() {
  var elementsToShow = document.querySelectorAll('.show-from-bottom');
  elementsToShow.forEach(function (element) {
    if (isElementInViewport(element)) {
      element.classList.add('show');
    }
  });
}

// Check if an element is visible in the viewport
function isElementInViewport(el) {
  var rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Call the showContentOnScroll function when the user scrolls
window.addEventListener('scroll', showContentOnScroll);