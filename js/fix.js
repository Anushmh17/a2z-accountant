console.log('🚀 fix.js is loading...');
// ===== GLOBAL FIXES =====
jQuery(document).ready(function ($) {
    console.log('🔧 Global fix ready function firing');

    // Hide header and footer if loaded inside an iframe (like on article.html)
    if (window.self !== window.top) {
        $('.mainHeader, .btSiteFooter, .btVerticalHeaderTop, .btVerticalMenuTrigger').attr('style', 'display: none !important');
        $('body').addClass('is-iframe');
    }

    // Fix 1: Reset any negative offsets
    function resetOffsets() {
        if ($(window).width() > 991) return; // Do not strip offsets on Desktop

        $('.btPageWrap, .btContentWrap, .btContentHolder, .btContent, .bt_bb_section').css({
            'transform': 'none',
            'margin-top': '0',
            'padding-top': '0',
            'position': 'relative',
            'top': '0'
        });
        // Specifically target the first section
        $('section.bt_bb_section').first().css({
            'margin-top': '0',
            'padding-top': '0',
            'transform': 'none'
        });
    }

    // Fix 2: Reliable single-trigger mobile menu with dedicated panel back button
    function fixMobileMenu() {
        console.log('📱 Initializing clean mobile menu');

        // *** DESKTOP GUARD: On desktop, let theme handle the menu natively ***
        // Only rename triggers and inject custom UI on mobile
        if (window.innerWidth >= 1200) {
            // On desktop: ensure the 'on' class is NOT stuck
            $('body').removeClass('btMenuVerticalOn btShowMenu btMobileMenuOpen btHideMenu');
            $('.btBelowLogoArea').removeClass('btMobileMenuOpen');
            $('.menuPort nav > ul > li').removeClass('on');
            // Make sure sub-menus are not inlined hidden
            $('.menuPort nav > ul > li > .sub-menu').css('display', '');

            // Prevent parent menu items with href="#" from getting stuck when clicked on desktop
            $('.menuPort nav > ul > li.menu-item-has-children > a').off('click.desktopfix').on('click.desktopfix', function (e) {
                if ($(this).attr('href') === '#' || !$(this).attr('href')) {
                    e.preventDefault();
                    $(this).closest('li').toggleClass('on');
                    return false;
                }
            });
            return;
        }

        // 1. NEUTRALIZE theme triggers to stop theme JS from interfering
        // We rename the classes so theme JS doesn't find them, but we keep styling if possible
        $('.btHorizontalMenuTrigger, .btVerticalMenuTrigger').each(function () {
            if (!$(this).hasClass('customHandled')) {
                $(this).addClass('customMenuTrigger customHandled').removeClass('btHorizontalMenuTrigger btVerticalMenuTrigger');
            }
        });

        // Inject sub-menu togglers for parent items (mobile only)
        $('.menu-item-has-children').each(function () {
            if (!$(this).find('> .subToggler').length) {
                $(this).append('<span class="subToggler" style="position:absolute; right:13px; top:0; height:44px; width:44px; cursor:pointer; z-index:10; display:flex; align-items:center; justify-content:center; border-radius:30px;"></span>');
            }
        });

        // 2. AGGRESSIVE NUKE for any "X" icons and theme close buttons
        function nukeThemeClose() {
            // Remove known close button classes
            $('.btCloseVertical, .btCloseHorizontal, .btCloseMenu, .btSearchInnerClose').remove();

            // Remove ANY element with data-ico-fa set to "X" (\uf00d)
            $('[data-ico-fa*="f00d"]').remove();
            $('[data-ico-fa*="&#xf00d;"]').remove();

            // Check for specific theme icon structures that might be re-injected
            $('.bt_bb_icon_holder').each(function () {
                var ico = $(this).attr('data-ico-fa') || '';
                if (ico.indexOf('f00d') !== -1) {
                    $(this).closest('.bt_bb_icon').remove();
                }
            });
        }

        nukeThemeClose();
        setInterval(nukeThemeClose, 500); // More frequent nuking

        // Inject dedicated BACK button into the menu panel if not exists
        if (!$('.btBelowLogoArea .btCustomMobileBack').length) {
            $('.btBelowLogoArea').prepend('<div class="btCustomMobileBack"><span></span></div>');
        }

        // --- Close/open helpers ---
        function closeMenu() {
            $('body').removeClass('btMenuVerticalOn btShowMenu btMobileMenuOpen btHideMenu');
            $('.btBelowLogoArea').removeClass('btMobileMenuOpen');
            // Ensure trigger is visible again
            $('.customMenuTrigger').show();
            console.log('✅ Menu CLOSED');
        }
        function openMenu() {
            $('body').addClass('btMenuVerticalOn btShowMenu btMobileMenuOpen');
            $('.btBelowLogoArea').addClass('btMobileMenuOpen');
            // Hide the original trigger so it doesn't show as 3 bars or X
            $('.customMenuTrigger').hide();
            console.log('✅ Menu OPENED');
            nukeThemeClose();
        }

        // Remove ALL previous jQuery handlers
        $(document).off('click.mobilefix click.closefix click.linkfix click.subfix click.customback click.triggerfix click.subfixtoggle');

        // Robust delegated handler for ALL triggers
        $(document).on('click.triggerfix', '.customMenuTrigger, .btHorizontalMenuTrigger, .btVerticalMenuTrigger', function (e) {
            if (window.innerWidth >= 1200) return;
            e.preventDefault();
            e.stopImmediatePropagation();
            openMenu();
            return false;
        });

        // Custom back button click
        $(document).on('click.customback', '.btCustomMobileBack', function (e) {
            e.preventDefault();
            e.stopImmediatePropagation();
            closeMenu();
            return false;
        });

        // Fallback for any theme close buttons that escape the nuke
        $(document).on('click.closefix', '.btCloseVertical, .btCloseHorizontal, .btCloseMenu', function (e) {
            e.preventDefault();
            e.stopImmediatePropagation();
            closeMenu();
            return false;
        });

        // Prevent parent menu items with href="#" from navigating, but still open submenus on mobile
        $(document).on('click.linkfix', '.mainHeader nav > ul > li.menu-item-has-children > a', function (e) {
            if (window.innerWidth > 991) return;
            var $a = $(this);
            var $li = $a.closest('li');
            if ($li.hasClass('menu-item-has-children') && ($a.attr('href') === '#' || !$a.attr('href'))) {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();
                $li.find('> .subToggler').trigger('click');
                return false;
            }
            closeMenu();
        });

        // Close menu on nav link click (for non-parent items or items with valid href)
        $(document).on('click.linkfix', '.mainHeader nav ul li:not(.menu-item-has-children) a, .mainHeader nav ul li.menu-item-has-children a[href!="#"][href]', function (e) {
            if ($(window).width() > 991) return;
            closeMenu();
        });

        // Submenu toggling (mobile only) - Delegated binding with tough propagation stopping
        $(document).on('click.subfixtoggle', '.subToggler', function (e) {
            if (window.innerWidth > 991) return; // Skip on desktop
            e.preventDefault();
            e.stopPropagation(); // VERY IMPORTANT: Stop event before it bubbles to parent LI where theme listens!
            e.stopImmediatePropagation();

            var $li = $(this).closest('li');
            var $ul = $li.find('> ul').first();

            if ($li.hasClass('on')) {
                $li.removeClass('on');
                $ul.stop(true, true).slideUp(200);
            } else {
                $li.addClass('on');
                $ul.stop(true, true).slideDown(200);
            }
            return false;
        });
    }
    // Run fixes
    resetOffsets();
    fixMobileMenu();
    $('body').removeClass('btMenuVerticalOn btShowMenu btMobileMenuOpen btHideMenu');
    $('.btBelowLogoArea').removeClass('btMobileMenuOpen');

    // Run again after a delay to catch any late-loading scripts
    setTimeout(resetOffsets, 500);
    setTimeout(fixMobileMenu, 500);
    setTimeout(resetOffsets, 1000);

    // Run on resize
    $(window).on('resize', function () {
        resetOffsets();
        fixMobileMenu();
    });
});

