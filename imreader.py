import sys
from PIL import Image
import commands
usrimg = Image.open(sys.argv[1])
# Converting the image to greyscale.
captcha = usrimg.convert('1')                               
# Saving the image as tesseract can read.
captcha.save('temp.bmp', dpi=(100,100))
# Invoking tesseract from python to extract characters
commands.getoutput('tesseract temp.bmp data')
# Reading the output generated in data.txt
with open('data.txt', 'r') as data:
        content = data.readlines()
        print ''.join(content) 
        # you may also want to remove whitespace characters like `\n` at the end of each line
        # content = [x.strip() for x in content]
