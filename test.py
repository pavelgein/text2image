from PIL import Image, ImageFont, ImageDraw
import os

#if (os.access("./dist/config.ini", os.F_OK)):
#	print("YES")
#else:
#	print("NO")

class Simple:
	def __init__(self, x):
		self.x = x

a = Simple(2)
setattr(a, 'x', 3)
print(a.x)	             

#font = ImageFont.truetype("arial.ttf", 16, encoding="cp1251")



#Im = Image.new("RGB", (100, 100), "white")
#draw = ImageDraw.Draw(Im)


#draw.text((left, top), text, font =  font, fill=image.color) 
#Im.show()