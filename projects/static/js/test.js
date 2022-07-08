var totalItems = $('.carousel-item').length;
var currentIndex = $('div.active').index() + 1;

$('.num').html(''+currentIndex+'/'+totalItems+'');

$('#project_carousel').on('slid.bs.carousel', function() {
  currentIndex = $('div.active').index() + 1;
  $('.num').html(''+currentIndex+'/'+totalItems+'');
});
