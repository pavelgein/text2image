from PIL import Image, ImageFont, ImageDraw
import os
from sys import argv

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
	def read(self, fileInp):
		#print("Read method is working\n")
		inp = open(fileInp, "r").readlines()
		descrFont = FontDescription()

		#Parse an input file
		for string in inp:
			#Find a '='
			indEq = string.find('=')
			if (indEq == -1):
				continue
			#print("Read have been still working")
			#print(string)
			#print(indEq)
			name = string[0 : indEq].strip()
			value = string[indEq + 1 :].strip()
			#print("Name: " + name + ", value:" + value + "\n")
			if (name in IntData):
				setattr(self, name, int(value))
			elif (name in FontData):
				if (name == 'font'):
					descrFont.name = value
				else:
					descrFont.size = int(value)
			else:
				setattr(self, name, value)
			self.font = descrFont


class FontDescription:
	def __init__(self, font_name = pathArial, size = 20):
		self.name = font_name
		self.size = size
   
	
def ShowDescription(desc):
	print(desc.encoding)
	print(desc.font.size)
	print(desc.width)
	print(desc.font.name)
	

#New Version
image = DescriptionImage()

configPath = './congif.ini'
if (len(argv) > 1):
    configPath = argv[1]
image.read("./config.ini")

#Old version	
#image = ReadDescription("./config.ini")

inp = open(image.path, "r").readlines()


#Create a target folder
if (not os.access(image.folder, os.F_OK)):
	os.makedirs(image.folder)


font = ImageFont.truetype(image.font.name, image.font.size, encoding='unic')	
os.chdir(image.folder)


for st in inp:
    
	#Delete a comment
	#print(st + "\n")
	indComment = st.find(';');
	if (indComment != -1):
		st = st[: indComment]

    #Parse the string
	ind = st.find(':')
	if (ind == -1):
		continue
	name = st[0 : ind].strip()
	text = st[ind + 1:].strip()

	# Check the size of image
	sizes = font.getsize(text)
	width = max(image.width + 20, sizes[0] + 20) 
	height = max(image.height + 20, sizes[1] + 20)

	#Set up margins
	top = (height - sizes[1]) / 2
	left = (width - sizes[0]) / 2

    #Create an image object
	Im = Image.new("RGB", (width, height), image.background)
	draw = ImageDraw.Draw(Im)
	draw.text((left, top), text.decode(image.encoding), font =  font, fill = image.color) 
    #Save the image on disk
	Im.save("./" + name + "." + image.format, image.format)
