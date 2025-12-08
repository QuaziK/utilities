from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import sys
    
LEVEL = 10

# open file and convert it to greyscale
im = Image.open(sys.argv[1]).convert('L')

# from photoshop tutorial: https://www.youtube.com/watch?v=eKLki6-gynU
# high pass 6px
# threshold 128
# gaussion blur 5px

for i in range(int(sys.argv[2])):
    print(f'Iteration {i+1} of {sys.argv[2]}')
    # high pass 
    low_pass = im.filter(ImageFilter.GaussianBlur(10))
    im = ImageChops.subtract(im, low_pass, scale=1.0, offset=128)
    # threshold 
    im = im.point(lambda p: p > 128 and 255)
    # gaussian
    im = im.filter(ImageFilter.GaussianBlur(5))

# make it crisp for viewing
im = im.point(lambda p: p > 128 and 255)
im.show()
#TODO turn sequence of pics into gif w/ ffmpeg
print('Saving...')
im.save(sys.argv[1].replace(sys.argv[1].split('/')[-1],'out.png'))