jQuery( function($){
    $('#play').click( function(){
        if($(this).hasClass('playing')){
            playPause();
            $(this).removeClass('playing').addClass('paused');
            $(this).attr('src', '/assets/images/iconfinder_icon-play_211876.png');
        }else if($(this).hasClass('paused')){
            playPause();
            $(this).addClass('playing').removeClass('paused');
            $(this).attr('src', '/assets/images/iconfinder_media-pause_216309.png');
        }else{
            start();
            $(this).addClass('playing');
            $(this).attr('src', '/assets/images/iconfinder_media-pause_216309.png');
        }
    });

    $('#next').click( function(){
        $.ajax({
            url: '/next',
            method: 'POST',
            statusCode: {
                500: function(){
                    alert('Playlist vazia! Por favor clique no botão gerar');
                    location.reload();
                }
            }
        });
    });

    $('#prev').click( function(){
        $.ajax({
            url: '/prev',
            method: 'POST',
            statusCode: {
                500: function(){
                    alert('Playlist vazia! Por favor clique no botão gerar');
                    location.reload();
                }
            }
        });
    });

    $('#random').click( function(){
        $.ajax({
            url: '/rand',
            method: 'POST'
        });
        $('#play').removeClass('paused playing').trigger('click');
    });

    $('#generate').click( function(){
        $.ajax({
            url: '/generate',
            method: 'POST'
        });
        $('#play').removeClass('paused playing').trigger('click');
    });

    $('#clear').click( function(){
        $.ajax({
            url: '/clear',
            method: 'POST'
        });
        $('#play').removeClass('paused playing').attr('src', '/assets/images/iconfinder_icon-play_211876.png');
    });

    function playPause(){
        $.ajax({
            url: '/pause',
            method: 'POST',
            statusCode: {
                500: function(){
                    alert('Playlist vazia! Por favor clique no botão gerar');
                    location.reload();
                }
            }
        });
    }

    function start(){
        $.ajax({
            url: '/play',
            method: 'POST',
            statusCode: {
                500: function(){
                    alert('Playlist vazia! Por favor clique no botão gerar');
                    location.reload();
                }
            }
        });
    }
});