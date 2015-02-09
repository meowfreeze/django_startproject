define(['jquery'], function ($) {
    
    var grid = false
    
    $('body').on('keydown.design', function(e) {
        
        if (e.keyCode == 71) {
            grid = !grid
        }
        
        if (grid) {
            $(this).append("<div class='grid-background'></div>")
        } else {
            $('.grid-background').remove()
        }
        
    })

});