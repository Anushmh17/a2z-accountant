#!/bin/bash

cd "C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z" || exit 1

# Read the new footer content
new_footer=$(<NEW_FOOTER_CONTENT.txt)

# Files to update
files=(
    "about.html" "contact.html" "article.html" "blog.html" "getquote.html"
    "annual-accounts.html" "business-consultancy.html" "book-keeping.html"
    "management-accounts.html" "online-accounting.html" "payroll-services.html"
    "personal-tax.html" "tax-services.html"
    "construction.html" "clinics-surgeries.html" "care-homes.html"
    "hospitality-leisure.html" "Landlords.html" "Manufacturing.html" "retails.html"
)

echo "Updating $(echo ${#files[@]}) HTML files with new footer..."
success=0
failed=0

for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ File not found: $file"
        ((failed++))
        continue
    fi
    
    # Create a temp file
    temp_file=$(mktemp)
    
    # Use awk to replace the footer
    awk -v new_footer="$new_footer" '
        /^        <div class="btSiteFooter">$/ {
            print $0
            print new_footer
            while (getline && !/^        <\/div><!-- \/btSiteFooter -->$/) {
                # Skip old footer
            }
            # Print closing tag
            next
        }
        { print }
    ' "$file" > "$temp_file"
    
    if mv "$temp_file" "$file"; then
        echo "✅ Updated: $file"
        ((success++))
    else
        echo "❌ Error updating: $file"
        rm -f "$temp_file"
        ((failed++))
    fi
done

echo ""
echo "=========================================="
echo "Results: $success updated, $failed failed"
