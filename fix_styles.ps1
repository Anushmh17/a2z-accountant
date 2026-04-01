$htmlFiles = Get-ChildItem -Path . -Filter *.html

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw

    # Remove the unwanted <style> blocks
    $oldContent = $content
    $content = $content -replace "(?s)<style id=['""]avantage-style-inline-css['""][^>]*>.*?</style>\s*", ""
    $content = $content -replace "(?s)<style data-id=['""]bt_bb_color_schemes['""][^>]*>.*?</style>\s*", ""
    $content = $content -replace "(?s)<style id=['""]global-styles-inline-css['""][^>]*>.*?</style>\s*", ""
    $content = $content -replace "(?s)<style id=['""]wp-block-library-inline-css['""][^>]*>.*?</style>\s*", ""
    $content = $content -replace "(?s)<style id=['""]classic-theme-styles-inline-css['""][^>]*>.*?</style>\s*", ""

    # Check and inject local-fonts.css
    if ($content -notmatch "local-fonts\.css") {
        $content = $content -replace "</head>", "`t<link rel=`"stylesheet`" href=`"css/local-fonts.css`">`r`n</head>"
    }

    # Check and inject fix.css
    if ($content -notmatch "fix\.css") {
        $content = $content -replace "</head>", "`t<link rel=`"stylesheet`" href=`"css/fix.css`">`r`n</head>"
    }

    if ($oldContent -ne $content) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Updated $($file.Name)"
    }
}
