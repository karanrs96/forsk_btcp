# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:56:28 2018

@author: Karan
"""

#from PIL import Image
import PIL

img = PIL.Image.open("sample.jpg")

img = img.convert("L") #Greyscale
img = img.rotate(-90) #clockwise 90 degree
half_width, half_height = img.size
half_width = half_width/2
half_height = half_height/2
img = img.crop((half_width-80, half_height-102, half_width+80, half_height+102)) #Crop (Center) (size = 160(W), 204(H))
img.thumbnail((75, 75))
fname = raw_input("Enter file name: ")
img.save(fname+".jpg")
#img.show()