import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import os

def create_volcano_background(width=1920, height=1080, filename='volcano_bg.png'):
    """Create a volcano-themed background image"""
    
    # Create a base image with gradient (sky to dark)
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()
    
    # Create gradient from sky blue to darker
    for y in range(height):
        # Sky gradient
        r = int(135 + (y / height) * 50)  # 135-185
        g = int(206 + (y / height) * 20)  # 206-226
        b = int(235 - (y / height) * 50)  # 235-185
        
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    # Draw volcanic mountain shape using PIL
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Mountain polygon (triangle-ish shape)
    mountain_points = [
        (100, height),
        (width // 2, height // 3),
        (width - 100, height)
    ]
    draw.polygon(mountain_points, fill=(100, 80, 60, 200), outline=(60, 40, 20, 255))
    
    # Add lava flows (orange/red)
    lava_points = [
        (width // 2 - 20, height // 3),
        (width // 2 - 80, height // 2),
        (width // 2 - 40, height)
    ]
    draw.polygon(lava_points, fill=(255, 100, 0, 150), outline=(255, 50, 0, 200))
    
    lava_points2 = [
        (width // 2 + 20, height // 3),
        (width // 2 + 80, height // 2),
        (width // 2 + 40, height)
    ]
    draw.polygon(lava_points2, fill=(255, 120, 20, 150), outline=(255, 70, 10, 200))
    
    # Add smoke (white circles)
    for i in range(5):
        x = width // 2 + np.random.randint(-50, 50)
        y = height // 3 - 100 + i * 30
        radius = 40 + i * 10
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], 
                    fill=(200, 200, 200, 100), outline=(180, 180, 180, 150))
    
    # Apply slight blur
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Save the image
    img.save(filename)
    print(f"✅ Volcano background created: {filename}")
    return filename

if __name__ == "__main__":
    create_volcano_background()
