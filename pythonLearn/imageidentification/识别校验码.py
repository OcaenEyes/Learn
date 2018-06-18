#!/usr/env/bin/python3
#_*_coding:utf-8_*_
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from PIL import Image
import pytesseract

image = Image.open('/Users/gaozhiyong/Documents/GitHub/python/Learn/pythonLearn/imageidentification/checkCode.png')
text = pytesseract.image_to_string(image)
print(text)