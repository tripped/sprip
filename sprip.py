import sys
from PIL import Image

if len(sys.argv) < 4:
    print "Usage: python %s <filename> <offset> <width> <height>" % sys.argv[0]

file = open(sys.argv[1])

offset = int(sys.argv[2], 0)
width = int(sys.argv[3])
height = int(sys.argv[4])

# Read raw data from the file
file.seek(offset)
data = file.read(width * height)

# Load it as an image
image = Image.fromstring('P', (width, height), data)

# Get palette (temporarily hardcoded)
palfile = open('quarantine/floor.img')
palfile.seek(0xD)
palette = palfile.read(768)

image.putpalette(palette)

image.save('output.png')
