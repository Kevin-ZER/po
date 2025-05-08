import os
from PIL import Image, ImageDraw, ImageFont
import random

# Create necessary directories
os.makedirs('public/projects', exist_ok=True)
os.makedirs('public/sections', exist_ok=True)

def create_cybersec_image(title, filename, color, directory='sections', size=(800, 600)):
    # Create a new image with a dark background
    width, height = size
    image = Image.new('RGB', (width, height), (15, 15, 20))
    draw = ImageDraw.Draw(image)
    
    # Add a matrix-like rain effect
    for _ in range(200):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        length = random.randint(5, 30)
        opacity = random.randint(50, 200)
        for i in range(length):
            if y + i < height:
                alpha = int(opacity * (1 - i/length))
                draw.point((x, y + i), fill=(color[0], color[1], color[2], alpha))
    
    # Add hexagonal grid pattern
    hex_size = 30
    for i in range(-hex_size, width + hex_size, hex_size):
        for j in range(-hex_size, height + hex_size, hex_size):
            points = [
                (i, j + hex_size//2),
                (i + hex_size//2, j),
                (i + hex_size, j + hex_size//2),
                (i + hex_size, j + hex_size*3//2),
                (i + hex_size//2, j + hex_size*2),
                (i, j + hex_size*3//2)
            ]
            draw.line(points + [points[0]], fill=(color[0]//4, color[1]//4, color[2]//4), width=1)
    
    # Add title with glow effect
    title_x = width//2 - len(title)*10
    title_y = height//2 - 20
    
    # Add glow
    for offset in range(5, 0, -1):
        glow_color = tuple(min(255, c // (offset)) for c in color)
        draw.text((title_x-offset, title_y), title, fill=glow_color)
        draw.text((title_x+offset, title_y), title, fill=glow_color)
    
    # Add main title
    draw.text((title_x, title_y), title, fill=color)
    
    # Save the image
    image.save(f'public/{directory}/{filename}')

# Generate project images
projects = [
    ('Phishing Framework', 'phishing.jpg', (0, 120, 255)),  # Blue
    ('Network Security', 'network.jpg', (0, 255, 100)),     # Green
    ('Code Scanner', 'scanner.jpg', (255, 200, 0)),         # Yellow
    ('Threat Intelligence', 'threat.jpg', (200, 0, 255))    # Purple
]

# Generate section images
sections = [
    ('About Me - Cybersecurity Expert', 'about.jpg', (0, 150, 255)),      # Blue
    ('Skills & Expertise', 'skills.jpg', (0, 255, 150)),                  # Cyan
    ('Security Experience', 'experience.jpg', (255, 100, 0)),             # Orange
    ('Contact & Security Consultation', 'contact.jpg', (150, 0, 255)),    # Purple
    ('Hero Background', 'hero.jpg', (0, 200, 255), (1200, 800)),         # Light Blue
]

# Generate all images
for title, filename, color in projects:
    create_cybersec_image(title, filename, color, 'projects')
    print(f'Generated project image: {filename}')

for title, filename, color, *size in sections:
    img_size = size[0] if size else (800, 600)
    create_cybersec_image(title, filename, color, 'sections', img_size)
    print(f'Generated section image: {filename}')

print('All project images have been generated!') 