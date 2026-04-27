import os
import sys
from PIL import Image, ImageDraw
import numpy as np

def create_ai_background(width=1920, height=1080, filename='ai_bg.png'):
    """Create an AI-themed dark background similar to the provided image"""
    
    # Create base dark image with gradient
    img = Image.new('RGB', (width, height), color='#0a0e27')
    pixels = img.load()
    
    # Create dark blue gradient background
    for y in range(height):
        # Dark blue to darker gradient
        r = int(10 + (y / height) * 20)
        g = int(14 + (y / height) * 30)
        b = int(39 + (y / height) * 40)
        
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    # Add some subtle tech patterns
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Add subtle tech lines and dots
    np.random.seed(42)
    for _ in range(30):
        x1 = np.random.randint(0, width)
        y1 = np.random.randint(0, height)
        x2 = np.random.randint(0, width)
        y2 = np.random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=(50, 100, 200, 30), width=1)
    
    # Add glowing points
    for _ in range(50):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(2, 8)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(100, 180, 255, 80))
    
    # Save the image
    img.save(filename)
    print(f"✅ AI background created: {filename}")
    print(f"✅ Size: {width}x{height}")
    print(f"✅ Location: {os.path.abspath(filename)}")
    return filename

if __name__ == "__main__":
    create_ai_background()
    print("\n✅ AI background is ready! Run: python main.py")
