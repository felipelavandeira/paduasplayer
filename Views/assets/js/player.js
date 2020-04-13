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
            method: 'POST'
        });
    });

    $('#prev').click( function(){
        $.ajax({
            url: '/prev',
            method: 'POST'
        });
    });

    function playPause(){
        $.ajax({
            url: '/pause',
            method: 'POST'
        });
    }

    function start(){
        $.ajax({
            url: '/play',
            method: 'POST'
        });
    }
});