import re
import os

# New footer HTML
new_footer = '''    <div class="btSiteFooter">
        <div class="bt_bb_wrapper" data-templates-time="">
            <!-- Footer Section 1 -->
            <section id="bt_bb_section69a67746888a9"
                class="bt_bb_section bt_bb_color_scheme_1 bt_bb_layout_boxed_1200 bt_bb_vertical_align_top bt_bb_top_spacing_medium bt_bb_bottom_spacing_none"
                style="--section-primary-color:#ffffff; --section-secondary-color:#191919; background-color: #000000 !important;">
                <div class="bt_bb_port">
                    <div class="bt_bb_cell">
                        <div class="bt_bb_cell_inner">
                            <div class="bt_bb_row bt_bb_column_gap_10"
                                style="--column-gap:10px;">
                                <div class="bt_bb_row_holder">
                                    <!-- About Us Column -->
                                    <div class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_subheadline_text_transform_default bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_subheadline bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">About Us</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>Expert Accountants</b></span></span></h5>
                                                <div class="bt_bb_headline_subheadline">With over 40 years of collective
                                                    experience in providing professional services to businesses, and
                                                    individuals, Expert Accountants are an independent firm based in London.
                                                </div>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_small"></div>
                                            <div class="bt_bb_icon bt_bb_color_scheme_8 bt_bb_style_filled bt_bb_size_small bt_bb_shape_circle bt_bb_align_inherit"
                                                style="min-width:3.5em; min-height:3.5em; --icon-primary-color:#222222; --icon-secondary-color:#ffffff;"><a href="#" target="_blank"
                                                    data-ico-fontawesome="&#xf09a;" class="bt_bb_icon_holder"></a></div>
                                            <div class="bt_bb_icon bt_bb_color_scheme_8 bt_bb_style_filled bt_bb_size_small bt_bb_shape_circle bt_bb_align_inherit"
                                                style="min-width:3.5em; min-height:3.5em; --icon-primary-color:#222222; --icon-secondary-color:#ffffff;"><a href="#" target="_blank"
                                                    data-ico-fontawesome="&#xf099;" class="bt_bb_icon_holder"></a></div>
                                            <div class="bt_bb_icon bt_bb_color_scheme_8 bt_bb_style_filled bt_bb_size_small bt_bb_shape_circle bt_bb_align_inherit"
                                                style="min-width:3.5em; min-height:3.5em; --icon-primary-color:#222222; --icon-secondary-color:#ffffff;"><a href="#" target="_blank"
                                                    data-ico-fontawesome="&#xf0e1;" class="bt_bb_icon_holder"></a></div>
                                            <div class="bt_bb_separator bt_bb_border_style_none"></div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_medium"></div>
                                        </div>
                                    </div>
                                    <!-- Quick Links Column -->
                                    <div class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">Quick Links</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>Main Pages</b></span></span></h5>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_small"></div>
                                            <div class="bt_bb_text">
                                                <ul style="list-style:none; padding-left:0; line-height:2.2em;">
                                                    <li><a href="index.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Home</a></li>
                                                    <li><a href="about.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">About</a></li>
                                                    <li><a href="blog.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Blog</a></li>
                                                    <li><a href="getquote.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Get Quote</a></li>
                                                    <li><a href="contact.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Contact</a></li>
                                                    <li><a href="article.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Article</a></li>
                                                </ul>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_medium"></div>
                                        </div>
                                    </div>
                                    <!-- Services Column -->
                                    <div class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">Services</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>What We Offer</b></span></span></h5>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_small"></div>
                                            <div class="bt_bb_text">
                                                <ul style="list-style:none; padding-left:0; line-height:2.2em;">
                                                    <li><a href="annual-accounts.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Annual Accounts</a></li>
                                                    <li><a href="book-keeping.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Book Keeping</a></li>
                                                    <li><a href="business-consultancy.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Business Consultancy</a></li>
                                                    <li><a href="management-accounts.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Management Accounts</a></li>
                                                    <li><a href="online-accounting.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Online Accounting</a></li>
                                                    <li><a href="payroll-services.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Payroll Services</a></li>
                                                    <li><a href="personal-tax.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Personal Tax</a></li>
                                                    <li><a href="tax-services.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Tax Services</a></li>
                                                </ul>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_medium"></div>
                                        </div>
                                    </div>
                                    <!-- Sectors Column -->
                                    <div class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">Sectors</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>Industries We Serve</b></span></span></h5>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_small"></div>
                                            <div class="bt_bb_text">
                                                <ul style="list-style:none; padding-left:0; line-height:2.2em;">
                                                    <li><a href="care-homes.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Care Homes</a></li>
                                                    <li><a href="clinics-surgeries.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Clinics & Surgeries</a></li>
                                                    <li><a href="construction.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Construction</a></li>
                                                    <li><a href="hospitality-leisure.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Hospitality & Leisure</a></li>
                                                    <li><a href="Landlords.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Landlords</a></li>
                                                    <li><a href="Manufacturing.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Manufacturing</a></li>
                                                    <li><a href="retails.html" style="color:#ffffff; text-decoration:none; padding:8px 0; display:block;">Retails</a></li>
                                                </ul>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_medium"></div>
                                        </div>
                                    </div>
                                    <!-- Ilford Office Column -->
                                    <div class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_subheadline_text_transform_default bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_subheadline bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">Contact</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>Ilford
                                                                Office</b></span></span></h5>
                                                <div class="bt_bb_headline_subheadline">Taking seamless key performance
                                                    indicators offline to maximise the long tail.</div>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome5solid="&#xf3c5;"
                                                    class="bt_bb_icon_holder"><span>698 Becontree Avenue, Dagenham, RM8
                                                        3HD</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome="&#xf095;"
                                                    class="bt_bb_icon_holder"><span>07939802086 / 0208 058
                                                        7212</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome="&#xf0e0;"
                                                    class="bt_bb_icon_holder"><span>info@expertaccountant.local</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <a href="index.html" target="_self" title=""
                                                    data-ico-fontawesome="&#xf0ac;"
                                                    class="bt_bb_icon_holder"><span></span></a>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none"></div>
                                            <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_medium bt_bb_bottom_spacing_normal">
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Middlesex Office Column -->
                                    <div
                                        class="bt_bb_column col-xxl-2 col-xl-2 col-md-6 col-sm-12 col-xs-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="2">
                                        <div class="bt_bb_column_content">
                                            <header
                                                class="bt_bb_headline bt_bb_font_weight_900 bt_bb_subheadline_text_transform_default bt_bb_color_scheme_1 bt_bb_dash_top bt_bb_superheadline bt_bb_superheadline_outside bt_bb_subheadline bt_bb_size_extrasmall bt_bb_align_inherit"
                                                style="--primary-color:#ffffff; --secondary-color:#191919;">
                                                <div class="bt_bb_headline_superheadline_outside"><span
                                                        class="bt_bb_headline_superheadline">Contact</span></div>
                                                <h5 class="bt_bb_headline_tag"><span
                                                        class="bt_bb_headline_content"><span><b>Middlesex</b></span></span>
                                                </h5>
                                                <div class="bt_bb_headline_subheadline">Taking seamless key performance
                                                    indicators offline to maximise the long tail.</div>
                                            </header>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome5solid="&#xf3c5;"
                                                    class="bt_bb_icon_holder"><span>Expert Accountants, 83 Halsbury Road
                                                        East, Northolt, Middlesex, UB5 4PY</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome="&#xf095;"
                                                    class="bt_bb_icon_holder"><span>07484222122</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <span data-ico-fontawesome="&#xf0e0;"
                                                    class="bt_bb_icon_holder"><span>info@yourfirm.co.uk</span></span>
                                            </div>
                                            <div class="bt_bb_separator bt_bb_border_style_none bt_bb_bottom_spacing_extra_small"></div>
                                            <div
                                                class="bt_bb_icon bt_bb_color_scheme_4 bt_bb_style_borderless bt_bb_size_xsmall bt_bb_shape_circle bt_bb_align_inherit"
                                                style="--icon-primary-color:#c3a660; --icon-secondary-color:#ffffff;">
                                                <a href="index.html" target="_self" title=""
                                                    data-ico-fontawesome="&#xf0ac;"
                                                    class="bt_bb_icon_holder"><span></span></a>
                                            </div>
                                            <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_medium bt_bb_bottom_spacing_extra_small">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Mobile Navigation Menu (visible only on mobile) -->
                            <div class="bt_bb_row bt_bb_hidden_sm bt_bb_hidden_md bt_bb_hidden_lg bt_bb_hidden_xl" style="margin-top:30px;">
                                <div class="bt_bb_row_holder">
                                    <div class="bt_bb_column col-xxl-12 col-xl-12 bt_bb_vertical_align_top bt_bb_align_center bt_bb_padding_normal"
                                        data-width="12">
                                        <div class="bt_bb_column_content">
                                            <div class="bt_bb_text">
                                                <ul style="list-style:none; padding-left:0; text-align:center;">
                                                    <li style="margin:8px 0;"><a href="index.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">Home</a></li>
                                                    <li style="margin:8px 0;"><a href="about.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">About</a></li>
                                                    <li style="margin:8px 0;"><a href="blog.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">Blog</a></li>
                                                    <li style="margin:8px 0;"><a href="getquote.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">Get Quote</a></li>
                                                    <li style="margin:8px 0;"><a href="contact.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">Contact</a></li>
                                                    <li style="margin:8px 0;"><a href="article.html" style="color:#ffffff; text-decoration:none; padding:12px 8px; display:inline-block; min-height:44px; line-height:44px;">Article</a></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><!-- cell_inner -->
                    </div><!-- cell -->
                </div><!-- port -->
            </section>
            <!-- Footer Section 2 - Copyright -->
            <section id="bt_bb_section69a677468936d"
                class="bt_bb_section bt_bb_color_scheme_2 bt_bb_layout_boxed_1200 bt_bb_vertical_align_top bt_bb_top_spacing_none bt_bb_bottom_spacing_none"
                style="--section-primary-color:#191919; --section-secondary-color:#ffffff; background-color:rgb(195,166,96);">
                <div class="bt_bb_port">
                    <div class="bt_bb_cell">
                        <div class="bt_bb_cell_inner">
                            <div class="bt_bb_row">
                                <div class="bt_bb_row_holder">
                                    <div class="bt_bb_column col-xxl-12 col-xl-12 bt_bb_vertical_align_top bt_bb_align_left bt_bb_padding_normal"
                                        data-width="12">
                                        <div class="bt_bb_column_content">
                                            <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_small bt_bb_bottom_spacing_none">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Desktop Copyright -->
                            <div class="bt_bb_row bt_bb_hidden_xs bt_bb_hidden_ms">
                                <div class="bt_bb_row_holder">
                                    <div
                                        class="bt_bb_column col-xxl-6 col-xl-6 bt_bb_vertical_align_middle bt_bb_align_left bt_bb_padding_normal"
                                        data-width="6">
                                        <div class="bt_bb_column_content">
                                            <div class="bt_bb_text">
                                                <p>Copyright by <strong>Expert Accountants</strong>. All rights reserved.
                                                    Developed By <a href="https://webbuilders.lk/">WEBbuilders.lk</a>
                                                </p>
                                            </div>
                                             <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_none">
                                            </div>
                                        </div>
                                    </div>
                                    <div
                                        class="bt_bb_column col-xxl-6 col-xl-6 bt_bb_vertical_align_middle bt_bb_align_right bt_bb_padding_normal"
                                        data-width="6">
                                        <div class="bt_bb_column_content">
                                            <div
                                                class="bt_bb_custom_menu btBottomFooterMenu bt_bb_direction_horizontal">
                                                <div class="menu-footer-menu-container">
                                                    <ul id="menu-footer-menu" class="menu">
                                                        <li
                                                            class="menu-item  menu-item-home current-menu-item ">
                                                            <a href="index.html" aria-current="page">Home</a>
                                                        </li>
                                                        <li
                                                            class="menu-item  ">
                                                            <a href="about.html">About us</a>
                                                        </li>
                                                        <li
                                                            class="menu-item  ">
                                                            <a href="contact.html">Contact</a>
                                                        </li>
                                                        <li
                                                            class="menu-item  ">
                                                            <a href="article.html">Article</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                            <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_none">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Mobile Copyright -->
                            <div class="bt_bb_row bt_bb_hidden_sm bt_bb_hidden_md bt_bb_hidden_lg">
                                <div class="bt_bb_row_holder">
                                    <div class="bt_bb_column col-xxl-12 col-xl-12 bt_bb_vertical_align_top bt_bb_align_center bt_bb_padding_normal"
                                        data-width="12">
                                        <div class="bt_bb_column_content">
                                            <div class="bt_bb_text">
                                                <p>Copyright by <strong>Expert Accountants</strong>. All rights reserved.
                                                    Developed By <a href="https://webbuilders.lk/">WEBbuilders.lk</a>
                                                </p>
                                            </div>
                                            <div
                                                class="bt_bb_separator bt_bb_border_style_none bt_bb_top_spacing_normal bt_bb_bottom_spacing_none">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><!-- cell_inner -->
                    </div><!-- cell -->
                </div><!-- port -->
            </section>
        </div>
    </div>'''

