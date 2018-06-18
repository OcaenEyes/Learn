#!/usr/env/bin/python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from PIL import Image
import pytesseract

import time
time1 = time.time()
print(time1)

image = Image.open('/Users/gaozhiyong/Documents/GitHub/python/Learn/pythonLearn/imageidentification/zimu.png')
content_text=pytesseract.image_to_string(image)
print(content_text)