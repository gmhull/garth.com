$(window).scroll(function(){
  $('nav').toggleClass('scrolled', $(this).scrollTop() > $(window).height()-40);
});

// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.projects-item',
  layoutMode: 'masonry',
});
// change is-checked class on buttons
$('.button-group').on( 'click', 'button', function(event) {
  $('.button-group').find('.is-checked').removeClass('is-checked');
  var $button = $( event.currentTarget );
  $button.addClass('is-checked');
  var filterValue = $(this).attr('data-filter');
  $grid.isotope({ filter: filterValue });
});
