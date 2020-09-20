from PIL import Image, ImageDraw, ImageFont
import easygui as eg
import textwrap

def memerizer(name, text, colour):
    image = Image.open(name)
    width, height = image.size
    print(width, height)
    font_type = ImageFont.truetype("Arial.ttf",36)
    draw = ImageDraw.Draw(image)
    if len(text)> 24:
        split = textwrap.wrap(text, 24)    
        draw.text(xy=(10,10),text=split[0],fill=(colour),font=font_type)
        draw.text(xy=(12,12),text=split[0],fill=(0,0,0),font=font_type)
        y1 = height - 102
        y2 = height - 100
        draw.text(xy=(10,y1),text=split[1],fill=(colour),font=font_type)
        draw.text(xy=(12,y2),text=split[1],fill=(0,0,0),font=font_type)
    else:
        draw.text(xy=(10,10),text=text,fill=(colour),font=font_type)
        draw.text(xy=(12,12),text=text,fill=(0,0,0),font=font_type)        
    image.show()
    filename = eg.filesavebox(title="File to save")
    image.save(filename)
try:
    name = eg.fileopenbox(title="File to open?")
    text  = eg.enterbox(title="Type in your meme",msg="Type your meme here")
    colour = eg.enterbox(title="Colour Choice",msg="Type a colour in using rrr,ggg,bbb format")
    colour = tuple(map(int, colour.split(",")))
    memerizer(name, text, colour)
except ValueError:
    print("Sorry you can't save without a filename")