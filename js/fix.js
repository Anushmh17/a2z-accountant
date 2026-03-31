/* Optimized fix.js to eliminate forced reflow and layout thrashing */
jQuery(document).ready(function ($) {
    console.log('🚀 fix.js is loading (optimized)...');

    // Hide header and footer if loaded inside an iframe (like on article.html)
    if (window.self !== window.top) {
        $('.mainHeader, .btSiteFooter, .btVerticalHeaderTop, .btVerticalMenuTrigger').attr('style', 'display: none !important');
        $('body').addClass('is-iframe');
    }

    // 1. MOBILE MENU RE-INIT (Simplified)
    function fixMobileMenu() {
        if (window.innerWidth >= 1200) return;
        $('.btHorizontalMenuTrigger, .btVerticalMenuTrigger').each(function () {
            if (!$(this).hasClass('customHandled')) {
                $(this).addClass('customMenuTrigger customHandled').removeClass('btHorizontalMenuTrigger btVerticalMenuTrigger');
            }
        });
    }

    // 2. MOBILE GAP FIX (Unified)
    function applyMobileFixes() {
        if ($(window).width() > 991) return;
        requestAnimationFrame(function() {
            // Neutralize layout shifts
            $('.btContentWrap, .btContentHolder, .btContent, .btPageWrap').css({
                'transform': 'none',
                'margin-top': '-70px',
                'padding-top': '0',
                'position': 'relative'
            });
            $('section.bt_bb_section').first().css({
                'margin-top': '0',
                'padding-top': '0'
            });
            fixMobileMenu();
        });
    }

    // Initial Trigger
    applyMobileFixes();

    // Trigger on full load (ensures images are calculated)
    $(window).on('load', applyMobileFixes);

    // Trigger on resize
    $(window).on('resize', function () {
        requestAnimationFrame(applyMobileFixes);
    });

    // Toggle menu
    $(document).on('click', '.customMenuTrigger', function(e) {
        e.preventDefault();
        $('body').toggleClass('btMenuVerticalOn btShowMenu btMobileMenuOpen');
        $('.btBelowLogoArea').toggleClass('btMobileMenuOpen');
    });

    // Component Initializers
    (function init() {
        if ($.fn.slick) {
            $('.slick-slider:not(.slick-initialized)').each(function () {
                var $this = $(this);
                var settings = $this.data('slick');
                if (settings) $this.slick(settings);
            });
        }
        $('.bt_bb_tabs_header li').on('click', function () {
            var index = $(this).index();
            $(this).addClass('on').siblings().removeClass('on');
            $(this).closest('.bt_bb_tabs').find('.bt_bb_tab_item').eq(index).addClass('on').siblings().removeClass('on');
        });
    })();
});
