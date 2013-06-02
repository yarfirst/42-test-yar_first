(function($){
    $(document).ready(function(){
        var token = $('[name=csrfmiddlewaretoken]').val();
        if (token){
            $('.js_delete').on('click', function(ev){
                ev.preventDefault();
                
                var el = $(this);
                $.post(el.attr('href'), {
                    'csrfmiddlewaretoken': token, 
                    'entry_id': el.attr('entry')
                }).done(function(resp) {
                    if (resp.entry_id !== undefined){
                        $('#request_log_' + resp.entry_id).remove();
                    }
                });
            });
        }
    });
})(jQuery);
