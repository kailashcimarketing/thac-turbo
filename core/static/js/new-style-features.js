document.addEventListener('turbo:load', function () {
//----------------------------------------
let $parentContainer = $('#header__megamenu-list-2-wrap-menus'),
    btns_menu = $('.header__megamenu-panel-btn-js');
function menu_desktop_toggle(this_) {
    let menu = $(this_).data('menu');
    let $menuElement = $(menu);
    $('.header__megamenu-panel-btn-js').removeClass('header__megamenu-panel-btn-active');
    $('.show-menu-item').removeClass('show-menu-item');
    if (!$menuElement.hasClass('show-menu-item')) {
        $menuElement.addClass('show-menu-item');
        let newHeight = $menuElement.outerHeight();
        $parentContainer.height(newHeight);
        $(this_).addClass('header__megamenu-panel-btn-active');
    }
    return false;
}
menu_desktop_toggle(btns_menu[0]);
btns_menu.on('click', function () {
    menu_desktop_toggle(this);
});
$(window).on('resize', function () {
    if (window.innerWidth < 992) {
        $('#header__megamenu-list-2-wrap-menus .header__megamenu-list-2-wrap-2-js').each(function () {
            let container = $(this).data('wrapper');
            if (!$(this).parent().is(container)) {
                $(this).appendTo(container);
            }
        });
    } else if (window.innerWidth > 991) {
        $('.header__megamenu-container-js .header__megamenu-list-2-wrap-2-js').each(function () {
            let container = $(this).data('wrapper-2');
            if (!$(this).parent().is(container)) {
                $(this).appendTo(container);
            }
        });
    }
}).trigger('resize');
//----------------------------------------
let videos_js = $('.video-js');
if (videos_js.length) {
    videos_js.each(function (i, el) {
        let video = el,
            container = $(el).parents('.container-video-js');
        function play() {
            video.play();
        }
        function pause() {
            video.pause();
        }
        pause();
        let video_tl = gsap.timeline({
            scrollTrigger: {
                trigger: container,
                start: 'top bottom',
                end: 'bottom top',
                onEnter: function () {
                    play();
                },
                onLeave: function () {
                    pause();
                },
                onEnterBack: function () {
                    play();
                },
                onLeaveBack: function () {
                    pause();
                }
            }
        });
        function addClassIfPlaying() {
            if (!video.paused && !video.ended) {
                container.addClass('child-video-play');
            }
        }
        video.addEventListener('play', function () {
            container.addClass('child-video-play');
        });

        video.addEventListener('pause', function () {
            container.removeClass('child-video-play');
        });

        video.addEventListener('ended', function () {
            container.removeClass('child-video-play');
        });

        addClassIfPlaying();
    });
}




});