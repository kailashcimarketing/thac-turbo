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
document.addEventListener("DOMContentLoaded", function () {
    const videoWrappers = document.querySelectorAll('.video-wrapper');
    
    videoWrappers.forEach(wrapper => {
      const video = wrapper.querySelector('video');
      const videoSrc = wrapper.getAttribute('data-video-src');
      if (videoSrc) {
        video.src = videoSrc;
        video.load();
      }
    });
  });
$(function () {
    $('.internal-link').on('click', function (e) {
        e.preventDefault();

        const targetId = $(this).attr('href');
        const targetElement = $(targetId);

        if (targetElement.length) {
            if (bodyScrollBar != null) {
                // Get the offset relative to the scroll container
                const bounding = targetElement[0].getBoundingClientRect();
                const containerScrollTop = bodyScrollBar.offset.y;
                const scrollTop = containerScrollTop + bounding.top;

                // Scroll to exact top of the section
                bodyScrollBar.scrollTo(0, scrollTop, 500);
            } else {
                // Fallback for native scroll
                const targetOffsetTop = targetElement.offset().top;
                $('html, body').animate({ scrollTop: targetOffsetTop }, 500);
            }
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
    $('.move-modal-items-to-body > .modal').each(function () {
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


    $('.vimeo-video-btn').on('click', function () {
        var video_container = $(this).parents('.video-module-wrapper');
        if(video_container.hasClass('active')){
            //console.log('active');
            video_container.find('.vimeo-post-img').show();
            //$(this).hide();
            video_container.removeClass('active');
            //video_container.find('.vimeo-iframe').hide();
            if ($(this).attr('type') == 'mp4-video') {
                var video = $(this).parent().find('video').get(0);
                video.pause();
                video.currentTime = 0;
            } else {
                var iframe = video_container.find('iframe');
                const player = new Vimeo.Player(iframe);
                player.pause();
            }
            return false;
        }else{
//console.log('---active');
            video_container.find('.vimeo-post-img').hide();
            //$(this).hide();
            video_container.addClass('active');
            video_container.find('.vimeo-iframe').show();
            if ($(this).attr('type') == 'mp4-video') {
                var video = $(this).parent().find('video').get(0);
                video.play();
            } else {
                var iframe = video_container.find('iframe');
                const player = new Vimeo.Player(iframe);
                player.play();
            }
            return false;
        }
    });


    /**** internal page navigation scripts  */
    const $navLinks = $('.internal-navigation-link');
    const $navContainer = $('.internal-page-navigation');

    // Build the internal navigation menu
    if ($navLinks.length) {
        let navHtml = '';
        let mobile_navHtml='<div class="internal-navigation-dropdown">';      
        mobile_navHtml += '<a class="btn nav-label">Select Section</a>';
        mobile_navHtml += '<ul>';

        $navLinks.each(function () {
            const label = $(this).data('label');
            const targetId = $(this).attr('id');

            if (label && targetId) {
                navHtml += `
                <div class="w-auto block-anim-js block-anim--row-short-js">
                    <a href="#${targetId}" class="btn btn--third scroll-link">
                        <span class="btn__content">
                            <span class="btn__txt">${label}</span>
                        </span>
                    </a>
                </div>`;
                /// navHtml += `<li><a href="#${targetId}" class="scroll-link">${label}</a></li>`;
                mobile_navHtml += `<li><a href="#${targetId}" class="scroll-link">${label}</a></li>`;
            }
            const $original = $('#' + targetId);
            const $next = $original.nextAll(':not(script):visible').first();
            if ($next.length) {
                $next.attr('id', targetId);
                //$original.replaceWith($next.clone(true, true));
                $original.remove();
            }
        });
        mobile_navHtml += '</ul>';
        mobile_navHtml += '</div>';


        $navContainer.html(navHtml+mobile_navHtml);
        if($(window).width() > 767){
            $('body').append('<div class="internal-page-navigation-after-scroll"><div class="news-category-filter ">' + navHtml + "</div></div>");
        }else{
            $('body').append('<div class="internal-page-navigation-after-scroll"><div class="news-category-filter ">'+ mobile_navHtml +'</div></div>');
        }
    }

    // Smooth scrolling on link click
    $(document).on('click', '.scroll-link', function (e) {
        e.preventDefault();
        $('.internal-page-navigation-container').addClass('active');
        const targetId = $(this).attr('href');
        const $target = $(targetId);
        $(".internal-navigation-dropdown").removeClass('open');
        
        if ($target.length && bodyScrollBar) {
            // Get the target's offset inside the custom scroll container
            const offsetTop = $target[0].offsetTop;

            bodyScrollBar.scrollTo(0, offsetTop, 600); // x, y, duration (ms)
        }else{
            const offsetTop = $target.offset().top;
            $('html, body').animate({ scrollTop: offsetTop }, 600);
        }
    });

    $(document).on('click', '.internal-navigation-dropdown > a', function (e) {
        e.preventDefault();
        $(this).parent().toggleClass('open');
    });

    if ($('.internal-page-navigation-container').length) {
        const $mainNavContainer = $('.internal-page-navigation-container');
        const initialOffsetTop = $mainNavContainer.offset().top + 350;
        const stickyClass = 'is-sticky-local-menu';
        let lastScrollTop = 0;

        if (bodyScrollBar != null) {
            // Use custom scrollbar listener
            bodyScrollBar.addListener(({ offset }) => {
                const scrollTop = offset.y;

                if (scrollTop >= lastScrollTop && scrollTop >= initialOffsetTop) {
                    $('body').addClass(stickyClass);
                } else {
                    $('body').removeClass(stickyClass);
                }

                lastScrollTop = scrollTop;
            });
        } else {
            // Fallback to native scroll listener
            $(window).on('scroll', function () {
                const scrollTop = $(this).scrollTop();

                if (scrollTop >= lastScrollTop && scrollTop >= initialOffsetTop) {
                    $('body').addClass(stickyClass);
                } else {
                    $('body').removeClass(stickyClass);
                }

                lastScrollTop = scrollTop;
            });
        }
    }



    /**** internal page navigation scripts  */
});


$(window).on('load', function () {
    const links = document.querySelectorAll('.scroll-link');
    const sections = Array.from(links).map(link =>
        document.querySelector(link.getAttribute('href'))
    );

    const offset = 100; // Adjust for fixed header height

    function handleScroll(scrollTop) {
        ScrollTrigger.update();

        const scrollY = scrollTop + offset;

        sections.forEach((section, index) => {
            if (!section) return; // Safety check

            //console.log(`section: #${section.id} | offsetTop: ${section.offsetTop} | offsetHeight: ${section.offsetHeight} | scrollY: ${scrollY} | inView: ${section.offsetTop <= scrollY && section.offsetTop + section.offsetHeight > scrollY}`);

            const inView =
                section.offsetTop <= scrollY &&
                section.offsetTop + section.offsetHeight > scrollY;

            if (inView) {
                links.forEach(link => link.classList.remove('active'));
                //console.log(links[index]);
                links[index].classList.add('active');
                $('.internal-page-navigation-after-scroll .nav-label').text(links[index].textContent || links[index].innerText);
            }
        });
    }

    if (bodyScrollBar != null) {
        bodyScrollBar.addListener(() => {
            const currentScrollTop = bodyScrollBar.offset.y;
            handleScroll(currentScrollTop);
        });
    } else {
        $(window).on('scroll', function () {
            const currentScrollTop = $(this).scrollTop();
            handleScroll(currentScrollTop);
        });
    }
});







