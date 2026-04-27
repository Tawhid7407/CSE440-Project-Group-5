import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import os

def create_blue_background(width=1920, height=1080, filename='blue_bg.png'):
    """Create a blue-themed background image"""
    
    # Create a base image with blue gradient
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()
    
    # Create gradient from light blue (sky) to deeper blue
    for y in range(height):
        # Sky blue gradient (light at top, deeper at bottom)
        r = int(135 - (y / height) * 50)  # 135 to 85
        g = int(206 - (y / height) * 30)  # 206 to 176
        b = int(235 - (y / height) * 20)  # 235 to 215
        
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    # Draw decorative elements
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Add some cloud-like shapes
    for i in range(3):
        x_center = (i + 1) * (width // 4)
        y_center = 150 + i * 80
        
        # Draw oval clouds
        for j in range(3):
            offset = j * 60 - 60
            draw.ellipse(
                [x_center + offset - 40, y_center - 25, x_center + offset + 40, y_center + 25],
                fill=(255, 255, 255, 120),
                outline=(200, 200, 220, 100)
            )
    
    # Add some water wave patterns at the bottom
    wave_height = height - 200
    for i in range(width):
        y_offset = int(20 * np.sin(i / 100)) + wave_height
        pixels[i, y_offset] = (100, 180, 255)
    
    # Add subtle bokeh effects (light circles)
    np.random.seed(42)
    for _ in range(30):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        r = np.random.randint(10, 30)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(200, 220, 255, 50))
    
    # Apply slight blur
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    
    # Save the image
    img.save(filename)
    print(f"✅ Blue background created: {filename}")
    print(f"✅ Size: {width}x{height}")
    print(f"✅ Location: {os.path.abspath(filename)}")
    return filename

if __name__ == "__main__":
    create_blue_background()
    print("\n✅ Blue background is ready! Run: python main.py")