// ===== MOBILE GAP FIX - FORCES CONTENT TO TOP =====
jQuery(document).ready(function ($) {
    function fixMobileGap() {
        if ($(window).width() <= 991) {
            // Immunity for specific pages with custom hero layouts
            if (window.location.pathname.includes('blog.html') || window.location.pathname.includes('article.html')) return;

            var headerHeight = $('.mainHeader').outerHeight() || 0;
            var contentTop = $('.btContentWrap').offset().top || 0;
            console.log('Header height:', headerHeight, 'Content top:', contentTop);

            $('body').css('overflow-x', 'hidden');

            // Pull content up
            $('.btContentWrap').css({
                'margin-top': '-70px',
                'padding-top': '0',
                'position': 'relative',
                'z-index': '1'
            });
        }
    }

    fixMobileGap();
    setTimeout(fixMobileGap, 100);
    setTimeout(fixMobileGap, 300);
    setTimeout(fixMobileGap, 500);
    setTimeout(fixMobileGap, 1000);

    $(window).on('resize', function () {
        fixMobileGap();
    });

    $(window).on('load', function () {
        fixMobileGap();
    });
});

// Force slick slider refresh on mobile
jQuery(window).on('resize orientationchange', function () {
    if (jQuery(window).width() <= 991) {
        jQuery('.slick-slider').slick('resize');
    }
});

