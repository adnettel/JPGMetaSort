import os, datetime
from PIL import Image

# Code to identify date created.
DATE_CREATED_EXIF_TAG = 306

# Constructs list of (fileString, dateObject).
fileDateList = []
for file in os.listdir("./"):
    if file.lower().endswith("jpg"):
        image = Image.open(file)
        info = image._getexif()
        date = datetime.datetime.strptime(info[DATE_CREATED_EXIF_TAG], '%Y:%m:%d %H:%M:%S')
        fileDateList.append((file, date))

# Sorts list of (f, d) based on d.
fileDateList.sort(key=lambda f: f[1])

# Renames files in current folder based on their order in fileDateList.
# Starts at 000000.jpg
index = 0
for fileDate in fileDateList:
    os.rename(
        './' + fileDate[0],
        './' + '{:06d}'.format(index) + '.jpg'
    )
    index +=1
