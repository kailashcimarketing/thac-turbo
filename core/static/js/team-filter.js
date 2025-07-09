var qsRegex;
var searchResultFlag;
document.addEventListener('turbo:load', function () {

    // init Isotope
    let $container = $('.s-team__cards.leadership-team').isotope({
        itemSelector: '.s-team__card-col',
        layoutMode: 'fitRows',
    });


    // bind filter button click
    $('.team-category-filter').on('click', 'a', function () {
        $('.team-category-filter a').removeClass('is-active');
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
            $('.load-more-team').hide();
        }else{
            $('.no-result-found').hide();
        };
    });

    //****************************
    // Isotope Load more button
    //****************************
    var loadItem = $(".load-more-team").attr('data-load');
    var initShow = 10;
    if (loadItem) {
        initShow = loadItem;
    }
    //number of items loaded on init & onclick load more button
    var counter = initShow; //counter for load more button
    var iso = $container.data('isotope'); // get Isotope instance

    //loadMore(initShow); //execute function onload

    function loadMore(toShow) {
        $container.find(".hidden").removeClass("hidden");

        var hiddenElems = iso.filteredItems.slice(toShow, iso.filteredItems.length).map(function (item) {
            return item.element;
        });
        $(hiddenElems).addClass('hidden');
        $container.isotope('layout');

        //when no more to load, hide show more button
        if (hiddenElems.length == 0) {
            $(".load-more-team").hide();
        } else {
            $(".load-more-team").show();
        };

    }


    //when load more button clicked
    $(".load-more-team").click(function () {
        if ($('.team-category-filter').data('clicked')) {
            //when filter button clicked, set initial value for counter
            counter = initShow;
            $('.team-category-filter').data('clicked', false);
        } else {
            counter = counter;
        };

        counter = counter + initShow;

        loadMore(counter);
    });

    //when filter button clicked
    $(".team-category-filter").click(function () {
        $(this).data('clicked', true);

        loadMore(initShow);
    });

    let $quicksearch = $('.quicksearch').keyup(debounce(function () {
        $container.find(".hidden").removeClass("hidden");
        if($quicksearch.val().length == 0){
            $(".load-more-team").show();
        }else{
            $(".load-more-team").hide();
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