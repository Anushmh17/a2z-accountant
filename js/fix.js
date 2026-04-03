/* Optimized fix.js to eliminate forced reflow and layout thrashing */
jQuery(document).ready(function ($) {
    console.log('fix.js is loading (optimized)...');

    function ensureMobileBackButton() {
        if ($('.btCustomMobileBack').length) return;
        $('body').append('<button type="button" class="btCustomMobileBack" aria-label="Close menu"><span></span></button>');
    }

    function openMobileMenu() {
        $('body').addClass('btMenuVerticalOn btShowMenu btMobileMenuOpen');
        $('.btBelowLogoArea').addClass('btMobileMenuOpen');
    }

    function closeMobileMenu() {
        $('body').removeClass('btMenuVerticalOn btShowMenu btMobileMenuOpen');
        $('.btBelowLogoArea').removeClass('btMobileMenuOpen');
    }

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
        requestAnimationFrame(function () {
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
            ensureMobileBackButton();
        });
    }

    // Initial Trigger
    applyMobileFixes();
    ensureMobileBackButton();

    // Trigger on full load (ensures images are calculated)
    $(window).on('load', function () {
        applyMobileFixes();
        ensureMobileBackButton();
    });

    // Trigger on resize
    $(window).on('resize', function () {
        requestAnimationFrame(applyMobileFixes);
    });

    // Toggle menu
    $(document).on('click', '.customMenuTrigger', function (e) {
        e.preventDefault();
        if ($('body').hasClass('btMobileMenuOpen')) {
            closeMobileMenu();
        } else {
            openMobileMenu();
        }
    });

    // Mobile back button to close the opened menu
    $(document).on('click', '.btCustomMobileBack', function (e) {
        if ($(window).width() > 991) return;

        e.preventDefault();
        closeMobileMenu();
    });

    // Mobile: allow tapping parent links to toggle sub-menus without closing
    $(document).on('click', '.btBelowLogoArea .menu-item-has-children > a', function (e) {
        if ($(window).width() > 991 || !$('body').hasClass('btMobileMenuOpen')) return;

        e.preventDefault();
        e.stopPropagation();

        var parentItem = $(this).parent();
        var subMenu = parentItem.children('.sub-menu').first();

        // Close siblings for a cleaner accordion feel
        parentItem.siblings('.menu-item-has-children').removeClass('on').children('.sub-menu').stop(true, true).slideUp(200);

        parentItem.toggleClass('on');
        subMenu.stop(true, true).slideToggle(200);
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
