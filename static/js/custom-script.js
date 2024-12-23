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

$(function() {
    $('.lazy').lazy();

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
});