function definput () {
    	$('#find').css('width', '80%');
        $('.header__main_find img').show();
        $('#find').val('');
    }
$(document).ready(function() {

    $('#find').click(function(e) {
        $('#find').val('');
        $('#find').css('width', '100%');
        $('.header__main_find img').hide();
    })
    
    $('.slider').bxSlider({
  auto: true,
  stopAutoOnClick: true,
  pager: true,
});
});