// ===== GLOBAL FIXES – RUN ON ALL PAGES =====
jQuery(document).ready(function ($) {
    console.log('🔧 Running complete fix script...');

    // ============================================
    // 1. RESET HEADER GAP (universal)
    // ============================================
    function resetOffsets() {
        if ($(window).width() > 991) return; // DON'T BREAK DESKTOP
        
        // Immunity for specific pages with custom hero layouts
        if (window.location.pathname.includes('blog.html') || window.location.pathname.includes('article.html')) return; 

        $('.btContentWrap, .btContentHolder, .btContent, .bt_bb_wrapper, .btPageWrap').css({
            'transform': 'none',
            'margin-top': '0',
            'padding-top': '0',
            'position': 'relative',
            'top': '0'
        });
        $('section.bt_bb_section').first().css({
            'margin-top': '0',
            'padding-top': '0'
        });
    }
    resetOffsets();
    $(window).on('resize', resetOffsets);

    // ============================================
    // 2. MOBILE SPECIFIC FIXES
    // ============================================
    function fixMobileLayout() {
        if ($(window).width() <= 991) {
            // Hide any floating elements
            $('.bt_bb_floating_element, .bt_bb_floating_image, .bt_bb_image[style*="position: absolute"]').hide();

            // Reset any negative margins on specific rows
            $('.bt_bb_row[style*="margin-top"]').css('margin-top', '2em');
            $('.bt_bb_row.bt_bb_row_width_boxed_991[style*="margin-top"]').css('margin-top', '0');

            // Force all columns to stack
            $('.bt_bb_column, .bt_bb_column_inner').css({
                'width': '100%',
                'max-width': '100%',
                'flex-basis': '100%',
                'padding-left': '20px',
                'padding-right': '20px'
            });

            // Fix slider height
            $('.bt_bb_content_slider, .slick-slider, .slick-list, .slick-track, .slick-slide').css('height', 'auto');

            // Refresh slick slider if present
            if ($('.slick-slider').hasClass('slick-initialized')) {
                $('.slick-slider').slick('setPosition');
            }
        } else {
            // Restore original styles for desktop (optional)
            $('.bt_bb_floating_element, .bt_bb_floating_image, .bt_bb_image[style*="position: absolute"]').show();
        }
    }

    // Run multiple times to catch late-loading content
    fixMobileLayout();
    setTimeout(fixMobileLayout, 300);
    setTimeout(fixMobileLayout, 600);
    $(window).on('resize orientationchange', function () {
        setTimeout(fixMobileLayout, 50);
    });

    // ============================================
    // 3. SLICK SLIDER RECALC ON MOBILE
    // ============================================
    $(window).on('load', function () {
        if ($(window).width() <= 991 && $('.slick-slider').length) {
            setTimeout(function () {
                $('.slick-slider').slick('setPosition');
            }, 200);
        }
    });

    // ============================================
    // 4. CONSULTANTS SECTION & COUNTER FIXES
    // ============================================
    function fixConsultantsSection() {
        var $section = $('.bt_bb_section.bt_bb_color_scheme_1').filter(function () {
            return $(this).css('background-color') === 'rgb(34, 34, 34)' ||
                $(this).css('background-color') === '#222222';
        });
        if ($section.length) {
            var $bgColumn = $section.find('.bt_bb_column.btLazyLoadBackground');
            if ($bgColumn.length) {
                var bgUrl = $bgColumn.data('background_image_src');
                if (bgUrl) {
                    $bgColumn.css({
                        'background-image': 'url(' + bgUrl + ')',
                        'background-size': 'cover',
                        'background-position': 'right center'
                    });
                }
            }
            var $counterRow = $section.find('.bt_bb_row.bt_bb_row_width_boxed_991');
            if ($counterRow.length) {
                $counterRow.css({
                    'margin-top': '-18em',
                    'margin-bottom': '5em',
                    'z-index': '2',
                    'position': 'relative',
                    'background-color': '#c3a660'
                });
            }
        }
    }

    function fixCounterColors() {
        $('.bt_bb_counter_holder').each(function () {
            var currentStyle = $(this).attr('style') || '';
            currentStyle = currentStyle.replace(/color:\s*#[0-9a-f]+;?/gi, '');
            $(this).attr('style', currentStyle + '; color: #c3a660 !important');
            $(this).find('*').css('color', '#c3a660');
            $(this).css('color', '#c3a660');
        });
    }

    // Run again
    setTimeout(fixConsultantsSection, 500);
    setTimeout(fixCounterColors, 500);
    $(window).on('load', function () {
        fixConsultantsSection();
        fixCounterColors();
    });
});

// ===== BLOG PAGE – HERO GAP FIX (mobile only, runs last) =====
jQuery(document).ready(function ($) {
    function fixBlogHeroGap() {
        // Desktop guard
        if ($(window).width() > 991) return;
        // Only run on the blog page
        if (window.location.pathname.indexOf('blog.html') === -1) return;

        var $mobileHeader = $('.btVerticalHeaderTop');
        var $headline = $('.btPageHeadline.bt_bb_section');
        if (!$headline.length) return;

        // Measure the actual gap between mobile header and hero section
        var headerBottom = $mobileHeader.length
            ? ($mobileHeader.offset().top + $mobileHeader.outerHeight(true))
            : 0;
        var headlineTop = $headline.offset().top;
        var gap = headlineTop - headerBottom;

        console.log('Blog hero gap:', gap + 'px');

        // Pull the entire content wrap up by the exact gap amount
        if (gap > 2) {
            var currentWrapMargin = parseInt($('.btContentWrap').css('margin-top')) || 0;
            $('.btContentWrap').css('margin-top', (currentWrapMargin - gap) + 'px');
            console.log('Blog: pulled content up by', gap + 'px');
        }
    }

    // Run AFTER all other fix.js functions have settled (they all run by 1000ms)
    setTimeout(fixBlogHeroGap, 1500);
    setTimeout(fixBlogHeroGap, 2000);

    $(window).on('load', function () {
        setTimeout(fixBlogHeroGap, 1500);
    });
    $(window).on('resize orientationchange', function () {
        if ($(window).width() <= 991) setTimeout(fixBlogHeroGap, 300);
    });
});
