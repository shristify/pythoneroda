import os
from PIL import Image, ImageDraw, ImageFont
import fonts.ttf


for file in os.listdir("."): 
    try:
	image = Image.open(file).convert('RGBA')
	#print(image.format, image.size, image.mode) # test
	path, filename = os.path.split(file)
	#print(filename)
	filename = os.path.splitext(filename)[0] # get filename without extension
	filex='./changed/{}.png'.format(filename)
    	image.rotate(270).resize((128,128)).save(filex)
	baseLayer= Image.open(filex).convert('RGBA')
	font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
	textLayer = Image.new('RGBA', baseLayer.size, (255,255,255,0))
	draw = ImageDraw.Draw(textLayer)
	draw.text((14,14), filename, font=font, fill=(255,255,255,128))
	draw.text((14,60), "@confusedcoder1", font=font, fill=(255,255,255,255))
	out = Image.alpha_composite(baseLayer, textLayer)
	out.show()
	filex='./changed2/{}.png'.format(filename)
    	out.save(filex)
	#print('OK')
    except:
	print("pass")	
	pass
