var qsRegex;
var searchResultFlag;
var filters = {};
$(window).on('load', function () {
    var $grid = $('.grid').isotope({
        // options
    });
    // filter items on button click
    $('.filter-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
    });

    // init Isotope
    let $container = $('.hero-news__cards').isotope({
        itemSelector: '.element-item',
        layoutMode: 'fitRows',
    });

    // Also run on window resize to maintain responsiveness
    $(window).on('resize', function () {
        // Debounce for performance (optional)
        clearTimeout(window.resizeTimeout);
        window.resizeTimeout = setTimeout(equalizeNewsHeights, 100);
    });

    function equalizeNewsHeights() {
        let maxHeight = 0;
        const $items = $('.hero-news__cards .element-item .new-card');

        $items.css('min-height', 'auto'); // Reset first

        $items.each(function () {
            const itemHeight = $(this).outerHeight(); // Use outerHeight to include padding
            if (itemHeight > maxHeight) {
                maxHeight = itemHeight;
            }
        });

        $items.css('min-height',maxHeight);
    }

    // bind filter button click
    $('.news-category-filter').on('click', 'a', function () {
        var $this = $(this);
        var filterGroup = $(this).parents('.news-category-filter').attr('data-filter-group');
        $this.parents('.news-category-filter').find('a').removeClass('is-active');
        $(this).addClass('is-active');
        var filterValue = $(this).attr('data-filter');
        filters[filterGroup] = filterValue;
        //var filterString = Object.values(filters).map(filters => filters.join(',')).join('');
        var filterString = concatValues( filters );
        // use filterFn if matches value
        $container.isotope({ filter: filterString || '*' });
    });

    $container.on('arrangeComplete', function (event, filteredItems) {
        equalizeNewsHeights();
        if (filteredItems.length == 0) {
            $('.no-result-found').show();
            $('.load-more-news').hide();
        } else {
            $('.no-result-found').hide();
        };
    });

    //****************************
    // Isotope Load more button
    //****************************
    var loadItem = $(".load-more-news").attr('data-load');
    var initShow = 12;
    if (loadItem) {
        initShow = loadItem;
    }
    //number of items loaded on init & onclick load more button
    var counter = initShow; //counter for load more button
    var iso = $container.data('isotope'); // get Isotope instance

    loadMore(initShow); //execute function onload
    equalizeNewsHeights();

    function loadMore(toShow) {
        $container.find(".hidden").removeClass("hidden");

        var hiddenElems = iso.filteredItems.slice(toShow, iso.filteredItems.length).map(function (item) {
            return item.element;
        });
        $(hiddenElems).addClass('hidden');
        $container.isotope('layout');

        //when no more to load, hide show more button
        if (hiddenElems.length == 0) {
            $(".load-more-news").hide();
        } else {
            $(".load-more-news").show();
        };

    }


    //when load more button clicked
    $(".load-more-news").click(function () {
        if ($('.news-category-filter').data('clicked')) {
            //when filter button clicked, set initial value for counter
            counter = initShow;
            $('.news-category-filter').data('clicked', false);
        } else {
            counter = counter;
        };

        counter = counter + initShow;

        loadMore(counter);
    });

    //when filter button clicked
    $(".news-category-filter").click(function () {
        $(this).data('clicked', true);

        loadMore(initShow);
    });

    let $quicksearch = $('.quicksearch').keyup(debounce(function () {
        $container.find(".hidden").removeClass("hidden");
        if ($quicksearch.val().length == 0) {
            $(".load-more-news").show();
        } else {
            $(".load-more-news").hide();
        }
        qsRegex = new RegExp($quicksearch.val(), 'gi');
        $container.isotope({
            filter: function () {
                var $this = $(this);
                var searchResult = qsRegex ? $this.text().toLowerCase().includes($quicksearch.val().toLowerCase()) : true;
                return searchResult;
            }
        });
    }, 200));

});

function debounce(fn, threshold) {
    var timeout;
    return function debounced() {
        if (timeout) {
            clearTimeout(timeout);
        }
        function delayed() {
            fn();
            timeout = null;
        }
        setTimeout(delayed, threshold || 100);
    };
}

function concatValues( obj ) {
    var value = '';
    for ( var prop in obj ) {
      value += obj[ prop ];
    }
    return value;
  }