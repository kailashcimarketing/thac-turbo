let bodyScrollBar = null, lastScrollTop = 0;

document.addEventListener('turbo:load', function () {
    

    gsap.registerPlugin(ScrollTrigger);
    console.log("called");
//------------------------------------------------------------
gsap.registerEffect({
    name: 'counter',
    extendTimeline: true,
    defaults: {
        end: '0',
        duration: 0.5,
        ease: 'power1',
        increment: 1,
    },
    effect: (targets, config) => {
        let tl = gsap.timeline();
        let endValue = parseFloat(
            config.end.toString().replace(',', '.')
        );
        if (isNaN(endValue)) endValue = 0;

        tl.to({}, {
            duration: config.duration,
            onUpdate: function () {
                let progress = this.progress();
                let currentValue = (endValue * progress);
                if (Number.isInteger(endValue)) {
                    currentValue = Math.round(currentValue);
                } else {
                    currentValue = currentValue.toFixed(1);
                }
                if (config.end.includes(',')) {
                    currentValue = currentValue.toString().replace('.', ',');
                }
                targets.forEach((target) => {
                    target.innerText = currentValue;
                });
            },
            ease: config.ease
        });

        return tl;
    }
});
//-------------------------------------------------------
// if(document.querySelector('#preloader')) {
    const startTime = performance.now();
    let tl_preloader = gsap.timeline({
        paused: true,
    });
    tl_preloader.counter('#preloader__counter-numb', {
        end: '100',
        increment: 1,
        duration: 3,
    });
// }
let selector_txt_lines = '.split-text-by-line-js';
if (document.querySelectorAll(selector_txt_lines).length > 0) {
    let txt = new SplitText(
            '.hero-title-js.split-text-by-line-js,' +
            '.hero-title-2-js.split-text-by-line-js,' +
            '.hero-txt-js.split-text-by-line-js p'
            , {
                type: 'lines',
                linesClass: 'anim-lines'
            })
        // txt_wrap = new SplitText(
        //     '.hero-title-js.split-text-by-line-js,' +
        //     '.hero-title-2-js.split-text-by-line-js,' +
        //     '.hero-txt-js.split-text-by-line-js p'
        //     , {
        //         type: 'lines',
        //         linesClass: 'anim-lines-wrap'
        //     })
}
//------------------------------
gsap.set('.container-hero-anim-js,.container-anim-js', {autoAlpha: 0});
// function hero_block_pos() {
//     $('.hero-item-js').each(function (i, el) {
//         if ($(el).offset().top >= window.innerHeight || $(window).scrollTop() >= window.innerHeight) {
//             $(el).removeClass('hero-item-js').addClass('block-anim-js');
//             $(el).parents('.container-hero-anim-js').removeClass('container-hero-anim-js').addClass('container-anim-js');
//         }
//     })
// }
document.querySelector('body').classList.add('enable-transition');
function hero_block_pos() {
    const heroItems = document.querySelectorAll('.hero-item-js');

    heroItems.forEach((el) => {
        const elementTop = el.getBoundingClientRect().top;
        const scrollTop = window.scrollY;

        if (elementTop >= window.innerHeight || scrollTop >= window.innerHeight) {
            el.classList.remove('hero-item-js');
            el.classList.add('block-anim-js');

            const container = el.closest('.container-hero-anim-js');
            if (container) {
                container.classList.remove('container-hero-anim-js');
                container.classList.add('container-anim-js');
            }
        }
    });
}
hero_block_pos();
//------------------------------
if(document.querySelectorAll('.hero-primary').length > 0) {
    let heroTitle = document.querySelector('.hero-primary__title.hero-title-js');
    if (heroTitle) {
        const lines = heroTitle.innerHTML.split('<br>');
        const wrappedLines = lines.map(line => `<span class="d-block anim-lines">${line.trim()}</span>`);
        heroTitle.innerHTML = wrappedLines.join('');
    }
}
//------------------------------
let duration_opacity = .5,
    duration_transform = .7,
    stagger_step = .05,
    stagger_lines = .05;
//------------------------------
let delay_0 = .05,
    delay_1 = .15,
    delay_2 = .2,
    delay_3 = .3,
    delay_4 = .4,
    delay_5 = .5,
    delay_6 = .5,
    delay_7 = .6;
//------------------------------
let hero_tl = gsap.timeline({
    paused: true,
    defaults: {
        ease: 'power1.inOut',
        duration: .5,
    }
});

hero_tl.from("#header", {
    y: '-100px',
    opacity: 1,
    duration: 0.75,
    ease: "power2.in",
    onComplete: () => {
        // Clear inline styles added by GSAP
        gsap.set("#header", { clearProps: "all" });
        gsap.set("#header", { opacity: 1 });
      }
  });
//-----------------------------------
if (document.querySelectorAll('.header-item-js.header-item-1-js').length > 0) {
    hero_tl.from('.header-item-js.header-item-1-js', {
        autoAlpha: 0,
        stagger: stagger_step,
    }, delay_0)
}
//------------------------------------------
if (document.querySelectorAll('.hero-item-js.hero-item-1-js').length > 0) {
    hero_tl.from('.hero-item-js.hero-item-1-js', {
        autoAlpha: 0,
        stagger: stagger_step,
    }, delay_1)
}
//-----------------------------------
if (document.querySelectorAll('.hero-title-js .anim-lines').length > 0) {
    // console.log(document.querySelectorAll('.hero-primary').length > 0)
    if(document.querySelectorAll('.hero-primary').length > 0) {
        hero_tl.from('.hero-title-js .anim-lines:nth-child(1)', {
            autoAlpha: 0,
            ease: 'power1.inOut',
            duration: duration_opacity,
        }, delay_3)
        hero_tl.from('.hero-title-js .anim-lines:nth-child(1)', {
            x: -100,
            ease: 'power1.inOut',
            duration: duration_transform,
        }, delay_2)
        hero_tl.from('.hero-title-js .anim-lines:nth-child(2)', {
            autoAlpha: 0,
            ease: 'power1.inOut',
            duration: duration_opacity,
        }, delay_3)
        hero_tl.from('.hero-title-js .anim-lines:nth-child(2)', {
            x: 100,
            ease: 'power1.inOut',
            duration: duration_transform,
        }, delay_2)
    } else {
        let init_pos = 50;
        if(document.querySelectorAll('.hero-title-js.hero-title--to-right-js').length > 0) {
            init_pos = -50;
        }
        hero_tl.from('.hero-title-js .anim-lines', {
            autoAlpha: 0,
            ease: 'power1.inOut',
            duration: duration_opacity,
            stagger: stagger_lines,
        }, delay_3)
        hero_tl.from('.hero-title-js .anim-lines', {
            x: init_pos,
            ease: 'power1.inOut',
            duration: duration_transform,
            stagger: stagger_lines,
        }, delay_2)
    }
}
if (document.querySelectorAll('.hero-title-2-js .anim-lines').length > 0) {
    hero_tl.from('.hero-title-2-js .anim-lines', {
        autoAlpha: 0,
        ease: 'power1.inOut',
        duration: duration_opacity,
        stagger: stagger_lines,
    }, delay_7)
    hero_tl.from('.hero-title-2-js .anim-lines', {
        yPercent: 100,
        ease: 'power1.inOut',
        duration: duration_transform,
        stagger: stagger_lines,
    }, delay_6)
}
//-----------------------------------
if (document.querySelectorAll('.hero-pic-scale-js').length > 0) {
 /*   hero_tl
    // .from('.hero-pic-scale-js', {
    //     autoAlpha: 0,
    //     duration: .3,
    // }, delay_4)
    .to('.hero-pic-scale-js', {
        scale: 1,
        ease: 'cubic-bezier(0.74, 0, 0.24, 0.99)',
        duration: 2,
    },0)*/
//    delay_3
}
//-----------------------------------
if (document.querySelectorAll('.hero-txt-js .anim-lines').length > 0) {
    hero_tl.from('.hero-txt-js .anim-lines', {
        autoAlpha: 0,
        duration: duration_opacity,
        stagger: stagger_lines,
    }, delay_5)
    hero_tl.from('.hero-txt-js .anim-lines', {
        yPercent: 100,
        duration: duration_transform,
        stagger: stagger_lines,
    }, delay_4)
}
//-----------------------------------
if (document.querySelectorAll('.hero-item-js.hero-item-2-js').length > 0) {
    hero_tl.from('.hero-item-js.hero-item-2-js', {
        autoAlpha: 0,
        stagger: stagger_step,
    }, delay_6)
}
//-----------------------------------
if (document.querySelectorAll('.hero-item-js.hero-item-3-js').length > 0) {
    hero_tl.from('.hero-item-js.hero-item-3-js', {
        autoAlpha: 0,
        duration: duration_opacity,
        stagger: stagger_step,
    }, delay_7)
    hero_tl.from('.hero-item-js.hero-item-3-js', {
        y: 30,
        duration: duration_transform,
        stagger: stagger_step,
    }, delay_6);
}
if (document.querySelectorAll('.container-anim-js.homepage-anim-js').length > 0) {
    hero_tl.from('.container-anim-js.homepage-anim-js .anim-js', {
        autoAlpha: 0,
        stagger: stagger_step,
    }, delay_6)
}

//-----------------------------------
let selector_anim_container = '.container-hero-anim-js',
    selector_anim_header = '.container-header-anim-js';
if (document.querySelectorAll(selector_anim_container).length > 0 || document.querySelectorAll(selector_anim_header).length > 0) {
    gsap.set([selector_anim_container, selector_anim_header], {
        autoAlpha: 1
    });
}
//------------------------------------------------------------
function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = '; expires=' + date.toGMTString();
    } else var expires = '';
    document.cookie = name + '=' + value + expires + '; path=/';
}
function readCookie(name) {
    var nameEQ = name + '=';
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
function eraseCookie(name) {
    createCookie(name, '', -1);
}
function cookieCheck() {
    var x = readCookie('cookie');
    if (!!x === false) {
        if(document.querySelectorAll('#modal-1').length > 0) {
            document.querySelector('#modal-1').classList.add('is-open');
            document.querySelector('#modal__overlay').classList.add('is-open');
        }
        document.querySelectorAll('#modal__overlay, #modal-close-1').forEach(function (element) {
            element.addEventListener('click', function () {
                event.preventDefault();
                createCookie('cookie', 'yes', 7);
            });
        });
    } else {
        if(document.querySelectorAll('#modal-1').length > 0) {
            document.querySelector('#modal-1').classList.add('is-open');
            document.querySelector('#modal__overlay').classList.add('is-open');
        }
        return false;
    }
    var y = readCookie('cookieConcession');
    if (!!y === false) {
        if(document.querySelectorAll('#modal-1').length > 0) {
            document.querySelector('#modal-1').classList.add('is-open');
            document.querySelector('#modal__overlay').classList.add('is-open');
        }
        document.querySelectorAll('#modal__overlay, #modal-close-1').forEach(function (element) {
            element.addEventListener('click', function () {
                event.preventDefault();
                createCookie('cookie', 'yes', 7);
            });
        });
    } else {
        if(document.querySelectorAll('#modal-1').length > 0) {
            document.querySelector('#modal-1').classList.remove('is-open');
            document.querySelector('#modal__overlay').classList.remove('is-open');
        }
        return false;
    }
}
//-----------------------------------
if(document.querySelectorAll('#preloader').length > 0) {
     tl_preloader
  .fromTo(".first_word", 
    { opacity: 0, x: -20 }, 
    { opacity: 1, x: 0, duration: 0.8 }
  )
  .to(".first_word", { opacity: 0, duration: 0.5 })

  .fromTo(".second_word", 
    { opacity: 0, x: -20 }, 
    { opacity: 1, x: 0, duration: 0.8 }
  )
  .to(".second_word", { opacity: 0, duration: 0.5 })

  .fromTo(".third_word", 
    { opacity: 0, x: -20 }, 
    { opacity: 1, x: 0, duration: 0.8 }
  )
  .to(".third_word", { opacity: 0, duration: 0.5 })

  .fromTo(".fourth_word", 
    { opacity: 0, x: -20 }, 
    { opacity: 1, x: 0, duration: 0.8 })
    .to(".fourth_word", { opacity: 0, duration: 0.5 });
    tl_preloader.to(".preloader__logo", {
        duration: 2,
        x: "-45vw",
        y: "-45vh",
        opacity: 0,
        scale: 0.55, 
        ease: "power2.inOut",
    });
    /*tl_preloader.play().then(function() {
        hero_tl.play();
        gsap.to('#preloader',{
            autoAlpha: 0,
            duration: .7,
            onComplete: function () {
                gsap.delayedCall(.2,function() {
                  hero_tl.play();
                });
                gsap.delayedCall(2,function() {
                    cookieCheck();
                });
            },
        })
    });*/
} else {
    //hero_tl.play();
}

/****new loader */
let tl_hero = gsap.timeline({
    paused: true,
});
hero_tl
  .from(".hero-title-anim-js", {
    x: "-200",
    autoAlpha: 0,
    duration: 1,
    ease: "power2.In"
  }, 1) // Start at 0 seconds
  .from(".hero-btn-anim-js", {
    x: "100",
    autoAlpha: 0,
    duration: 1,
    ease: "power2.In"
  }, 1.25) // Start at 0 seconds (same time)
  .from(".hero-round-btn-anim-js", {
    y: "150",
    autoAlpha: 0,
    duration: 1,
    ease: "power2.In"
  }, 1.5); // Start at 0 seconds (same time)
  
let tl_logo_preloader = gsap.timeline({
    paused: true,
});

let tl_preloader_bg = gsap.timeline({ paused: true, })
    .to(".preloader-bg", {
        height: "0",
        autoAlpha: 1,
        duration: 2,
        delay: 1,
        ease: "power2.out",
        onStart:function(){
            $('.logo-loader').css('background','none');
        }

    });
if ($('.logo-loader').length) {
            const first = document.querySelector('.first');
            const second = document.querySelector('.second');
            const three = document.querySelector('.third');
            // Set initial positions - all words start below the container
            gsap.set([first, second, three], {
                y: 100,
                opacity: 0
            });
            
            // Animate first word with smooth bounce effect
            tl_logo_preloader.to(first, {
                duration: 0.8,
                y: 0,
                opacity: 1,
                ease: "back.out(0.7)"
            })
            .to(first, {
                duration: 0.5,
                y: -100,
                opacity: 0,
                ease: "power2.in"
            }, "+=0.8")
            
            // Animate second word with smooth bounce effect
            .to(second, {
                duration: 0.8,
                y: 0,
                opacity: 1,
                ease: "back.out(0.7)"
            }, "-=0.3")
            .to(second, {
                duration: 0.5,
                y: -100,
                opacity: 0,
                ease: "power2.in"
            }, "+=0.8")
            
            // Animate third word with smooth bounce effect
            .to(three, {
                duration: 0.8,
                y: 0,
                opacity: 1,
                ease: "back.out(0.7)"
            }, "-=0.3")
            .to(three, {
                duration: 0.5,
                y: -100,
                opacity: 0,
                ease: "power2.in",
                onStart: function () {
                    tl_preloader_bg.play();
                }
            }, "+=0.8");
        // 1. Get target logo position
var logoOffset = $('.header__logo-1').offset(); // { top: ..., left: ... }

// 2. Get window center
var windowWidth = $(window).width();
var windowHeight = $(window).height();
var centerX = windowWidth / 2;
var centerY = windowHeight / 2;

// 3. Get the center of the .header__logo-1 element
var logoWidth = $('.header__logo-1').outerWidth();
var logoHeight = $('.header__logo-1').outerHeight();
var logoCenterX = logoOffset.left + logoWidth / 2;
var logoCenterY = logoOffset.top + logoHeight / 2;

// 4. Calculate difference (this is what you pass to GSAP)
var x = logoCenterX - centerX;
var y = logoCenterY - centerY;
    tl_logo_preloader.to(".preloader__logo", {
        duration: 2,
        x: window.innerWidth>991?x:"0",
        y:y+10,
        opacity: 0,
        scale: 0.49,
        ease: "power2.inOut",
        onStart: function () {
            hero_tl.play();
            tl_logo_preloader.to(".preloader__logo", {opacity:0});
        }
    });

    tl_logo_preloader.play().then(function () {
        gsap.to('.logo-loader', {
            autoAlpha: 0,
            duration: .7,
            onStart: function () {
                gsap.delayedCall(.2, function () {
                    hero_tl.play();
                });
                gsap.delayedCall(2, function () {
                    cookieCheck();
                });
            },
        })
    });
} else {
    hero_tl.play();
}
/************** */

// window.addEventListener('load', () => {
//     const endTime = performance.now();
//     const loadDuration = (endTime - startTime) / 1000;
//     gsap.to(tl_preloader, {
//         timeScale: tl_preloader.duration() / loadDuration,
//         duration: .7,
//         onComplete: function() {
//             gsap.to('#preloader',{
//                 autoAlpha: 0,
//                 duration: .7,
//                 onComplete: function () {
//                     hero_tl.play();
//                     gsap.delayedCall(2,function() {
//                         cookieCheck();
//                     });
//                 },
//             })
//         }
//     });
// });
//------------------------------------------------------------

/* main.js  */
function isTouchDevice() {
    return 'ontouchstart' in window || navigator.maxTouchPoints > 0;
}
if (window.innerWidth < 768) {
    const contentContainers = document.querySelectorAll('.s-pin-banners__content-container');
    contentContainers.forEach((container) => {
        if (container.hasAttribute('data-scrollbar')) {
            container.removeAttribute('data-scrollbar');
        }
    });
}
if (!isTouchDevice()) {
    document.documentElement.classList.add('Scrollbar-init');
    // let bodyScrollBar_all = Scrollbar.initAll();
    let bodyScrollBar_all = Scrollbar.initAll({
        ignoreEvents: (event) => {
            return event.target.closest('[data-scroll="exclude"]');
        },
    });
    const scrollableBlocks = document.querySelectorAll('[data-scroll="exclude"]');
    scrollableBlocks.forEach((block) => {
        block.addEventListener('wheel', (e) => e.stopPropagation(), { passive: false });
        block.addEventListener('touchmove', (e) => e.stopPropagation(), { passive: false });
    });
    
    bodyScrollBar = Scrollbar.get(document.querySelector('#body-content-wrap'));
    
    ScrollTrigger.scrollerProxy('#body-content-wrap', {
        scrollTop(value) {
            if (arguments.length) {
                bodyScrollBar.scrollTop = value;
            }
            return bodyScrollBar.scrollTop;
        },
        getBoundingClientRect() {
            return {
                top: 0,
                left: 0,
                width: window.innerWidth,
                height: window.innerHeight,
            };
        },
    });

    bodyScrollBar.addListener(() => {
        ScrollTrigger.update();
        const currentScrollTop = bodyScrollBar.offset.y;
        if (currentScrollTop > lastScrollTop) {
            scroll_dir(1);
        } else if (currentScrollTop < lastScrollTop) {
            scroll_dir(-1);
        }
        lastScrollTop = currentScrollTop;
        scroll_offset(currentScrollTop);
    });

}
var document_body = document.body;
var body = $('body');
function scroll_offset(scroll) {
    if (scroll > 0) {
        document_body.classList.add('is-offset-top');
    } else {
        document_body.classList.remove('is-offset-top');
    }
}
function scroll_dir(direction) {
    if (direction === 1) {
        document_body.classList.add('scroll-down');
        
    } else {
        document_body.classList.remove('scroll-down');

    }
}
function setScrollTrigger() {
    const scroller = !isTouchDevice() ? '#body-content-wrap' : 'body';
    ScrollTrigger.defaults({
        scroller: scroller,
        pinType: !isTouchDevice() ? 'transform' : 'fixed',
    });
}
setScrollTrigger();
window.addEventListener('resize', setScrollTrigger);

//-------------------------------------------------------
let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', vh + 'px');
document.documentElement.style.setProperty('--vh-2', vh + 'px');
var isMobile = /iPhone|iPad|iPod|midp|rv:1.2.3.4|ucweb|windows ce|windows mobile|BlackBerry|IEMobile|Opera Mini|Android/i.test(navigator.userAgent);
window.addEventListener('resize', function () {
    vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', vh + 'px');
    if (!isMobile) {
        document.documentElement.style.setProperty('--vh-2', vh + 'px');
    }
});
//-------------------------------------------------------
function moveElement(element,parent1,parent2) {
    if (window.innerWidth < 992) {
        if (element.parentElement !== parent1) {
            parent1.appendChild(element);
        }
    } else {
        if (element.parentElement !== parent2) {
            parent2.appendChild(element);
        }
    }
}


    const menuBurger = document.querySelector('#menu-burger');
    if (menuBurger) {
        menuBurger.addEventListener('click', () => {
            event.preventDefault();
            $('#search-block').removeClass('is-open');
            $('[href="#search-block"]').removeClass('is-open');
            if($(window).width() > 767){
                
                $('#header__login-block').removeClass('is-open');
                $('[href="#header__login-block"]').removeClass('is-open');
                $('#header__col-2,#header__col-3').removeClass('hide-when-open');
                $('#header__overlay').removeClass('show-overlay-3 show-overlay-2');
            }
            
            if(!$('body').hasClass('menu-open') && $('body').hasClass('is-open-menu')){
                
                if($('#search-block').hasClass('is-open')){
                //    $('.close-search').trigger('click');
                }
            }
            document.body.classList.toggle('menu-open');
            document.querySelector('#header__overlay').classList.toggle('show-overlay-1');            
            return false;
        });
    }
    const element = document.querySelector('#header__megamenu-list-2-wrap-2');
    if (element) {
        let parent1 = document.querySelector('#header__megamenu-container-2'),
            parent2 = document.querySelector('#header__megamenu-list-2-wrap');
        window.addEventListener('resize', function () {
            moveElement(element, parent1, parent2)
            // updateMegamenuHeight();
        });
        moveElement(element, parent1, parent2);
    }
    const element_2 = document.querySelector('#header__col-3-btns-wrap');
    if (element_2) {
        let parent1 = document.querySelector('#header__megamenu-header'),
            parent2 = document.querySelector('#header__col-3');
        window.addEventListener('resize', function () {
            moveElement(element_2, parent1, parent2)
        });
        moveElement(element_2, parent1, parent2);
    }
    const element_3 = document.querySelector('#drop-content-2');
    if (element_3) {
        let parent1 = document.querySelector('#header__megamenu-header'),
            parent2 = document.querySelector('#header__col-3');
        window.addEventListener('resize', function () {
            moveElement(element_3, parent1, parent2)
        });
        moveElement(element_3, parent1, parent2);
    }
    const element_4 = document.querySelector('#header__login-block');
    if (element_4) {
        let parent1 = document.querySelector('#header__megamenu-header'),
            parent2 = document.querySelector('#header');
        window.addEventListener('resize', function () {
            moveElement(element_4, parent1, parent2)
        });
        moveElement(element_4, parent1, parent2);
    }
    const element_5 = document.querySelector('#search-block');
    if (element_5) {
        let parent1 = document.querySelector('#header'),
            parent2 = document.querySelector('#header__col-4');
        window.addEventListener('resize', function () {
            moveElement(element_5, parent1, parent2)
        });
        moveElement(element_5, parent1, parent2);
    }

//-------------------------------------------------------

let pin_banners = $('.s-pin-banners__content-js');
if(pin_banners.length && window.innerWidth < 768) {
    for (let i = 0; i < pin_banners.length; i++) {
        $('.s-pin-banners__content--'+ (i+1)).appendTo('.s-pin-banners__block--'+ (i+1));
        $('.s-pin-banners__contents-pic-wrap--'+ (i+1)).appendTo('.s-pin-banners__block--'+ (i+1));
    }
}
function isSafari() {
    return /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
}
function isWindows() {
    return /windows/i.test(navigator.userAgent);
}
function set_delay(item) {
    let delay = 0;
    if (item.data('delay-anim')) {
        delay = item.data('delay-anim');
    }
    if (item.data('delay-anim-sm') && window.innerWidth > 575) {
        delay = item.data('delay-anim-md');
    }
    if (item.data('delay-anim-md') && window.innerWidth > 767) {
        delay = item.data('delay-anim-md');
    }
    if (item.data('delay-anim-lg') && window.innerWidth > 991) {
        delay = item.data('delay-anim-lg');
    }
    if (item.data('delay-anim-xl') && window.innerWidth > 1199) {
        delay = item.data('delay-anim-xl');
    }
    if (item.is('.block-anim--row-parent-js')) {
        delay = item.parent().index() * .12;
    }
    if (item.is('.block-anim--row-js')) {
        delay = item.index() * .12;
    }
    if (item.is('.block-anim--row-short-js')) {
        delay = item.index() * .05;
    }
    if (item.is('.block-anim--each-2-js:nth-child(2n+2)')
        || item.is('.block-anim--each-3-js:nth-child(3n+2)')
        || item.is('.block-anim--each-4-js:nth-child(4n+2)')) {
        delay = .1
    }
    if (item.is('.block-anim--each-3-js:nth-child(3n+3)')
        || item.is('.block-anim--each-4-js:nth-child(4n+3)')) {
        delay = .2
    }
    if (item.is('.block-anim--each-4-js:nth-child(4n+4)')) {
        delay = .3
    }
    if ((item.is('.block-anim--each-2-sm-js:nth-child(2n+2)') && window.innerWidth > 575)
        || (item.is('.block-anim--each-3-sm-js:nth-child(3n+2)') && window.innerWidth > 575)
        || (item.is('.block-anim--each-4-sm-js:nth-child(4n+2)') && window.innerWidth > 575)) {
        delay = .1
    }
    if ((item.is('.block-anim--each-3-sm-js:nth-child(3n+3)') && window.innerWidth > 575)
        || (item.is('.block-anim--each-4-sm-js:nth-child(4n+3)') && window.innerWidth > 575)) {
        delay = .2
    }
    if (item.is('.block-anim--each-4-sm-js:nth-child(4n+4)') && window.innerWidth > 575) {
        delay = .3
    }
    if ((item.is('.block-anim--each-2-md-js:nth-child(2n+2)') && window.innerWidth > 767)
        || (item.is('.block-anim--each-3-md-js:nth-child(3n+2)') && window.innerWidth > 767)
        || (item.is('.block-anim--each-4-md-js:nth-child(4n+2)') && window.innerWidth > 767)) {
        delay = .1
    }
    if ((item.is('.block-anim--each-3-md-js:nth-child(3n+3)') && window.innerWidth > 767)
        || (item.is('.block-anim--each-4-md-js:nth-child(4n+3)') && window.innerWidth > 767)) {
        delay = .2
    }
    if (item.is('.block-anim--each-4-md-js:nth-child(4n+4)') && window.innerWidth > 767) {
        delay = .3
    }
    if ((item.is('.block-anim--each-2-lg-js:nth-child(2n+2)') && window.innerWidth > 991)
        || (item.is('.block-anim--each-3-lg-js:nth-child(3n+2)') && window.innerWidth > 991)
        || (item.is('.block-anim--each-4-lg-js:nth-child(4n+2)') && window.innerWidth > 991)) {
        delay = .1
    }
    if ((item.is('.block-anim--each-3-lg-js:nth-child(3n+3)') && window.innerWidth > 991)
        || (item.is('.block-anim--each-4-lg-js:nth-child(4n+3)') && window.innerWidth > 991)) {
        delay = .2
    }
    if (item.is('.block-anim--each-4-lg-js:nth-child(4n+4)') && window.innerWidth > 991) {
        delay = .3
    }
    if ((item.is('.block-anim--each-2-xl-js:nth-child(2n+2)') && window.innerWidth > 1199)
        || (item.is('.block-anim--each-3-xl-js:nth-child(3n+2)') && window.innerWidth > 1199)
        || (item.is('.block-anim--each-4-xl-js:nth-child(4n+2)') && window.innerWidth > 1199)) {
        delay = .1
    }
    if ((item.is('.block-anim--each-3-xl-js:nth-child(3n+3)') && window.innerWidth > 1199)
        || (item.is('.block-anim--each-4-xl-js:nth-child(4n+3)') && window.innerWidth > 1199)) {
        delay = .2
    }
    if (item.is('.block-anim--each-4-xl-js:nth-child(4n+4)') && window.innerWidth > 1199) {
        delay = .3
    }
    if (item.is('.block-anim--each-parent')) {
        let parent = item.parent();
        if (item.is('.block-anim--each-parent-2-js') && parent.is(':nth-child(2n+2)')
            || item.is('.block-anim--each-parent-3-js') && parent.is(':nth-child(3n+2)')
            || item.is('.block-anim--each-parent-4-js') && parent.is(':nth-child(4n+2)')) {
            delay = .1
        }
        if (item.is('.block-anim--each-parent-3-js') && parent.is(':nth-child(3n+3)')
            || item.is('.block-anim--each-parent-4-js') && parent.is(':nth-child(4n+3)')) {
            delay = .2
        }
        if (item.is('.block-anim--each-parent-4-js') && parent.is(':nth-child(4n+4)')) {
            delay = .3
        }
        if ((item.is('.block-anim--each-2-sm-js') && parent.is(':nth-child(2n+2)') && window.innerWidth > 575)
            || (item.is('.block-anim--each-3-sm-js') && parent.is(':nth-child(3n+2)') && window.innerWidth > 575)
            || (item.is('.block-anim--each-4-sm-js') && parent.is(':nth-child(4n+2)') && window.innerWidth > 575)) {
            delay = .1
        }
        if ((item.is('.block-anim--each-3-sm-js') && parent.is(':nth-child(3n+3)') && window.innerWidth > 575)
            || (item.is('.block-anim--each-4-sm-js') && parent.is(':nth-child(4n+3') && window.innerWidth > 575)) {
            delay = .2
        }
        if (item.is('.block-anim--each-4-sm-js') && parent.is(':nth-child(4n+4)') && window.innerWidth > 575) {
            delay = .3
        }
        if ((item.is('.block-anim--each-2-md-js') && parent.is(':nth-child(2n+2)') && window.innerWidth > 767)
            || (item.is('.block-anim--each-3-md-js') && parent.is(':nth-child(3n+2)') && window.innerWidth > 767)
            || (item.is('.block-anim--each-4-md-js') && parent.is(':nth-child(4n+2)') && window.innerWidth > 767)) {
            delay = .1
        }
        if ((item.is('.block-anim--each-3-md-js') && parent.is(':nth-child(3n+3)') && window.innerWidth > 767)
            || (item.is('.block-anim--each-4-md-js') && parent.is(':nth-child(4n+3)') && window.innerWidth > 767)) {
            delay = .2
        }
        if (item.is('.block-anim--each-4-md-js') && parent.is(':nth-child(4n+4)') && window.innerWidth > 767) {
            delay = .3
        }
        if ((item.is('.block-anim--each-2-lg-js') && parent.is(':nth-child(2n+2)') && window.innerWidth > 991)
            || (item.is('.block-anim--each-3-lg-js') && parent.is(':nth-child(3n+2)') && window.innerWidth > 991)
            || (item.is('.block-anim--each-4-lg-js') && parent.is(':nth-child(4n+2)') && window.innerWidth > 991)) {
            delay = .1
        }
        if ((item.is('.block-anim--each-3-lg-js') && parent.is(':nth-child(3n+3)') && window.innerWidth > 991)
            || (item.is('.block-anim--each-4-lg-js') && parent.is(':nth-child(4n+3)') && window.innerWidth > 991)) {
            delay = .2
        }
        if (item.is('.block-anim--each-4-lg-js') && parent.is(':nth-child(4n+4)') && window.innerWidth > 991) {
            delay = .3
        }
        if ((item.is('.block-anim--each-2-xl-js') && parent.is(':nth-child(2n+2)') && window.innerWidth > 1199)
            || (item.is('.block-anim--each-3-xl-js') && parent.is(':nth-child(3n+2)') && window.innerWidth > 1199)
            || (item.is('.block-anim--each-4-xl-js') && parent.is(':nth-child(4n+2)') && window.innerWidth > 1199)) {
            delay = .1
        }
        if ((item.is('.block-anim--each-3-xl-js') && parent.is(':nth-child(3n+3)') && window.innerWidth > 1199)
            || (item.is('.block-anim--each-4-xl-js') && parent.is(':nth-child(4n+3)') && window.innerWidth > 1199)) {
            delay = .2
        }
        if (item.is('.block-anim--each-4-xl-js') && parent.is(':nth-child(4n+4)') && window.innerWidth > 1199) {
            delay = .3
        }
    }
    return delay;
}
function setMaxHeightForCaptions() {
    let captions = $('.swiper__caption-js');
    if(captions.length) {
        let maxHeight = 0;
        captions.each(function () {
            let elementHeight = $(this).outerHeight(true);
            if (elementHeight > maxHeight) {
                maxHeight = elementHeight;
            }
        });
        $('.swiper__captions-js').css('height', maxHeight + 'px');
    }
}
setMaxHeightForCaptions();
if (isSafari()) {
    document.documentElement.classList.add('safari-browser');
}
if(isWindows()) {
    document.documentElement.classList.add('windows-browser');
}

//-----------------------------
    let blocks_anim = $('.block-anim-js');
    if (blocks_anim.length) {
        blocks_anim.each(function (index, item) {
            let $item = $(item),
                start_trigger = 'top bottom-=100px',
                trigger_block = item,
                y_set = 25,
                x_set = 0,
                duration_opacity = .5,
                duration_transform = .7;
            if (window.innerWidth > 991) {
                duration_opacity = .7;
                duration_transform = .9;
            }
            if ($item.is('.block-anim--trigger-top-js')) {
                start_trigger = 'top bottom';
            }
            if ($item.parent('.block-anim-wrap-js').length) {
                trigger_block = $item.parents('.block-anim-wrap-js');
            }
            if ($item.is('.block-anim--from-left-js')) {
                y_set = 0;
                x_set = '-70px';
            }
            if ($item.is('.block-anim--from-right-js')) {
                y_set = 0;
                x_set = '70px';
            }
            let delay = set_delay($item);
            let anim_tl = gsap.timeline({
                defaults: {
                    ease: 'power2.inOut',
                },
                scrollTrigger: {
                    trigger: trigger_block,
                    start: start_trigger,
                    pin: false,
                    once: true
                }
            });
            //    --------------------------
            let offset_opacity = 0;
            gsap.delayedCall(.05, function () {
                if (!$item.is('.block-anim--static-js')) {
                    offset_opacity = .1;
                    anim_tl.from(item, {
                        y: y_set,
                        x: x_set,
                        duration: duration_transform,
                        delay: delay
                    }, 0);
                }
                anim_tl.from(item, {
                    autoAlpha: 0,
                    duration: duration_opacity,
                    delay: delay
                }, offset_opacity);
            })
        });
    }


    //-----------------------------
    if ($('.container-anim-js').length) {
        gsap.set('.container-anim-js', {
            autoAlpha: 1,
            delay: .15,
        });
    }


    //-----------------------------
    
    let dropupBtns = $('.drop-block__btn-js');
    if (dropupBtns.length) {
        dropupBtns.on('click', function (e) {
            //e.preventDefault();
            let targetId = $(this).attr('href'),
                targetContent = $(targetId),
                hides = $($(this).data('hide-open')),
                overlay = $($(this).data('overlay'));
            if (targetContent.length) {
                if(targetId == '#search-block' && !targetContent.hasClass('is-open') ){
                    if($(window).width() > 768){
                        $('#header__login-block').removeClass('is-open');
                        $('[href="#header__login-block"]').removeClass('is-open');
                        $('#header__overlay').removeClass('show-overlay-2');
                    }

                    if($(window).width() < 768){
                        document.body.classList.remove('menu-open');
                        document.querySelector('#header__overlay').classList.remove('show-overlay-1');
                    }
                }
                $('body').toggleClass('is-open-menu');
                targetContent.toggleClass('is-open');
                $('.drop-block__btn-js[href="' + targetId + '"]').toggleClass('is-open');
                if ($(window).width() < 992 && $(this).hasClass('drop-block__btn-mob-slide-js')) {
                    targetContent.stop().slideToggle(300);
                }
            }
            if(hides.length) {
                hides.toggleClass('hide-when-open');
            }
            if(overlay.length) {
                overlay.toggleClass($(this).data('overlay-class'));
}           

            if($('body').hasClass('menu-open')){
                if($(window).width() > 768){
                document.body.classList.remove('menu-open');
                    document.querySelector('#header__overlay').classList.remove('show-overlay-1');
                }
            }
            return false;
        });
    }
    let drop_btn = $('.drop-block__btn-2-js');
    if(drop_btn.length) {
        drop_btn.on('click',function() {
            let targetId = $(this).attr('href'),
                targetContent = $(targetId);
            targetContent.toggleClass('is-open');
            return false;
        })
    }
    $('[data-panel]').on('click', function () {
        if(window.innerWidth < 992) {
            let panel = $(this).data('panel');
            $(panel).toggleClass('is-open');
            return false;
        }
    });
    let $searchInput = $('#search-block-input'), $resultsWrap = $('#search-block__results-list-wrap'),
        $popular = $('#search-block__popular');
    if ($searchInput) {
        $searchInput.on('input', function () {
            const inputVal = $(this).val().trim();
            if (inputVal.length > 0) {
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
        });
    }
    if ($('[data-scrollto]').length) {
        $('[data-scrollto]').on('click', function (event) {
            let elementId = $(this).data('scrollto');
            let trip = $(elementId).offset().top,
                paddingOffset = 0,
                idOffset = trip - paddingOffset;
            if (!isTouchDevice()) {
                bodyScrollBar.scrollIntoView(document.querySelector(elementId), {
                    offsetLeft: 0,
                    offsetTop: paddingOffset,
                    alignToTop: true,
                    onlyScrollIfNeeded: false,
                });
            } else {
                $('html,body').animate(
                    {
                        scrollTop: idOffset
                    },
                    2000
                );
            }

            return false;
        });
    }
    $('#header__overlay').on('click',function() {
        $(this).removeClass('show-overlay-1 show-overlay-2 show-overlay-3 show-overlay-4');
        if(window.innerWidth < 992) {
            $('.overlay-toggle-state-js.is-open:not(.drop-block__btn-mob-slide-js)').removeClass('is-open');
        } else {
            $('.overlay-toggle-state-js.is-open').removeClass('is-open');
        }
        $('#header__col-2.hide-when-open, #header__col-3.hide-when-open').removeClass('hide-when-open');
        $('body').removeClass('menu-open');
    })
    function header_st(this_) {
        let scroll_top = $(this_).scrollTop(),
            offset = 0;
        if (scroll_top > offset) {
            body.addClass('is-offset-top');
        }
        if (scroll_top <= offset) {
            body.removeClass('is-offset-top');
        }
    }
    header_st(window);
    lastScrollTop = 0;
    $(window).on('scroll', function () {
        header_st(this);
    // ----------------
        let currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (currentScrollTop > lastScrollTop) {
            document.body.classList.add('scroll-down');
        } else {
            document.body.classList.remove('scroll-down');
        }
        lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop;
    })
    //-----------------------------
var header = $('#header');
$(window).on('load', function () {
    if ($('.text-anim-by-line-js').length) {
        $('.text-anim-by-line-js').each(function () {
            let $element = $(this);
            let $firstSpan = $element.find('.color-1');
            if ($firstSpan.length) {
                let beforeText = $element.html().split($firstSpan.prop('outerHTML'))[0]?.trim();
                let afterText = $element.html().split($firstSpan.prop('outerHTML'))[1]?.trim();
                $firstSpan.addClass('text-anim-js');
                let newHtml = '';
                if (beforeText) {
                    newHtml += `<span class="text-anim-js">${beforeText}</span>`;
                }
                newHtml += $firstSpan.prop('outerHTML');

                if (afterText) {
                    newHtml += `<span class="text-anim-js">${afterText}</span>`;
                }
                $element.html(newHtml);
                $element.find('.text-anim-js br:first-child').remove();
            }
        });
    }

    //-----------------------------
    if(window.innerWidth < 768) {
        $('.s-scroll-banners__title,.s-pin-banners__title,.s-pin-banners__content-kicker,.s-pin-banners__hr').addClass('block-anim-js');
        if($('.s-scroll-banners__slide').length) {
            $('.s-scroll-banners__slide').addClass('block-anim-js block-anim--row-js');
        }
    }
    if(window.innerWidth > 991) {
        $('.s-team__card-col.col-lg-4:nth-child(3n + 1) .new-card').addClass('parallax-xx-js parallax-js-x').attr('data-parallax-value',5).attr('parallax-trigger-start','top bottom').attr('parallax-trigger-end','bottom center');
        $('.s-team__card-col.col-lg-4:nth-child(3n + 2) .new-card').addClass('parallax-y-js parallax-js').attr('data-parallax-value',-5).attr('parallax-trigger-start','top bottom').attr('parallax-trigger-end','bottom center');
        $('.s-team__card-col.col-lg-4:nth-child(3n + 3) .new-card').addClass('parallax-xx-js parallax-js-x').attr('data-parallax-value',-5).attr('parallax-trigger-start','top bottom').attr('parallax-trigger-end','bottom center');
    }
    if(window.innerWidth < 992) {
        if($('.s-table__block-wrap').length) {
            $('.s-table__block-wrap').removeClass('block-anim-js block-anim--static-js');
            $('.s-table__block-body-row').addClass('block-anim-js');
        }
        if($('.s-quote__pic-wrap').length) {
            $('.s-quote__pic-wrap.parallax-js').removeClass('parallax-js').addClass('block-anim-js');
        }
        let titles = $('.s-news__title,.s-faq__title');
        if(titles.length) {
            titles.find('.parallax-js').removeClass('parallax-js');
            titles.addClass('block-anim-js');
        }
        let steps_cards = $('.s-steps__card-wrap');
        if(steps_cards.length) {
            $('.s-steps__card-wrap .parallax-js').removeClass('parallax-js');
            $('.step-card').removeClass('block-anim-js');
            steps_cards.addClass('block-anim-js');
        }
    }
    if($('.content-block-anim-js').length) {
        $('.content-block-anim-js > *').addClass('block-anim-js');
    }
    //-----------------------------
    let parallaxes = $('.parallax-js');
    if (parallaxes.length) {
        parallaxes.each(function (i, el) {
            let $item = $(el),
                transform_value = $item.data('parallax-value') || 15,
                scale_value = 1.2,
                scrub_val = $item.data('parallax-scrub') || 0.7,
                start_pos = $item.data('parallax-trigger-start') || 'top bottom',
                end_pos = $item.data('parallax-trigger-end') || 'bottom top+=100px',
                trig = $item.parents('.parallax-trigger-js').length ? $item.parents('.parallax-trigger-js') : el;
            if ($item.is('.parallax-hero-js')) {
                start_pos = 'top top';
                end_pos = 'bottom top';
            }
            if ($item.is('.parallax-footer-js')) {
                end_pos = 'bottom-=5px bottom';
            }
            if ($item.data('parallax-scale')) {
                scale_value = $item.data('parallax-scale');
            }
            if ($item.is('.parallax-img-js')) {
                let translateY_val = $item.is('.parallax-y-js') ? transform_value : 0,
                    translateX_val = $item.is('.parallax-x-js') ? transform_value : 0,
                    imgStyles = {
                        'height': `calc(100% + ${translateY_val}%)`,
                        'width': `calc(100% + ${translateX_val}%)`,
                        'top' : `-${translateY_val}%`,
                        'position' : 'relative'
                    };
                $item.css(imgStyles);
            }
            if ($item.is('.parallax-y-js:not(.parallax-img-js')) {
                let translateY_val = $item.is('.parallax-y-js') ? transform_value * .75 : 0,
                    imgStyles = {
                        'transform' : `translateY(-${translateY_val}%)`,
                    };
                $item.css(imgStyles);
            }
            if ($item.is('.parallax-x-js:not(.parallax-img-js')) {
                let translateY_val = $item.is('.parallax-x-js') ? transform_value * .75 : 0,
                    imgStyles = {
                        'transform' : `translateX(-${translateY_val}%)`,
                    };
                $item.css(imgStyles);
            }
            // console.log(trig)
            let parallax_tl = gsap.timeline({
                scrollTrigger: {
                    trigger: trig,
                    start: start_pos,
                    end: end_pos,
                    scrub: scrub_val,
                    // markers: true,
                    pin: false,
                    onEnter: () => {
                        if (isSafari()) $item.addClass('will-change-transform');
                    },
                    onLeave: () => {
                        if (isSafari()) $item.removeClass('will-change-transform');
                    },
                    onEnterBack: () => {
                        if (isSafari()) $item.addClass('will-change-transform');
                    },
                    onLeaveBack: () => {
                        if (isSafari()) $item.removeClass('will-change-transform');
                    }
                }
            });
            if ($item.is('.parallax-y-js')) {
                parallax_tl.to(el, {yPercent: transform_value, duration: 1, ease: 'none',force3D: true});
            }
            if ($item.is('.parallax-x-js')) {
                parallax_tl.to(el, {xPercent: transform_value, duration: 1, ease: 'none',force3D: true});
            }
            if ($item.is('.parallax-scale-js')) {
                if ($item.is('.parallax-scale--from-js')) {
                    scale_value = 0.6;
                    parallax_tl.from(el, {scale: scale_value, duration: 1, ease: 'none',force3D: true});
                } else {
                    parallax_tl.to(el, {scale: scale_value, duration: 1, ease: 'none',force3D: true});
                }
            }
            if ($item.is('.parallax-rotate-js')) {
                parallax_tl.to(el, {rotate: 60, duration: 1, ease: 'none',force3D: true});
            }
            if ($item.is('.parallax-def-js')) {
                let yTransformValue = $item.is('.parallax-def-reverse-js') ? -transform_value : transform_value;
                parallax_tl.to(el, {yPercent: yTransformValue, duration: 1, ease: 'none',force3D: true});
            }
            if ($item.is('.parallax-diagonally-js')) {
                parallax_tl.to(el, {xPercent: -transform_value, yPercent: -transform_value, duration: 1, ease: 'none',force3D: true});
            }
        });
    }
    

    //-----------------------------
    $('.cta-card').on('mouseenter',function() {
        let pic = $(this).data('pic');
        gsap.to('.s-bg-banner-cards__bg:not('+pic+')',{
            autoAlpha: 0,
            overwrite: 'auto'
        })
        gsap.to(pic,{
            autoAlpha: 1,
            overwrite: 'auto'
        })
    })
    $('.cta-card').on('mouseleave',function() {
        let pic = '.s-bg-banner-cards__bg--default';
        gsap.to('.s-bg-banner-cards__bg:not('+pic+')',{
            autoAlpha: 0,
            overwrite: 'auto'
        })
        gsap.to(pic,{
            autoAlpha: 1,
            overwrite: 'auto'
        })
    })
    //-----------------------------
    let text_anim = $('.text-anim-js');
    if (text_anim.length) {
        text_anim.each(function (index, item) {
            let $item = $(item),
                convert_to_line = item,
                start_trigger = 'top bottom-=100px',
                trigger_block = item,
                y_set = 40,
                duration_opacity = .5,
                duration_transform = .6,
                ease = 'power1.inOut',
                text_p = $(item).find('p,li,h4,h3,h5,h6'),
                is_text = text_p.length,
                is_global_list = $(item).is('.text-anim--global-list-js');
            if (text_p.length) {
                convert_to_line = text_p;
                ease = 'power2.inOut';
            }
            let txt = new SplitText(convert_to_line, {
                    type: 'lines',
                    linesClass: 'anim-txt-lines'
                }),
                // txt_wrap = new SplitText(convert_to_line, {
                //     type: 'lines',
                //     linesClass: 'anim-txt-lines-wrap'
                // }),
                anim_content = $(item).find('.anim-txt-lines');
            if ($item.is('.block-anim--trigger-1-js')) {
                start_trigger = 'top bottom';
            }
            if ($item.parent('.block-anim-wrap-js').length) {
                trigger_block = $item.parents('.block-anim-wrap-js');
            }

            let delay = set_delay($item);
            let anim_tl = gsap.timeline({
                defaults: {
                    ease: ease,
                },
                scrollTrigger: {
                    trigger: trigger_block,
                    start: start_trigger,
                    once: true,
                    pin: false,
                }
            });
            gsap.delayedCall(.05, function () {
                anim_tl
                .from(anim_content, {
                    y: y_set,
                    duration: duration_transform,
                    stagger: {
                        each: 0.15,
                        onComplete: function() {
                            if(is_text) {
                                let completedElement = this.targets()[0];
                                $(completedElement).parents('li').addClass('line-anim-end');
                            }
                            if(is_global_list) {
                                let completedElement = this.targets()[0];
                                $(completedElement).parents('.text-anim--global-list-js').addClass('global-line-anim-end');
                            }
                        }
                    },
                    delay: delay,
                }, 0)
                .from(anim_content, {
                    autoAlpha: 0,
                    duration: duration_opacity,
                    stagger: .15,
                    delay: delay
                }, 0.1);
            })
            // gsap.set($(trigger_block).parents('.container-anim-js'), {
            //     autoAlpha: 1,
            //     delay: .1,
            // });
        })
    }
    
    
    if (!isTouchDevice() && isSafari()) {
        gsap.utils.toArray(
            '.s-parallax-banner__bg-wrap,.s-bg-banner__container, .s-promo-banner__title, .s-parallax-banner__container, .s-scroll-banners__btn-wrap,.s-bg-banner-cards__container,.s-promo-banner__pic-wrap,.s-explore__bg-wrap,.s-college__title-wrap,.hero-about__title,.hero-contact__bg-wrap,.hero-news__bg-wrap,.s-gallery-slider__swiper'
        ).forEach(el => {
            const tl = gsap.timeline({
                scrollTrigger: {
                    trigger: el,
                    start: 'top bottom',
                    end: 'bottom top',
                    onEnter: () => {
                        if (isSafari()) $(el).addClass('set-will-change-transform');
                    },
                    onLeave: () => {
                        if (isSafari()) $(el).removeClass('set-will-change-transform');
                    },
                    onEnterBack: () => {
                        if (isSafari()) $(el).addClass('set-will-change-transform');
                    },
                    onLeaveBack: () => {
                        if (isSafari()) $(el).removeClass('set-will-change-transform');
                    }
                }
            });
        });

    }
    //-----------------------------
    let counters = $('.counter-js');
    if (counters.length) {
        counters.each(function (index, item) {
            let $item = $(item),
                start_trigger = 'top bottom-=100px',
                $block = $(this).parents('.block-counter-js'),
                y_set = 25,
                x_set = 0,
                trigger = $block,
                duration_opacity = .5,
                duration_transform = .7,
                duration_count = 1,
                delay = set_delay($block),
                end_value = String($item.data('finish')),
                increment_value = $item.data('increment');
            if (!increment_value) {
                increment_value = 1;
            }
            if (window.innerWidth < 992) {
                start_trigger = 'top bottom-=50px';
            }
            if ($block.is('.counter-wrap-block-is-js') && window.innerWidth > 991) {
                trigger = $block.parents('.block-counter-block-js');
            }
            //---------------------------------------

            let tl_count = gsap.timeline({
                defaults: {
                    duration: .7,
                    ease: 'power1.inOut',
                },
                scrollTrigger: {
                    trigger: trigger,
                    start: start_trigger,
                    pin: false,
                }
            });
            if (!$block.is('.block-counter--anim-not-js')) {
                let offset_opacity = 0;
                gsap.delayedCall(.05, function () {
                    if (!$block.is('.block-anim--static-js')) {
                        offset_opacity = .1;
                        tl_count
                        .from($block, {
                            y: y_set,
                            x: x_set,
                            duration: duration_transform,
                            delay: delay
                        })
                        .from($block, {
                            autoAlpha: 0,
                            duration: duration_opacity,
                            delay: delay
                        }, offset_opacity)
                        .counter(item, {
                            end: end_value,
                            increment: increment_value,
                            duration: duration_count
                        }, '<+=.25');
                    }
                    if ($block.is('.block-anim--static-js')) {
                        tl_count.from($block, {
                            autoAlpha: 0,
                            duration: duration_opacity,
                            delay: delay
                        }, offset_opacity)
                        .counter(item, {
                            end: end_value,
                            increment: increment_value,
                            duration: duration_count
                        }, '<+=.25');
                    }
                })
            }
            if ($block.is('.block-counter--anim-not-js')) {
                tl_count.counter(item, {end: end_value, increment: increment_value, duration: duration_count});
            }
        });
    }
    
    //-----------------------------
    if(window.innerWidth > 991) {
        $('.s-table__block-headings-js').each(function (i, el) {
            let section = $(el).parents('.s-table__block'),
                container = $(el).find('.s-table__block-headings-container-js'),
                pin_wrap = null;
                let lastDirection = null;
            let pin_tl = gsap.timeline({
                scrollTrigger: {
                    trigger: section,
                    pin: el,
                    pinSpacing: false,
                    start: () => {
                        // return 'top top+=' + (header.innerHeight() + 9);
                        return 'top top';
                    },
                    end: () => {
                        // return 'bottom-=' + $(el).innerHeight() + ' top+=' + (header.innerHeight() + 9);
                        return 'bottom-=' + $(el).innerHeight() + ' top';
                    },
                    onEnter: () => {
                        if (isSafari()) pin_wrap.addClass('will-change-transform');
                    },
                    onLeave: () => {
                        if (isSafari()) pin_wrap.removeClass('will-change-transform');
                    },
                    onEnterBack: () => {
                        if (isSafari()) pin_wrap.addClass('will-change-transform');
                    },
                    onLeaveBack: () => {
                        if (isSafari()) pin_wrap.removeClass('will-change-transform');
                    },
                    onUpdate: (self) => {
                        let direction = self.direction;
                        let progress = self.progress;
                        if (progress === 0 || progress === 1) {
                            gsap.to(container, {
                                y: 0,
                                duration: 0.3,
                                overwrite: true,
                            });
                            lastDirection = null;
                            return;
                        }
                        if (direction !== lastDirection) {
                            if (direction === 1) {
                                gsap.to(container, {
                                    y: 0,
                                    duration: 0.3,
                                    overwrite: true,
                                });
                            } else if (direction === -1) {
                                gsap.to(container, {
                                    y: function() {
                                        return (header.innerHeight() + 9);
                                    },
                                    duration: 0.3,
                                    overwrite: true,
                                });
                            }
                            lastDirection = direction;
                        }
                    },
                    // markers: true,
                }
            });
            pin_wrap = $(el).parents('.pin-spacer');
        });
    }
    
    let swiper_def_btns = $('.swiper-def-btns-js');
    if (swiper_def_btns.length) {

        swiper_def_btns.each(function (index, item) {
            let spaceBetween = 21;
            if($(item).is('.s-vacancies__swiper-js')) {
                spaceBetween = 10;
            }
            let swiper = new Swiper(item, {
                slidesPerView: 'auto',
                spaceBetween: 16,
                speed: 900,
                slideToClickedSlide: true,
                breakpoints: {
                    576: {
                        spaceBetween: spaceBetween,
                    },
                }
            });
        })
    }
    //-----------------------------
    let gallery = $('.s-gallery-slider__swiper-js');
    if(gallery) {
        let swiper_gallery = new Swiper('.s-gallery-slider__swiper-js', {
            speed: 900,
            spaceBetween: 20,
            navigation: {
                nextEl: '.swiper-btn--next',
                prevEl: '.swiper-btn--prev',
            },
            pagination: {
                el: '.swiper-pagination',
                type: 'fraction',
                formatFractionCurrent: function (number) {
                    return number;
                }
            },
            on: {
                slideChange: function () {
                    let activeIndex = this.activeIndex,
                        slider = $(this.el);
                    slider.find('.swiper__caption-js').removeClass('is-active');
                    slider.find('.swiper__caption-'+activeIndex+'-js').addClass('is-active');
                }
            }
        });
    }
    //-----------------------------
    let swiper_def_lg = $('.swiper-md-def-js');
    if (swiper_def_lg.length && window.innerWidth < 768) {
        swiper_def_lg.each(function (index, item) {
            let swiper = new Swiper(item, {
                slidesPerView: 'auto',
                spaceBetween: 10,
                speed: 900,
            });
        })
    }
    //-----------------------------
    let mob_toggle_txt = $('.s-pin-banners__btn-circle-js');
    //-----------------------------
    if (mob_toggle_txt.length) {
        mob_toggle_txt.on('click', function () {
            let section = $(this).data('block'),
                txt = $(this).data('slide');
            $(section).toggleClass('is-open');
            $(txt).stop().slideToggle(400, function() {
                ScrollTrigger.refresh(true);
            });
        })
    }
    //-----------------------------
    if($('.s-scroll-banners').length && window.innerWidth > 767) {
        $('.s-scroll-banners').each(function(i, item) {
            let wrapper = $(this).find('.s-scroll-banners__pics-wrap'),
                slides = $(this).find('.s-scroll-banners__slide');
            let parallax_tl = gsap.timeline({
                scrollTrigger: {
                    trigger: wrapper,
                    // markers: true,
                    start: 'top bottom',
                    end: 'bottom top',
                    scrub: .7,
                    onEnter: () => {
                        if (isSafari()) wrapper.addClass('will-change-transform');
                    },
                    onLeave: () => {
                        if (isSafari()) wrapper.removeClass('will-change-transform');
                    },
                    onEnterBack: () => {
                        if (isSafari()) wrapper.addClass('will-change-transform');
                    },
                    onLeaveBack: () => {
                        if (isSafari()) wrapper.removeClass('will-change-transform');
                    }
                }
            });
            parallax_tl.to(wrapper, {
                xPercent: -10,
                force3D: true
            });
        });
    }
    //-----------------------------
    if($('.s-pin-banners').length && window.innerWidth > 767) {
        let parallax_tl = gsap.timeline({
            defaults: {
                ease: 'none',
            },
            scrollTrigger: {
                trigger: '.s-pin-banners-wrap-h',
                pin: '.s-pin-banners',
                pinSpacing: false,
                // markers: true,
                start: 'top top',
                end: 'bottom bottom',
                scrub: .7,
                onEnter: function() {
                  gsap.to('#header',{autoAlpha: 0})
                },
                onLeave: function() {
                    gsap.to('#header',{autoAlpha: 1})
                },
                onEnterBack: function() {
                    gsap.to('#header',{autoAlpha: 0})
                },
                onLeaveBack: function() {
                    gsap.to('#header',{autoAlpha: 1})
                },
            }
        });
        let lastState_1 = null,
            lastState_2 = null,
            lastState_3 = null,
            only_once_1 = true,
            only_once_2 = true,
            only_once_3 = true;
        parallax_tl
        .to('.s-pin-banners__contents-pic-wrap--1',{
            height: 0,
            duration: 1,
            onUpdate: function () {
                const progress = this.progress()
                const currentState = progress > 0.5 ? 'visible' : 'hidden';
                if (currentState !== lastState_1) {
                    lastState_1 = currentState;
                    if (currentState === 'visible') {
                        if(only_once_1) {
                            gsap.to('.s-pin-banners__content--1', {
                                autoAlpha: 0,
                                ease: 'power2.inOut',
                                duration: 0.9,
                                delay: .1,
                            });
                            gsap.to(['.s-pin-banners__content--2 .s-pin-banners__title','.s-pin-banners__content--2 .s-pin-banners__txt-wrap'], {
                                y: 0,
                                stagger: .15,
                                ease: 'power2.inOut',
                                duration: 1,
                            });
                            only_once_1 = false;
                        } else {
                            gsap.to('.s-pin-banners__content--1', {
                                autoAlpha: 0,
                                duration: 0.5,
                            });
                        }
                        gsap.set('.s-pin-banners__amount-block-numb-txt--1',{
                            autoAlpha: 0,
                        })
                    } else {
                        gsap.to('.s-pin-banners__content--1', {
                            autoAlpha: 1,
                            duration: 0.5,
                        });
                        gsap.set('.s-pin-banners__amount-block-numb-txt--1',{
                            autoAlpha: 1,
                        })
                    }
                }
            }
        })
        .to('.s-pin-banners__contents-pic-wrap--2 .s-pin-banners__contents-pic',{
            scale: 1,
            duration: 1,
        },0)
        .to('.s-pin-banners__contents-pic-wrap--2',{
            height: 0,
            duration: 1,
            onUpdate: function () {
                const progress = this.progress()
                const currentState = progress > 0.5 ? 'visible' : 'hidden';
                if (currentState !== lastState_2) {
                    lastState_2 = currentState;
                    if (currentState === 'visible') {
                        if(only_once_2) {
                            gsap.to('.s-pin-banners__content--2', {
                                autoAlpha: 0,
                                ease: 'power2.inOut',
                                duration: 0.9,
                                delay: .1,
                            });
                            gsap.to(['.s-pin-banners__content--3 .s-pin-banners__title','.s-pin-banners__content--3 .s-pin-banners__txt-wrap'], {
                                y: 0,
                                stagger: .15,
                                ease: 'power2.inOut',
                                duration: 1,
                            });
                            only_once_2 = false;
                        } else {
                            gsap.to('.s-pin-banners__content--2', {
                                autoAlpha: 0,
                                duration: 0.5,
                            });
                        }
                        gsap.set('.s-pin-banners__amount-block-numb-txt--2',{
                            autoAlpha: 0,
                        });
                    } else {
                        gsap.to('.s-pin-banners__content--2', {
                            autoAlpha: 1,
                            duration: 0.5,
                        });
                        gsap.set('.s-pin-banners__amount-block-numb-txt--2',{
                            autoAlpha: 1,
                        })
                    }
                }
            }
        })
        .to('.s-pin-banners__contents-pic-wrap--3 .s-pin-banners__contents-pic',{
            scale: 1,
            duration: 1,
        },1)
        .to('.s-pin-banners__contents-pic-wrap--3',{
            height: 0,
            duration: 1,
            onUpdate: function () {
                const progress = this.progress();
                const currentState = progress > 0.5 ? 'visible' : 'hidden';
                if (currentState !== lastState_3) {
                    lastState_3 = currentState;
                    if (currentState === 'visible') {
                        if(only_once_3) {
                            gsap.to('.s-pin-banners__content--3', {
                                autoAlpha: 0,
                                ease: 'power2.inOut',
                                duration: 0.9,
                                delay: .1,
                            });
                            gsap.to(['.s-pin-banners__content--4 .s-pin-banners__title','.s-pin-banners__content--4 .s-pin-banners__txt-wrap'], {
                                y: 0,
                                stagger: .15,
                                ease: 'power2.inOut',
                                duration: 1,
                            });
                            only_once_3 = false;
                        } else {
                            gsap.to('.s-pin-banners__content--3', {
                                autoAlpha: 0,
                                duration: 0.5,
                            });
                        }
                        gsap.set('.s-pin-banners__amount-block-numb-txt--3',{
                            autoAlpha: 0,
                        })
                    } else {
                        gsap.to('.s-pin-banners__content--3', {
                            autoAlpha: 1,
                            duration: 0.5,
                            delay: .1,
                        });
                        gsap.set('.s-pin-banners__amount-block-numb-txt--3',{
                            autoAlpha: 1,
                        })
                    }
                }
            }
        })
        .to('.s-pin-banners__contents-pic-wrap--4 .s-pin-banners__contents-pic',{
            scale: 1,
            duration: 1,
        },2)

    }
    //-----------------------------
    if($('.s-promo-banner__big-txt').length) {
        let parallax_tl = gsap.timeline({
            scrollTrigger: {
                trigger: '.s-promo-banner__big-txt',
                // markers: true,
                start: 'top bottom',
                end: 'bottom top',
                scrub: .7,
                onEnter: () => {
                    if (isSafari()) $('.s-promo-banner__big-txt-line').addClass('will-change-transform');
                },
                onLeave: () => {
                    if (isSafari()) $('.s-promo-banner__big-txt-line').removeClass('will-change-transform');
                },
                onEnterBack: () => {
                    if (isSafari()) $('.s-promo-banner__big-txt-line').addClass('will-change-transform');
                },
                onLeaveBack: () => {
                    if (isSafari()) $('.s-promo-banner__big-txt-line').removeClass('will-change-transform');
                }
            }
        });
        parallax_tl
        .to('.s-promo-banner__big-txt-line--1', {
            xPercent: -30,
            force3D: true
        })
        .to('.s-promo-banner__big-txt-line--2', {
            xPercent: 30,
            force3D: true
        },0);
    }
    
})
/**--------------------------------------*/

/**** */
//-----------------------------
    let acc_items = $('.acc-items-js');
    if (acc_items.length) {
        acc_items.each(function (index, item) {
            $(item).find('.acc-title-js:not(.acc-title-disable-js)').on('click', function () {
                let content = $(this).siblings('.acc-content-js'),
                    active_content = $(item).find('.acc-item-js.open  .acc-content-js'),
                    active_block = $(this).parents('.acc-item-js').siblings('.acc-item-js.open');
                let is_wrap = !!$(this).parents('.acc-item-wrap-js').length;
                if (is_wrap) {
                    active_block = $(this).parents('.acc-item-wrap-js').siblings('.acc-item-wrap-js').find('.acc-item-js.open');
                }
                let block_ = $(this).parents('.acc-item-js');
                if (block_.is('.open')) {
                    block_.removeClass('open');
                    if (is_wrap) {
                        block_.parent('.acc-item-wrap-js').removeClass('open-wrap');
                    }
                    content.stop().slideUp(400, function () {
                        ScrollTrigger.refresh(true);
                    });
                } else {
                    if (active_block.length) {
                        active_block.removeClass('open');
                    }
                    if (active_content.length) {
                        active_content.stop().slideUp(400, function () {
                            ScrollTrigger.refresh(true);
                        });
                    }
                    if (is_wrap) {
                        block_.parent('.acc-item-wrap-js').addClass('open-wrap');
                    }
                    block_.addClass('open');
                    content.stop().slideDown(400, function () {
                        ScrollTrigger.refresh(true);
                    });
                }
                return false;
            });
        });
        $('.faq .acc-item-wrap-js:nth-child(2) .acc-item-js').addClass('open');
        $('.footer .acc-item-js:first-child').addClass('open');
        $('.acc-item-js.open').parent('.acc-item-wrap-js').addClass('open-wrap');
        $('.acc-title-init-open-js').parent('.acc-item-js').addClass('open');
        $('.acc-item-js.open .acc-content-js').show(0);
    }

    $('.modal-video-js').each(function (i, item) {
        let id_modal = $(this).parents('.modal-js').attr('id'),
            btns = $('.modal-toggle-btn-js[href="#' + id_modal + '"]'),
            modal = $('#' + id_modal);

        let player = new Plyr(item, {});

        gsap.set(modal, {
            clipPath: 'polygon(120% 0%, 220% 0%, 200% 100%, 100% 100%)',
            onComplete: function() {
                modal.addClass('set-up-anim-modal');
            }
        });
        btns.on('click', function () {
            if (modal.hasClass('is-open')) {
                gsap.to(modal, {
                    clipPath: 'polygon(100% 0%, 200% 0%, 220% 100%, 120% 100%)',
                    duration: 0.8,
                    ease: 'cubic-bezier(0.74, 0, 0.24, 0.99)',
                    overwrite: 'auto',
                    onComplete: function () {
                        modal.removeClass('is-open');
                        player.pause();
                        gsap.set(modal, {
                            clipPath: 'polygon(120% 0%, 220% 0%, 200% 100%, 100% 100%)',
                        });
                    },
                });
            } else {
                modal.addClass('is-open');
                gsap.to(modal, {
                    clipPath: 'polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)',
                    duration: 0.8,
                    ease: 'cubic-bezier(0.74, 0, 0.24, 0.99)',
                    overwrite: 'auto',
                    onStart: function () {
                        player.play();
                    },
                });
            }
            return false;
        });
    });
    $('.modal-event-btn-js').on('click',function() {
        let modal = $(this).attr('href');
        $(modal).toggleClass('is-open');
        return false;
    });
    $('.video-module-js').each(function(i, item) {
        let video = $(item).find('video'),
            btn = $(item).find('.video-module__btn-js');
        let player = new Plyr(video, {});
        video.on('ready', function() {
            let plyrWrapper = $(item).find('.plyr--full-ui');
            if (plyrWrapper.length) {
                plyrWrapper.append(btn);
            }
        });
        btn.on('click', function() {
            if ($(this).is('.play-video')) {
                $(this).removeClass('play-video');
                player.pause();
            } else {
                $(this).addClass('play-video');
                player.play();
            }
        });
        video.on('play', function() {
            btn.addClass('play-video');
        });
        video.on('pause', function() {
            btn.removeClass('play-video');
        });
    });

//----------------------------------------------------
(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
        typeof define === 'function' && define.amd ? define(factory) :
            (global = typeof globalThis !== 'undefined' ? globalThis : global || self, global.VenoBox = factory());
}(this, (function () { 'use strict';

    /**
     * VenoBox 2.1.8
     * Copyright 2013-2024 Nicola Franchini
     * @license: https://github.com/nicolafranchini/VenoBox/blob/master/LICENSE
     */
    let backdrop, blocknum, blockshare, blocktitle, core, container, content, current_item, current_index, diffX, diffY, endY, elPreloader, elPreloaderInner;
    let gallIndex, images, infinigall, items, navigationDisabled, newcontent, numeratio, nextok, prevok, overlay;
    let set_maxWidth, set_overlayColor, set_ratio, set_autoplay, set_href, set_customclass, set_fitview, startY, thenext, theprev, thisborder, thisgall, title, throttle;

    const svgOpen = '<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor">';
    const svgClose = '</svg>';
    const downloadIcon = svgOpen + '<path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/><path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>' + svgClose;
    const shareIcon = svgOpen + '<path fill-rule="evenodd" d="M3.5 6a.5.5 0 0 0-.5.5v8a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5v-8a.5.5 0 0 0-.5-.5h-2a.5.5 0 0 1 0-1h2A1.5 1.5 0 0 1 14 6.5v8a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 14.5v-8A1.5 1.5 0 0 1 3.5 5h2a.5.5 0 0 1 0 1h-2z"/><path fill-rule="evenodd" d="M7.646.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 1.707V10.5a.5.5 0 0 1-1 0V1.707L5.354 3.854a.5.5 0 1 1-.708-.708l3-3z"/>' + svgClose;
    const linkIcon = svgOpen + '<path fill-rule="evenodd" d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z"/><path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/><path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>' + svgClose;

    let startX = 0;
    let endX = 0;
    let diff = 0;
    let threshold = 50;
    let startouch = false;
    let imagesHolder = false;
    let imgLoader = false;
    let clonecontent;
    let canDrag = false;

    const spinners = {
        'bounce': ['sk-bounce', 'sk-bounce-dot', 2],
        'chase': ['sk-chase', 'sk-chase-dot', 6],
        'circle': ['sk-circle', 'sk-circle-dot', 12],
        'circle-fade': ['sk-circle-fade', 'sk-circle-fade-dot', 12],
        'flow': ['sk-flow', 'sk-flow-dot', 3],
        'fold': ['sk-fold', 'sk-fold-cube', 4],
        'grid': ['sk-grid', 'sk-grid-cube', 9],
        'plane': ['sk-plane', '', 0],
        'pulse': ['sk-pulse', '', 5],
        'swing': ['sk-swing', 'sk-swing-dot', 2],
        'wander': ['sk-wander', 'sk-wander-cube', 3],
        'wave': ['sk-wave', 'sk-wave-rect', 5]
    };

    // Default settings
    const defaults = {
        selector: '.venobox',
        autoplay : false,
        bgcolor: '#fff',
        border: '0',
        customClass: false,
        infinigall: false,
        maxWidth: '100%',
        navigation: true,
        navKeyboard: true,
        navTouch: true,
        navSpeed: 300,
        numeration: false,
        overlayClose: true,
        overlayColor: 'rgba(23,23,23,0.95)',
        popup: false,
        ratio: '16x9', // '1x1' | '4x3' | '16x9' | '21x9'
        share: false,
        shareStyle: 'pill', // 'bar' | 'block' | 'pill' | 'transparent'
        spinner: 'bounce', // 'plane' | 'chase' | 'bounce' | 'wave' | 'pulse' | 'flow' | 'swing' | 'circle' | 'circle-fade' | 'grid' | 'fold' | 'wander'
        spinColor : '#d2d2d2',
        titleattr: 'title',
        titlePosition: 'top', // 'top' || 'bottom'
        titleStyle: 'bar', // 'bar' | 'block' | 'pill' | 'transparent'
        toolsBackground: '#1C1C1C', // 'transparent'
        toolsColor: '#d2d2d2',
        onPreOpen: function(){ return true; }, // Return the selected object - set return false to prevent opening
        onPostOpen: function(){}, // Return: current_item, gallIndex, thenext, theprev
        onPreClose: function(){ return true; }, // Return: current_item, gallIndex, thenext, theprev - set return false to prevent closing
        onNavComplete: function(){}, // Return: current_item, gallIndex, thenext, theprev
        onContentLoaded: function(){}, // Return: newcontent
        onInit: function(){}, // Return: plugin obj
        jQuerySelectors: false,
        focusItem: false,
        fitView: false,
        initialScale: 0.9,
        transitionSpeed: 200
    };

    /**
     * Generate spinner html
     * @param {Array} spinarray Selected spinner
     */
    function createspinner(spinarray){
        if (!spinarray) {
            return 'Loading...';
        }
        let spinner = '<div class="sk-center ' + spinarray[0] + '">';
        let i = 0;
        for (i = 0; i < spinarray[2]; i++) {
            spinner += '<div class="' + spinarray[1] + '"></div>';
        }
        spinner += '</div>';
        return spinner;
    }

    /**
     * A simple forEach() implementation for Arrays, Objects and NodeLists
     * @param {Array|Object|NodeList} collection Collection of items to iterate
     * @param {Function} callback Callback function for each iteration
     * @param {Array|Object|NodeList} scope Object/NodeList/Array that forEach is iterating over (aka `this`)
     */
    function forEach(collection, callback, scope) {
        if (Object.prototype.toString.call(collection) === '[object Object]') {
            let prop;
            for (prop in collection) {
                if (Object.prototype.hasOwnProperty.call(collection, prop)) {
                    callback.call(scope, collection[prop], prop, collection);
                }
            }
        } else {
            let i = 0;
            let len = collection.length;
            for (i = 0; i < len; i++) {
                callback.call(scope, collection[i], i, collection);
            }
        }
    }

    /**
     * Merge defaults with user options
     * @param {Object} defaults Default settings
     * @param {Object} options User options
     * @returns {Object} Merged values of defaults and options
     */
    function extend( defaults, options ) {
        let extended = {};

        forEach(defaults, function (value, prop) {
            extended[prop] = defaults[prop];
        });

        forEach(options, function (value, prop) {
            extended[prop] = options[prop];
        });
        return extended;
    }

    /**
     * Linear animation timing
     */
    function timingLinear(timeFraction){
        return timeFraction;
    }

    /**
     * Animate with callback
     * https://javascript.info/js-animation
     */
    function animate({timing, draw, duration}) {
        let start = performance.now();
        requestAnimationFrame(function animate(time) {
            // timeFraction goes from 0 to 1
            let timeFraction = (time - start) / duration;
            if (timeFraction > 1) {
                timeFraction = 1;
            }
            // calculate the current animation state
            let progress = timing(timeFraction);
            draw(progress); // draw it
            if (timeFraction < 1) {
                requestAnimationFrame(animate);
            }
        });
    }

    /**
     * Parse Youtube or Vimeo videos and get host & ID
     */
    function parseVideo(url) {
        let type, match, vid;
        let regYt = /(https?:\/\/)?((www\.)?(youtube(-nocookie)?|youtube.googleapis)\.com.*(v\/|v=|vi=|vi\/|e\/|embed\/|user\/.*\/u\/\d+\/)|youtu\.be\/)([_0-9a-z-]+)/i;
        match = url.match(regYt);
        if (match && match[7]) {
            type = 'youtube';
            vid = match[7];
        } else {
            let regVim = /^.*(vimeo\.com\/)((channels\/[A-z]+\/)|(groups\/[A-z]+\/videos\/))?([0-9]+)/;
            match = url.match(regVim);
            if (match && match[5]) {
                type = 'vimeo';
                vid = match[5];
            }
        }
        return {
            type: type,
            id: vid
        };
    }

    /**
     * Get additional url parameters
     */
    function getUrlParameter(url) {
        let result = '';
        let sPageURL = decodeURIComponent(url);
        let firstsplit = sPageURL.split('?');

        if (firstsplit[1] !== undefined) {
            let sURLVariables = firstsplit[1].split('&');
            let sParameterName;
            let i;
            for (i = 0; i < sURLVariables.length; i++) {
                sParameterName = sURLVariables[i].split('=');
                result = result + '&'+ sParameterName[0]+'='+ sParameterName[1];
            }
        }
        return encodeURI(result);
    }

    /**
     * Get all images from string
     */
    function getImages(string) {
        imagesHolder.innerHTML = string;
        return imagesHolder.querySelectorAll('img');
    }

    /**
     * Update item settings.
     */
    function updateVars(obj){
        if (!obj) {
            return false;
        }
        navigationDisabled = true;
        current_item = obj;
        nextok = false;
        prevok = false;
        set_maxWidth = obj.getAttribute("data-maxwidth") || obj.settings.maxWidth;
        set_overlayColor = obj.getAttribute("data-overlay") || obj.settings.overlayColor;
        set_ratio = obj.getAttribute("data-ratio") || obj.settings.ratio;
        set_autoplay = obj.hasAttribute("data-autoplay") || obj.settings.autoplay;
        set_href = obj.getAttribute("data-href") || obj.getAttribute('href');
        set_customclass = obj.getAttribute("data-customclass") || obj.settings.customClass;
        title = obj.getAttribute(obj.settings.titleattr) || '';
        thisborder = obj.getAttribute("data-border") || obj.settings.border;
        set_fitview = obj.hasAttribute("data-fitview") || obj.settings.fitView;
    }

    /**
     * Close modal.
     */
    function close() {
        if (!current_item || !document.body.classList.contains('vbox-open')) {
            return false;
        }
        if (current_item.settings.onPreClose && typeof current_item.settings.onPreClose === 'function') {
            if (current_item.settings.onPreClose(current_item, gallIndex, thenext, theprev) === false) {
                return false;
            }
        }

        document.body.removeEventListener('keydown', keyboardHandler);
        document.body.classList.remove('vbox-open');

        if (current_item.settings.focusItem) {
            current_item.focus();
        }

        animate({
            duration: 200,
            timing: timingLinear,
            draw: function(progress) {
                overlay.style.opacity =  1 - progress;
                if (progress === 1){
                    overlay.remove();
                }
            }
        });
    }

    /**
     * Navigate gallery.
     */
    function next() {
        navigateGall(thenext);
    }
    function prev() {
        navigateGall(theprev);
    }

    /**
     * Keyboard navigation.
     */
    function keyboardHandler(e) {
        if (e.keyCode === 27) { // esc
            close();
        }
        if (!throttle) {
            if (e.keyCode == 37 && prevok === true) { // <
                navigateGall(theprev);
            }
            if (e.keyCode == 39 && nextok === true) { // >
                navigateGall(thenext);
            }
            /* prevent keyboard processing until timer completed */
            throttle = setTimeout(() => {
                throttle = null;
            }, 100);
        }
    }

    /**
     * Append and fade-in new content
     */
    function contentLoaded(){

        navigationDisabled = false;

        content.style.opacity = 0;

        content.innerHTML = newcontent;
        dragListeners();

        let vboxChild = content.querySelector(":first-child");

        vboxChild.classList.add('vbox-child');

        vboxChild.style.backgroundColor = current_item.settings.bgcolor;
        // vboxChild.style.maxWidth = set_maxWidth;
        vboxChild.style.transform = 'scale('+ current_item.settings.initialScale +')';
        vboxChild.style.transition = 'transform '+ current_item.settings.transitionSpeed +'ms';

        // Fix weird drag
        let childImageLock = content.querySelector('.vbox-child img');

        if (childImageLock) {
            childImageLock.addEventListener('dragstart', function(e) {
                e.preventDefault();
            });
        }

        // reset content scroll
        container.scrollTo(0, 0);
        vboxChild.style.transform = 'scale(1)';

        overlay.style.setProperty('--vbox-padding', thisborder);
        overlay.style.setProperty('--vbox-max-width', set_maxWidth);

        // Reset custom classes.
        forEach(overlay.classList, function(obj){
            if (obj !== 'vbox-overlay') {
                overlay.classList.remove(obj);
            }
        });

        // Set custom class.
        if (set_customclass){
            overlay.classList.add(set_customclass);
        }

        // Set fitview class.
        if (set_fitview){
            content.classList.add('vbox-fit');
        } else {
            content.classList.remove('vbox-fit');
        }

        animate({
            duration: current_item.settings.transitionSpeed,
            timing: timingLinear,
            draw: function(progress) {
                content.style.opacity = progress;
                if (progress === 1){
                    elPreloader.classList.add('vbox-hidden');
                }
            }
        });
        if (current_item.settings.onContentLoaded && typeof current_item.settings.onContentLoaded === 'function') {
            current_item.settings.onContentLoaded(newcontent);
        }
    }

    /**
     * Check animation state
     * @param {string} state 'loading' | 'animated'
     */
    function checkState(state) {
        if (!content.classList.contains('vbox-' + state)) {
            contentLoaded();
        }
    }

    /**
     * Load iFrame
     */
    function loadIframe(dest, ratio){
        content.classList.add("vbox-loading");
        newcontent = '<div class="venoratio venoratio-' + ratio + '"><iframe src="' + dest + '"></iframe></div>';
        content.classList.remove("vbox-loading");
        checkState('animated');
    }

    /**
     * Load videos
     */
    function loadVid(dest, ratio, autoplay){

        content.classList.add("vbox-loading");
        let stringAutoplay;
        let videoObj = parseVideo(dest);

        if (videoObj.type == 'vimeo' || videoObj.type == 'youtube') {
            let player;

            // set rel=0 to hide related videos at the end of YT + optional autoplay
            stringAutoplay = autoplay ? "?rel=0&autoplay=1" : "?rel=0";
            let queryvars = stringAutoplay + getUrlParameter(dest);

            if (videoObj.type == 'vimeo') {
                player = 'https://player.vimeo.com/video/';
            } else if (videoObj.type == 'youtube') {
                player = 'https://www.youtube-nocookie.com/embed/';
            }
            newcontent = '<div class="venoratio venoratio-' + ratio + '"><iframe webkitallowfullscreen mozallowfullscreen allowfullscreen allow="autoplay" frameborder="0" src="'+player+videoObj.id+queryvars+'"></iframe></div>';
        } else {
            // // check if it's a video file - thanks to @alexxandar
            // if (/\.(mp4|ogg|ogv|mov|webm)$/i.test(dest)) {
            stringAutoplay = autoplay ? " autoplay" : "";
            newcontent = '<div class="venoratio venoratio-' + ratio + '"><video src="' + dest + '"' + stringAutoplay + ' controls>Your browser does not support the video tag.</video></div>';
            // }
        }

        content.classList.remove("vbox-loading");
        checkState('animated');
    }

    /**
     * Load inline content
     */
    function loadInline(dest){
        let inlineContent = document.querySelector(dest);
        if (inlineContent) {
            content.classList.add("vbox-loading");
            newcontent = '<div class="vbox-inline">' + inlineContent.innerHTML + '</div>';
            content.classList.remove("vbox-loading");
            checkState('animated');
        }
    }

    /**
     * Preload images from ajax call
     */
    function loadAjaxImages(){
        images = getImages(newcontent);
        if (images.length) {
            let imgCounter = 0;
            forEach(images, function(getimg){
                let srcimg = getimg.src;
                const ajaxImgLoader = new Image();
                ajaxImgLoader.onload = function(){
                    imgCounter++;
                    if ( imgCounter == images.length ) {
                        content.classList.remove("vbox-loading");
                        checkState('animated');
                    }
                };
                ajaxImgLoader.onerror = function(){
                    imgCounter++;
                    if ( imgCounter == images.length ) {
                        content.classList.remove("vbox-loading");
                        checkState('animated');
                    }
                };
                ajaxImgLoader.src = srcimg;
            });
        } else {
            content.classList.remove("vbox-loading");
            checkState('animated');
        }
    }

    /**
     * Load Ajax
     */
    function loadAjax(dest){
        content.classList.add("vbox-loading");
        let xhr = new XMLHttpRequest();
        xhr.open("GET", dest, true);
        xhr.onload = function() {
            newcontent = '<div class="vbox-inline">'+ xhr.response +'</div>';
            loadAjaxImages();
        };
        xhr.onerror = function() {
            newcontent = '<div class="vbox-inline"></div>';
            content.classList.remove("vbox-loading");
            checkState('animated');
        };
        xhr.send();
    }

    /**
     * Preload image
     */
    function loadImage(dest){
        imgLoader.onload = function(){
            // image  has been loaded
            newcontent = '<div class="vbox-child"><img src="' + dest + '"></div>';
            content.classList.remove('vbox-loading');
            checkState('animated');
        };
        imgLoader.src = dest;
    }

    /**
     * Start Drag
     */
    function dragStart(e) {
        if (!navigationDisabled) {
            let speed = current_item.settings.navSpeed * 0.84;
            content.style.transition =  "margin " + speed + "ms ease-out, opacity " + speed + "ms ease-out";
            startX = endX = e.type === "touchstart" ? e.touches[0].pageX : e.pageX;
            startY = endY = e.type === "touchstart" ? e.touches[0].pageY : e.pageY;
            startouch = true;
        }
    }

    /**
     * End Drag
     */
    function dragEnd(e) {
        if (startouch) {
            startouch = false;
            let subject = current_item;
            let change = false;
            diff = endX - startX;

            if (diff < 0 && nextok) {
                subject = thenext;
                change = true;
            }
            if (diff > 0 && prevok) {
                subject = theprev;
                change = true;
            }

            if (Math.abs(diff) >= threshold && change) {
                navigateGall(subject);
            } else {
                content.style.marginLeft = 0;
                content.style.opacity = 1;
            }
        }
    }

    /**
     * Drag items
     */
    function drag(e) {
        if (startouch && !navigationDisabled) {
            endX = e.type === "touchmove" ? e.touches[0].pageX : e.pageX;
            endY = e.type === "touchmove" ? e.touches[0].pageY : e.pageY;
            diffX = endX - startX;
            diffY = endY - startY;

            let absdiffX = Math.abs(diffX);
            let absdiffY = Math.abs(diffY);

            if (absdiffX > absdiffY && absdiffX <= 180) {
                let diffopac = (1 - absdiffX / 180) * 1.5;
                e.preventDefault();
                content.style.marginLeft = diffX + "px";
                content.style.opacity = diffopac;
            }
        }
    }

    function setShareButtons(href){
        // Navigator share
        if (navigator.canShare) {
            const shareData = {
                url: href
            };
            blockshare.insertAdjacentHTML('beforeend', '<div class="vbox-link-btn vbox-share-mobile">'+shareIcon+'</div>');
            const mobileShareBtn = blockshare.querySelector('.vbox-share-mobile');
            mobileShareBtn.addEventListener('click', function(e){
                e.preventDefault();
                navigator.share(shareData);
            });
        }

        // Download
        blockshare.insertAdjacentHTML('beforeend', '<a target="_blank" href="'+href+'" download>'+downloadIcon+'</a>');

        // Copy link
        blockshare.insertAdjacentHTML('beforeend', '<div class="vbox-tooltip"><div class="vbox-link-btn vbox-share-copy"><span class="vbox-tooltip-text" id="myTooltip"></span>'+linkIcon+'</div ></div>');
        const shareCopyBtn = blockshare.querySelector('.vbox-share-copy');
        shareCopyBtn.addEventListener('click', function(e){
            e.preventDefault();
            let tooltip = document.getElementById("myTooltip");
            navigator.clipboard.writeText(href).then(function() {
                tooltip.innerHTML = '<div class="vbox-tooltip-inner">Copied</div>';
            }, function() {
                console.log('copy failed');
            });
        });
    }

    function dragListeners(){
        // activate swipe
        if (canDrag) {
            content.classList.add('vbox-grab');
            content.addEventListener("touchstart", dragStart, false);
            content.addEventListener("touchend", dragEnd, false);
            content.addEventListener("touchmove", drag, false);
            content.addEventListener("mousedown", dragStart, false);
            content.addEventListener("mouseup", dragEnd, false);
            content.addEventListener("mouseout", dragEnd, false);
            content.addEventListener("mousemove", drag, false);
        } else {
            content.classList.remove('vbox-grab');
            content.removeEventListener("touchstart", dragStart, false);
            content.removeEventListener("touchend", dragEnd, false);
            content.removeEventListener("touchmove", drag, false);
            content.removeEventListener("mousedown", dragStart, false);
            content.removeEventListener("mouseup", dragEnd, false);
            content.removeEventListener("mouseout", dragEnd, false);
            content.removeEventListener("mousemove", drag, false);
        }
    }

    /**
     * Check navigation
     * @param {object} el Current item
     */
    function checknav(el){

        if (!el) {
            return false;
        }

        thisgall = el.dataset.gall;
        numeratio = el.settings.numeration;
        infinigall = el.settings.infinigall;
        blockshare.innerHTML = '';

        let vbtype = el.dataset.vbtype;

        if (el.settings.share && vbtype !== 'iframe' && vbtype !== 'inline' && vbtype !== 'ajax' ) {
            setShareButtons(el.href);
        }

        items = document.querySelectorAll('.vbox-item[data-gall="' + thisgall + '"]');

        current_index = Array.prototype.indexOf.call(items, el);

        if (items.length < 2) {
            numeratio = false;
        }
        if (items.length < 3) {
            infinigall = false;
        }

        thenext = items[current_index + 1];
        theprev = items[current_index - 1];

        if (!thenext && infinigall) {
            thenext = items[0];
        }

        if (!theprev && infinigall) {
            theprev = items[items.length - 1];
        }

        // Update gallery numeration
        if (items.length >= 1) {
            gallIndex = current_index + 1;
            blocknum.innerHTML = gallIndex + ' / ' + items.length;
        } else {
            gallIndex = 1;
        }
        if (numeratio) {
            blocknum.classList.remove('vbox-hidden');
        } else {
            blocknum.classList.add('vbox-hidden');
        }

        // Update title
        if (title !== '') {
            blocktitle.classList.remove('vbox-hidden');
        } else {
            blocktitle.classList.add('vbox-hidden');
        }
        blocktitle.innerHTML = title;

        // update navigation arrows
        prevok = false;
        nextok = false;

        if (thenext || infinigall) {
            nextok = true;
        }

        if (current_index > 0 || infinigall) {
            prevok = true;
        }

        canDrag = (prevok || nextok) && el.settings.navTouch;

        let vbox_next = overlay.querySelector('.vbox-next');
        let vbox_prev = overlay.querySelector('.vbox-prev');

        if (prevok) {
            vbox_prev.classList.remove('vbox-hidden');
        } else {
            vbox_prev.classList.add('vbox-hidden');
        }

        if (nextok) {
            vbox_next.classList.remove('vbox-hidden');
        } else {
            vbox_next.classList.add('vbox-hidden');
        }

        if (!el.settings.navigation) {
            vbox_next.classList.add('vbox-hidden');
            vbox_prev.classList.add('vbox-hidden');
        }
    } // Checknav

    /**
     * Update overlay and tools style.
     */
    function updateOverlay(destination){

        if (!destination) {
            return false;
        }

        backdrop.style.backgroundColor = set_overlayColor;

        // Custom preloader color.
        elPreloaderInner.innerHTML = createspinner(spinners[destination.settings.spinner]);

        overlay.style.setProperty('--sk-color', destination.settings.spinColor);

        elPreloader.classList.remove('vbox-hidden');

        blockshare.classList.remove('vbox-top', 'vbox-bottom');
        blocktitle.classList.remove('vbox-top', 'vbox-bottom');

        if (destination.settings.titlePosition == 'top') {
            blocktitle.classList.add('vbox-top');
            blockshare.classList.add('vbox-bottom');
        } else {
            blocktitle.classList.add('vbox-bottom');
            blockshare.classList.add('vbox-top');
        }

        let titleWidth = destination.settings.titleStyle === 'bar' ? '100%' : 'auto';
        let titleRadius = destination.settings.titleStyle === 'pill' ? '5em' : '0';
        let shareWidth = destination.settings.shareStyle === 'bar' ? '100%' : 'auto';
        let shareRadius = destination.settings.shareStyle === 'pill' ? '5em' : '0';
        let titlebg = destination.settings.titleStyle === 'transparent' ? 'transparent' : destination.settings.toolsBackground;
        let sharebg = destination.settings.shareStyle === 'transparent' ? 'transparent' : destination.settings.toolsBackground;

        overlay.style.setProperty('--vbox-title-width', titleWidth);
        overlay.style.setProperty('--vbox-title-radius', titleRadius);
        overlay.style.setProperty('--vbox-share-width', shareWidth);
        overlay.style.setProperty('--vbox-share-radius', shareRadius);
        overlay.style.setProperty('--vbox-tools-color', destination.settings.toolsColor);
        overlay.style.setProperty('--vbox-title-background', titlebg);
        overlay.style.setProperty('--vbox-share-background', sharebg);
    }

    /**
     * Load content
     */
    function loadContent(){
        if (!current_item) {
            return false;
        }
        let vbtype = current_item.dataset.vbtype;
        switch (vbtype) {
            case 'iframe':
                loadIframe(set_href, set_ratio);
                break;
            case 'inline':
                loadInline(set_href);
                break;
            case 'ajax':
                loadAjax(set_href);
                break;
            case 'video':
                loadVid(set_href, set_ratio, set_autoplay);
                break;
            default:
                loadImage(set_href);
        }
    }

    /**
     * Gallery navigation.
     */
    function navigateGall(destination) {

        if (!destination || navigationDisabled || !document.body.classList.contains('vbox-open')) {
            return false;
        }

        updateVars(destination);
        updateOverlay(destination);

        // swipe out item
        const speed = (current_item.settings.navSpeed * 0.84);
        content.style.transition = 'margin '+ speed + 'ms ease-out, opacity '+ speed + 'ms ease-out';

        if (destination === theprev) {
            content.classList.add("swipe-right");
        }
        if (destination === thenext) {
            content.classList.add("swipe-left");
        }

        elPreloader.classList.remove('vbox-hidden');
        const startopacity = content.style.opacity;
        content.classList.add("vbox-animated", "vbox-loading");

        clonecontent = content.cloneNode(false);
        clonecontent.classList.add('cloned');
        clonecontent.classList.remove("swipe-left", "swipe-right");
        clonecontent.style.opacity = 0;
        clonecontent.style.marginLeft = '0';
        clonecontent.style.marginRight = '0';

        const oldcontent = content;
        container.append(clonecontent);
        content = clonecontent;
        content.classList.remove('cloned');

        checknav(destination);

        animate({
            duration: current_item.settings.navSpeed,
            timing: timingLinear,
            draw: function(progress) {

                oldcontent.style.opacity = startopacity - progress/startopacity;

                if (progress === 1){
                    oldcontent.remove();
                    content.classList.remove("vbox-animated");
                    checkState('loading');
                    navigationDisabled = false;

                    if (current_item.settings.onNavComplete && typeof current_item.settings.onNavComplete === 'function') {
                        current_item.settings.onNavComplete(current_item, gallIndex, thenext, theprev);
                    }
                }
            }
        });
        loadContent();
    }

    /**
     * Open item.
     */
    function open(obj) {

        if (document.body.classList.contains('vbox-open') || !obj) {
            return false;
        }

        if (obj.settings.onPreOpen && typeof obj.settings.onPreOpen === 'function') {
            if (obj.settings.onPreOpen(obj) === false) {
                return false;
            }
        }

        updateVars(obj);

        document.body.insertAdjacentHTML('beforeend', core);
        document.body.classList.add('vbox-open');

        overlay = document.querySelector(".vbox-overlay");
        backdrop = overlay.querySelector(".vbox-backdrop");
        container = overlay.querySelector(".vbox-container");
        content = container.querySelector(".vbox-content");
        blocknum = overlay.querySelector(".vbox-num");
        blockshare = overlay.querySelector(".vbox-share");
        blocktitle = overlay.querySelector(".vbox-title");
        elPreloader = overlay.querySelector(".vbox-preloader");
        elPreloaderInner = elPreloader.querySelector(".vbox-preloader-inner");

        overlay.style.opacity = 0;

        updateOverlay(obj);
        checknav(obj);

        content.classList.add("vbox-animated", "vbox-loading");

        // fade in overlay
        animate({
            duration: 200,
            timing: timingLinear,
            draw: function(progress) {
                overlay.style.opacity = progress;
                if (progress === 1){
                    content.classList.remove('vbox-animated');
                    navigationDisabled = false;
                    checkState('loading');
                    if (current_item.settings.onPostOpen && typeof current_item.settings.onPostOpen === 'function') {
                        current_item.settings.onPostOpen(current_item, gallIndex, thenext, theprev);
                    }
                }
            }
        });

        loadContent();

        // Keyboard actions
        if (obj.settings.navKeyboard) {
            document.body.addEventListener('keydown', keyboardHandler);

            // Reset the throttle timer
            document.body.addEventListener('keyup', () => {
                if (throttle) {
                    clearTimeout(throttle);
                    throttle = null;
                }
            });
        }

        // Prev gallery
        document.querySelector('.vbox-prev').addEventListener('click', function(){
            navigateGall(theprev);
        });

        // Newxt gallery
        document.querySelector('.vbox-next').addEventListener('click', function(){
            navigateGall(thenext);
        });

        // Close modal.
        overlay.addEventListener('click', function(e){
            let closeBtn = document.querySelector('.vbox-close');
            if (closeBtn) {
                if (closeBtn.contains(e.target) || closeBtn === e.target || (current_item.settings.overlayClose &&
                    (e.target.classList.contains('vbox-overlay') ||
                        e.target.classList.contains('vbox-content') ||
                        e.target.classList.contains('vbox-backdrop') ||
                        e.target.classList.contains('vbox-close') ||
                        e.target.classList.contains('vbox-preloader') ||
                        e.target.classList.contains('vbox-container'))
                )) {
                    close();
                }
            }
        });
    }

    /**
     * Initialize Plugin
     */
    function init(venobox, settings) {

        if (settings.onInit && typeof settings.onInit === 'function') {
            settings.onInit(venobox);
        }

        let selectors = settings.jQuerySelectors || document.querySelectorAll(settings.selector);
        let navigation = '<a class="vbox-next"><span>Next</span></a><a class="vbox-prev"><span>Prev</span></a>';
        let vbheader = '<div class="vbox-title"></div><div class="vbox-left-corner"><div class="vbox-num">0/0</div></div><div class="vbox-close"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="vbox-close-icon" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M13.854 2.146a.5.5 0 0 1 0 .708l-11 11a.5.5 0 0 1-.708-.708l11-11a.5.5 0 0 1 .708 0Z"/><path fill-rule="evenodd" d="M2.146 2.146a.5.5 0 0 0 0 .708l11 11a.5.5 0 0 0 .708-.708l-11-11a.5.5 0 0 0-.708 0Z"/></svg></div>';
        let vbfooter = '<div class="vbox-share"></div>';
        let preloader = '<div class="vbox-preloader"><div class="vbox-preloader-inner"></div></div>';
        core = '<div class="vbox-overlay"><div class="vbox-backdrop"></div>' + preloader + '<div class="vbox-container"><div class="vbox-content"></div></div>' + vbheader + navigation + vbfooter + '</div>';

        // DOM manipulation only initialized on constructor, so this is SSR framework safe (ex. SvelteKit)
        imagesHolder = imagesHolder || document.createElement('div');
        imgLoader = imgLoader || new Image();

        /**
         *  Loop items.
         */
        forEach(selectors, function(obj){
            if (obj instanceof Element) {
                if (obj.classList.contains("vbox-item")) {
                    return true;
                }
                obj.settings = settings;
                obj.classList.add("vbox-item");

                // Open Link
                obj.addEventListener("click", function(e){
                    e.preventDefault();
                    // Remove focus from link to avoid multiple calls with enter key
                    obj.blur();
                    open(obj);
                    return false;
                }); // Click;
            }
        }); // forEach

        if (settings.popup) {
            let popup = document.querySelector(settings.popup);
            popup.settings = settings;
            open(popup);
        }
    } // init

    /**
     * VenoBox constructor
     */
    const VenoBox = function (options) {

        const venobox = {};

        // Merge user options with defaults
        let settings = extend( defaults, options || {} );

        venobox.close = close;
        venobox.next = next;
        venobox.prev = prev;
        venobox.open = open;
        venobox.settings = settings;

        init(venobox, settings);

        // Public APIs
        return venobox;
    };

    /* jQuery bridge for $().venobox() */
    if (typeof jQuery === 'function') {
        (function($){
            $.fn.extend({
                // plugin name - venobox
                venobox: function(options) {
                    const pluginoptions = options || {};
                    pluginoptions.jQuerySelectors = this;
                    // Init venobx
                    new VenoBox(pluginoptions);
                } // venobox
            }); // extend
        })(jQuery);
    }

    // See https://www.npmjs.com/package/venobox documentation.

    return VenoBox;

})));
function initVenoBox(){
    let venobox = new VenoBox({
        selector: '.venobox',
        spinner: 'rotating-plane',
        overlayColor: 'rgba(255, 255, 255, 0.8)',
        bgcolor: 'none',
        toolsColor: '#002664',
        toolsBackground: 'rgba(255, 255, 255, 0.8)',
        transitionSpeed: 400,
    });
}
initVenoBox();



   $(document).on('click', '.vimeo-video-btn', function () {
        var video_container = $(this).parents('.video-module-wrapper');
        if (video_container.hasClass('active')) {
            //console.log('active');
            video_container.find('.vimeo-post-img').show();
            //$(this).hide();
            video_container.removeClass('active');
            //video_container.find('.vimeo-iframe').hide();
            if ($(this).attr('type') != 'mp4-video') {
                var iframe = video_container.find('iframe');
                const player = new Vimeo.Player(iframe);
                player.pause();
            }
            return false;
        } else {
            //console.log('---active');
            video_container.find('.vimeo-post-img').hide();
            //$(this).hide();
            video_container.addClass('active');
            video_container.find('.vimeo-iframe').show();
            if ($(this).attr('type') != 'mp4-video') {
                var iframe = video_container.find('iframe');
                const player = new Vimeo.Player(iframe);
                player.play();
            }
            return false;
        }
    });


});