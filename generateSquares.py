import csv

import textwrap

from PIL import Image, ImageDraw, ImageFont, ImageOps

width = 1024;
height = 1024;
textSize = 80
font = ImageFont.truetype("NimbusRoman-Regular.otf", size=textSize);

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    lines = textwrap.wrap(text, width= width // textSize)
    y_text = (height - textSize * len(lines)) / 2
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height


with open('./phrases.csv', 'r') as f:
    reader = csv.reader(f);
    for [phrase] in reader:
        print(phrase);
        img = Image.new('RGB', (width, height), color = 'white');
        imgDraw = ImageDraw.Draw(img);
        draw_multiple_line_text(img, phrase, font, 'black', 0)
        img = ImageOps.expand(img, border = 20, fill = 'black')
        img.save(f'./images/squares/{phrase}.jpg'); 
