#! usr/bin/env python3

import os
import sys
from glob import glob
from PIL import Image
for infile in os.listdir('Images_Original'):
	try:
		image= Image.open(infile).convert('RGB')
		print(image.format)
		path, filename=os.path.split(infile)	
		print(filename)
		filename=os.path.splitext(filename)[0]
		image.rotate(270).resize(128,128).save("/Images_New/{}.jpeg".format(filename))	
		print("yay")
	except:
		print("NO")
		pass