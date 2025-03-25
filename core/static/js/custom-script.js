function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}

$(function () {
    $('.internal-link').on('click',function(){
        if($($(this).attr('href')).length){
            $('html, body').animate({ scrollTop: $($(this).attr('href')).offset.top }, 500);
        }
        
    });
    if ($('.gallery-slider').length) {
        $('.gallery-slider').each(function () {
            let gallery_id = "gallery-" + makeid(10);
            $(this).attr('id', gallery_id);
            lightGallery(document.querySelector('#' + gallery_id), {
                thumbnail: true,
                selector: '.item',
                licenseKey: 'A8DB462B-20964EBE-95B89530-6E0512EB',
                subHtmlSelectorRelative: true
            });
            $('#' + gallery_id).owlCarousel({
                loop: true,
                nav: true,
                dots: false,
                responsive: {
                    0: {
                        items: 1
                    },
                }
            });
        });
    }

    $('.modal-popup').each(function () {
        $(this).appendTo('body');
    });

        

    if (document.querySelector('#ajax-search')) {
        document.querySelector('#ajax-search').addEventListener('input', function (e) {
            $query = $(this).val();
            clearTimeout(typingTimer);
            typingTimer = setTimeout(liveSearch($query), 1500);
        });
    }

    function liveSearch($query) {
        var $searchInput = $('#search-block-input'), $resultsWrap = $('#search-block__results-list-wrap'),
        $popular = $('#search-block__popular');
        if ($query.length > 0) {
            $resultsWrap.addClass('d-block');
            if ($(window).width() < 576) {
                $popular.addClass('d-none');
            }
        } else {
            $resultsWrap.removeClass('d-block');
            if ($(window).width() < 576) {
                $popular.removeClass('d-none');
            }
        }
        
        $.ajax({
            type: 'get',
            url: '/search',
            data: {
                'query': $query
            },
            success: function (e) {
                $('.search-block__results-list').html(e);
            },
            error: function (a, b, c) {
                // console.log(a);
                // console.log(b);
            }
        });
    }
    let typingTimer;
    

    $('.vimeo-video-btn').on('click',function(){
        var video_container = $(this).parents('.video-module-container');
        video_container.find('.vimeo-post-img').hide();
        $(this).hide();
        video_container.find('.vimeo-iframe').show();
        var iframe = video_container.find('iframe');
        const player = new Vimeo.Player(iframe);
        player.play();
        return false;
    });
});

