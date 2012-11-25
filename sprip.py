import sys
from PIL import Image

def readbyte(f):
    """Read one byte as an int from a file"""
    return ord(f.read(1))

if len(sys.argv) < 3:
    print "Usage: python %s <filename> <palettefile> [output]" % sys.argv[0]
    print "  `output` should be a format string; '%03d.png' is the default."
    exit(1)

outformat = "%03d.png"
if len(sys.argv) >= 4:
    outformat = sys.argv[3]

# Load the palette
palfile = open(sys.argv[2], 'rb')
palfile.seek(0xD)
palette = palfile.read(768)
palfile.close()

# Open the main texture file
datfile = open(sys.argv[1], 'rb')

# Read sprite count and sizes
count = readbyte(datfile)
sizes = [(readbyte(datfile), readbyte(datfile)) for _ in range(count)]

# Read each sprite based on the sizes
for i,size in enumerate(sizes):
    data = datfile.read(size[0] * size[1])
    image = Image.fromstring('P', size, data)
    image.putpalette(palette)
    image.save(outformat % i)

