# Image Upload Guide for Shivam Construction Company Website

## How to Upload Images

### Step 1: Access Admin Panel
1. Go to: http://127.0.0.1:8000/admin/
2. Login with your superuser credentials

### Step 2: Upload Company Logo and Hero Image
1. Go to **Company Information** section
2. Click on the company entry (or create one if it doesn't exist)
3. Upload images in these fields:
   - **Logo**: Company logo (will appear in navigation)
   - **Hero Image**: Background image for home page hero section
4. Click **Save**

### Step 3: Upload Gallery Images
1. Go to **Company Images** section
2. Click **Add Company Image**
3. Fill in the details:
   - **Title**: Name of the image
   - **Image**: Upload the image file
   - **Image Type**: Select the category:
     - **Introduction Images**: For home page introduction section
     - **Vision Images**: For about page vision section
     - **Quality Policy Images**: For about page quality section
     - **Service Images**: For services page
     - **Equipment Images**: For equipment page
     - **Project Images**: For projects page
     - **Team Images**: For team page
     - **General Images**: For any other use
   - **Description**: Optional description
   - **Order**: Number to control display order (lower numbers appear first)
4. Click **Save**

### Step 4: Upload Project Images
1. Go to **Completed Projects** section
2. Click on a project or create a new one
3. Upload image in the **Image** field
4. Click **Save**

### Step 5: Upload Equipment Images
1. Go to **Equipment** section
2. Click on an equipment item or create a new one
3. Upload image in the **Image** field
4. Click **Save**

## Image Requirements

### Recommended Sizes:
- **Logo**: 200x200px or similar square ratio
- **Hero Image**: 1920x1080px (16:9 ratio)
- **Introduction Images**: 800x600px (4:3 ratio)
- **Equipment Images**: 600x400px (3:2 ratio)
- **Project Images**: 1200x800px (3:2 ratio)

### File Formats:
- JPG/JPEG (recommended for photos)
- PNG (recommended for logos and graphics)
- WebP (modern format, smaller file size)

### File Size:
- Keep images under 2MB for faster loading
- Compress images before uploading if they're too large

## Image Organization Tips

1. **Introduction Images**: Upload 3 images for the home page introduction section
2. **Vision Images**: Upload 1-2 images for the vision section
3. **Quality Images**: Upload 1-2 images for the quality policy section
4. **Equipment Images**: Upload one image per equipment item
5. **Project Images**: Upload one image per completed project

## Troubleshooting

### Images Not Showing:
1. Check that the image file was uploaded successfully
2. Verify the image path in the admin panel
3. Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.py
4. Check file permissions on the media directory

### Images Too Large:
- Use image compression tools before uploading
- Recommended tools: TinyPNG, ImageOptim, or online compressors

### Images Not Responsive:
- The CSS automatically makes images responsive
- If issues persist, check image dimensions and aspect ratios

## Quick Start

To quickly add images from your company materials:

1. **Company Logo**: Upload your SCC logo
2. **Hero Image**: Upload a construction site image for the home page
3. **Introduction Images**: Upload 3 construction equipment images
4. **Vision Image**: Upload the vision page image
5. **Quality Images**: Upload 2 quality policy images
6. **Equipment Images**: Upload images for each equipment item
7. **Project Images**: Upload images for completed projects

All images will automatically display on the website once uploaded!