# List of files to update
files = [
    "about.html",
    "contact.html",
    "article.html",
    "blog.html",
    "getquote.html",
    "annual-accounts.html",
    "business-consultancy.html",
    "book-keeping.html",
    "management-accounts.html",
    "online-accounting.html",
    "payroll-services.html",
    "personal-tax.html",
    "tax-services.html",
    "construction.html",
    "clinics-surgeries.html",
    "care-homes.html",
    "hospitality-leisure.html",
    "Landlords.html",
    "Manufacturing.html",
    "retails.html"
]

success_count = 0
fail_count = 0

for file in files:
    if os.path.exists(file):
        try:
            print(f"Processing {file}...")
            
            # Read the file content
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use regex to find and replace the btSiteFooter section
            # Pattern matches from opening <div class="btSiteFooter"> to its closing comment
            pattern = r'<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->'
            
            # Check if pattern exists
            if re.search(pattern, content, re.DOTALL):
                # Replace the old footer with new footer (keeping the closing comment)
                new_content = re.sub(pattern, new_footer + '<!-- /btSiteFooter -->', content, flags=re.DOTALL)
                
                # Save the updated content back to the file
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  ✓ Successfully updated {file}")
                success_count += 1
            else:
                print(f"  ✗ Could not find btSiteFooter section in {file}")
                fail_count += 1
        except Exception as e:
            print(f"  ✗ Error processing {file}: {str(e)}")
            fail_count += 1
    else:
        print(f"  ✗ File not found: {file}")
        fail_count += 1

print("\n========================================")
print("Summary:")
print(f"  Successfully updated: {success_count} files")
print(f"  Failed: {fail_count} files")
print("========================================")
