import PIL
from PIL import Image
from tkinter.filedialog import *

f1 = askopenfilenames()
img = Image.open(f1[0])
img.save("co.jpg", "JPEG", optimize = True, quality = 10)
Image.open('co.jpg')
