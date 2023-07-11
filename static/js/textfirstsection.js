  $(document).ready(function() {
      $('.grill-text-grill').animate({ left: '0px', top: '0px' }, 2000);
      $('.grill-text-steak').animate({ left: '0px', top: '0px' }, 2000);
      $('.grill-text-a').animate({ left: '0px', top: '0px' }, 2000);
    });

$(document).ready(function() {
  $(".bar-text").delay(2000).queue(function(next) {
    $(this).css("animation", "typing 3.5s steps(40, end) 0s forwards");
    next();
  });
});

