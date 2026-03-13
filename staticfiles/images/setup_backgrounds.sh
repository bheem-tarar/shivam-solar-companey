#!/bin/bash
# Script to set up background images for pages
# This will create symbolic links or copy existing images to match the required names

cd "$(dirname "$0")"

# Check if images exist and create links/copies
# Services background - construction sites, loaders
if [ -f "yellow-excavator-machine-loading-soil-into-a-dump-truck-at-construction-site-PF3FCH.jpg" ] && [ ! -f "services-bg.jpg" ]; then
    cp "yellow-excavator-machine-loading-soil-into-a-dump-truck-at-construction-site-PF3FCH.jpg" "services-bg.jpg"
    echo "Created services-bg.jpg"
fi

# Projects background - completed roads
if [ -f "240_F_632481162_bbPsH5A8Ba3LFfO3MBQW6RXlnmVD7g8s.jpg" ] && [ ! -f "projects-bg.jpg" ]; then
    cp "240_F_632481162_bbPsH5A8Ba3LFfO3MBQW6RXlnmVD7g8s.jpg" "projects-bg.jpg"
    echo "Created projects-bg.jpg"
fi

# Equipment background - machinery
if [ -f "240_F_596352826_wHODNKtqL62783yKwHBYCBq1rfoON6q5.jpg" ] && [ ! -f "equipment-bg.jpg" ]; then
    cp "240_F_596352826_wHODNKtqL62783yKwHBYCBq1rfoON6q5.jpg" "equipment-bg.jpg"
    echo "Created equipment-bg.jpg"
fi

# Vision background
if [ -f "240_F_1690730377_HhztuZ4UGrOKrSA3EkjpTj0EF4SCDU1g.jpg" ] && [ ! -f "vision-bg.jpg" ]; then
    cp "240_F_1690730377_HhztuZ4UGrOKrSA3EkjpTj0EF4SCDU1g.jpg" "vision-bg.jpg"
    echo "Created vision-bg.jpg"
fi

# Quality background
if [ -f "download.jpeg" ] && [ ! -f "quality-bg.jpg" ]; then
    cp "download.jpeg" "quality-bg.jpg"
    echo "Created quality-bg.jpg"
fi

# Team background - use any available image
if [ ! -f "team-bg.jpg" ]; then
    if [ -f "240_F_1690730377_HhztuZ4UGrOKrSA3EkjpTj0EF4SCDU1g.jpg" ]; then
        cp "240_F_1690730377_HhztuZ4UGrOKrSA3EkjpTj0EF4SCDU1g.jpg" "team-bg.jpg"
        echo "Created team-bg.jpg"
    fi
fi

# Contact background
if [ ! -f "contact-bg.jpg" ]; then
    if [ -f "yellow-excavator-machine-loading-soil-into-a-dump-truck-at-construction-site-PF3FCH.jpg" ]; then
        cp "yellow-excavator-machine-loading-soil-into-a-dump-truck-at-construction-site-PF3FCH.jpg" "contact-bg.jpg"
        echo "Created contact-bg.jpg"
    fi
fi

echo "Background images setup complete!"
echo "If you want to use different images, replace the files:"
echo "  - services-bg.jpg (for Services page)"
echo "  - projects-bg.jpg (for Projects page)"
echo "  - equipment-bg.jpg (for Equipment page)"
echo "  - vision-bg.jpg (for Vision section)"
echo "  - quality-bg.jpg (for Quality section)"
echo "  - team-bg.jpg (for Team page)"
echo "  - contact-bg.jpg (for Contact page)"

