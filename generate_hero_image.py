from PIL import Image, ImageDraw, ImageFont
import numpy as np
from datetime import datetime

def create_cyber_background(width=1200, height=800):
    # Create a dark background
    background = Image.new('RGB', (width, height), (15, 23, 42))  # Dark blue background
    
    # Create a draw object
    draw = ImageDraw.Draw(background)
    
    # Add gradient overlay
    for y in range(height):
        alpha = int(255 * (1 - y/height * 0.5))  # Fade to darker at bottom
        for x in range(width):
            r, g, b = background.getpixel((x, y))
            draw.point((x, y), fill=(r, g, b, alpha))
    
    # Add matrix-like effect
    for _ in range(1000):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        size = np.random.randint(1, 3)
        color = (0, 255, 0, np.random.randint(50, 150))  # Green with varying opacity
        draw.rectangle([x, y, x+size, y+size], fill=color)
    
    # Add circuit-like patterns
    for _ in range(50):
        start_x = np.random.randint(0, width)
        start_y = np.random.randint(0, height)
        length = np.random.randint(50, 200)
        color = (0, 255, 0, np.random.randint(30, 100))
        
        # Draw horizontal or vertical line
        if np.random.random() > 0.5:
            draw.line([start_x, start_y, start_x + length, start_y], fill=color, width=2)
        else:
            draw.line([start_x, start_y, start_x, start_y + length], fill=color, width=2)
    
    # Add some glowing orbs
    for _ in range(20):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        radius = np.random.randint(20, 50)
        color = (0, 255, 0, np.random.randint(30, 100))
        
        # Draw gradient circle
        for r in range(radius, 0, -1):
            alpha = int(color[3] * (r/radius))
            draw.ellipse([x-r, y-r, x+r, y+r], fill=(0, 255, 0, alpha))
    
    return background

def add_text(background, text, position, size=60, color=(0, 255, 0)):
    draw = ImageDraw.Draw(background)
    
    # Try to load a monospace font, fall back to default if not available
    try:
        font = ImageFont.truetype("consolas.ttf", size)
    except:
        font = ImageFont.load_default()
    
    # Add text with glow effect
    for offset in range(3):
        draw.text((position[0]+offset, position[1]), text, font=font, fill=(0, 255, 0, 100))
        draw.text((position[0], position[1]+offset), text, font=font, fill=(0, 255, 0, 100))
    
    # Add main text
    draw.text(position, text, font=font, fill=color)
    
    return background

def main():
    # Create the background
    background = create_cyber_background()
    
    # Add some cybersecurity-themed text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    background = add_text(background, "CYBER SECURITY", (50, 50), size=80)
    background = add_text(background, "SYSTEM ACTIVE", (50, 150), size=40)
    background = add_text(background, timestamp, (50, 200), size=30)
    
    # Save the image
    background.save("public/hero.jpg", quality=95)
    print("Hero image generated successfully!")

if __name__ == "__main__":
    main() 