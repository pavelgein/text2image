from PIL import Image, ImageFont, ImageDraw
import os

pathArial = "C:\\Windows\\Fonts\\arial.ttf"
IntData = ['height', 'width']
FontData = ['font', 'size']

#debug = open("output.txt", "w")

class DescriptionImage:
	def __init__(self, height = 100 , width = 100, 
				path = "./input.txt", format = 'png', size = 20, 
				color = 'black', font_name = pathArial, 
				encoding = 'utf8', folder = "./", background = 'white'):
		self.height = height
		self.width = width
		self.path = path
		self.format = format
		self.font = FontDescription(font_name, size)
		self.color = color
		self.encoding = encoding
		self.folder = folder
		self.background = background

class FontDescription:
	def __init__(self, font_name = pathArial, size = 20):
		self.name = font_name
		self.size = size
   
def ReadDescription(file_in):
	InpDescr = open(file_in, "r").readlines()
	description = DescriptionImage()
	descrFont = FontDescription()
	for string in InpDescr:
		h = string.split("=")
		if (len(h) < 2):
			continue
		name = h[0].strip()
		value = h[1].strip()
		if (name in IntData):
			setattr(description, name, int(value))
		elif (name in FontData):
			if (name == 'font'):
				descrFont.name = value
			else:
				descrFont.size = int(value)
		else:
			setattr(description, name, value)
	description.font = descrFont
	return description
	
def ShowDescription(desc):
	print(desc.encoding)
	print(desc.font.size)
	print(desc.width)
	print(desc.font.name)
	

	
image = ReadDescription("./config.ini")

inp = [i.split(';')[0].strip() for i in open(image.path, "r").readlines()]

#Create a target folder
if (os.access(image.folder, os.F_OK)):
	if (not os.access(image.folder, os.W_OK)):
		print('Can\'t write in folder!')
else:
	os.makedirs(image.folder)

font = ImageFont.truetype(image.font.name, image.font.size, encoding='unic')	
os.chdir(image.folder)

for st in inp:
	#h = st.split(":")
	ind = st.find(':')
	if (ind == -1):
		continue
	name = st[0:i].strip()
	text = s[i+1:].strip()

	# Check the size of image
	sizes = font.getsize(text)
	width = max(image.width + 20, sizes[0] + 20) 
	height = max(image.height + 20, sizes[1] + 20)

	#Set up margins
	top = (height - sizes[1]) / 2
	left = (width - sizes[0]) / 2

	Im = Image.new("RGB", (width, height), image.background)
	draw = ImageDraw.Draw(Im)
	draw.text((left, top), text.decode(image.encoding), font =  font, fill = image.color) 
	Im.save("./" + name + "." + image.format, image.format)
