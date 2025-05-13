var qsRegex;
var searchResultFlag;
$(window).on('load', function () {

    // init Isotope
    let $container = $('.hero-news__events').isotope({
        itemSelector: '.event-item',
        layoutMode: 'fitRows',

    });


    // bind filter button click
    $('.event-category-filter').on('click', 'a', function () {
        $('.event-category-filter a').removeClass('is-active');
        $(this).addClass('is-active');
        var filterValue = $(this).attr('data-filter');
        // use filterFn if matches value
        $container.isotope({
            filter: filterValue
        });
    });

    $container.on( 'arrangeComplete', function( event, filteredItems ) {
        if(filteredItems.length == 0){
            $('.no-result-found').show();
            $('.load-more-event').hide();
        }else{
            $('.no-result-found').hide();
        };
    });

    //****************************
    // Isotope Load more button
    //****************************
    var loadItem = $(".load-more-event").attr('data-load');
    var initShow = 5;
    if (loadItem) {
        initShow = loadItem;
    }
    //number of items loaded on init & onclick load more button
    var counter = initShow; //counter for load more button
    var iso = $container.data('isotope'); // get Isotope instance

    loadMoreEvent(initShow); //execute function onload

    function loadMoreEvent(toShow) {
        $container.find(".hidden").removeClass("hidden");

        var hiddenElems = iso.filteredItems.slice(toShow, iso.filteredItems.length).map(function (item) {
            return item.element;
        });
        $(hiddenElems).addClass('hidden');
        $container.isotope('layout');

        //when no more to load, hide show more button
        if (hiddenElems.length == 0) {
            $(".load-more-event").hide();
        } else {
            $(".load-more-event").show();
        };

    }


    //when load more button clicked
    $(".load-more-event").click(function () {
        if ($('.event-category-filter').data('clicked')) {
            //when filter button clicked, set initial value for counter
            counter = initShow;
            $('.event-category-filter').data('clicked', false);
        } else {
            counter = counter;
        };

        counter = counter + initShow;

        loadMoreEvent(counter);
    });

    //when filter button clicked
    $(".event-category-filter").click(function () {
        $(this).data('clicked', true);

        loadMoreEvent(initShow);
    });

    let $quicksearch = $('.quicksearch').keyup(debounce(function () {
        $container.find(".hidden").removeClass("hidden");
        if($quicksearch.val().length == 0){
            $(".load-more-event").show();
        }else{
            $(".load-more-event").hide();
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