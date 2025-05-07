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
    $('.internal-link').on('click', function () {
        if ($($(this).attr('href')).length) {
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
        var video_container = $(this).parents('.video-module-container');
        video_container.find('.vimeo-post-img').hide();
        $(this).hide();
        video_container.find('.vimeo-iframe').show();
        var iframe = video_container.find('iframe');
        const player = new Vimeo.Player(iframe);
        player.play();
        return false;
    });


    /**** internal page navigation scripts  */
    const $navLinks = $('.internal-navigation-link');
    const $navContainer = $('.internal-page-navigation');

    // Build the internal navigation menu
    if ($navLinks.length) {
        let navHtml = '';

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
            }
            const $original = $('#' + targetId);
            const $next = $original.nextAll(':not(script):visible').first();
            if ($next.length) {
                $next.attr('id',targetId);
                //$original.replaceWith($next.clone(true, true));
                $original.remove();
            }
        });


        $navContainer.html(navHtml);
        $('body').append('<div class="internal-page-navigation-after-scroll"><div class="news-category-filter ">' + navHtml + "</div></div>");
    }
   
    // Smooth scrolling on link click
    $(document).on('click', '.scroll-link', function (e) {
        e.preventDefault();
        $('.internal-page-navigation-container').addClass('active');
        const targetId = $(this).attr('href');
        const $target = $(targetId);

        if ($target.length && bodyScrollBar) {
            // Get the target's offset inside the custom scroll container
            const offsetTop = $target[0].offsetTop;

            bodyScrollBar.scrollTo(0, offsetTop, 600); // x, y, duration (ms)
        }
    });

    if ($('.internal-page-navigation-container').length) {
        let lastScrollTop = 0;
        const $mainNavContainer = $('.internal-page-navigation-container');
        const initialOffsetTop = $mainNavContainer.offset().top + 350;
        const stickyClass = 'is-sticky-local-menu';

        bodyScrollBar.addListener(({ offset }) => {
            const scrollTop = offset.y;

            if (scrollTop >= lastScrollTop && scrollTop >= initialOffsetTop) {
                $('body').addClass(stickyClass);
            } else {
                $('body').removeClass(stickyClass);
            }

            lastScrollTop = scrollTop;
        });
    }
    
    

    /**** internal page navigation scripts  */
});


$(window).on('load',function(){
    const links = document.querySelectorAll('.scroll-link');
    const sections = Array.from(links).map(link =>
       document.querySelector(link.getAttribute('href'))
    );
    console.log(sections);
    const offset = 100; // Adjust for fixed header height

    bodyScrollBar.addListener(() => {
    // Your existing logic
    ScrollTrigger.update();
    const currentScrollTop = bodyScrollBar.offset.y;
    
    
    // 🔥 ScrollSpy logic inside the same listener
    const scrollY = currentScrollTop + offset;

    sections.forEach((section, index) => {
        console.log(
  `section: #${section.id} | offsetTop: ${section.offsetTop} | offsetHeight: ${section.offsetHeight} | scrollY: ${scrollY} | inView: ${section.offsetTop <= scrollY && section.offsetTop + section.offsetHeight > scrollY}`
);
        if ( section.offsetTop <= scrollY && section.offsetTop + section.offsetHeight > scrollY ) {
            console.log("hello active");
            links.forEach(link => link.classList.remove('active'));
            links[index].classList.add('active');
        }
    });
    });

  });





  
  