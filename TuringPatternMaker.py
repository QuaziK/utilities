from PIL import Image, ImageFilter, ImageChops
from skimage import io, img_as_float
import numpy as np
import sys
import math

# open file and convert it to greyscale
im = Image.open(sys.argv[1]).convert('L')
previous = im
diff = math.inf
STOP_THRESHOLD = 0.01

# from photoshop tutorial: https://www.youtube.com/watch?v=eKLki6-gynU
# high pass 6px
# threshold 128
# gaussion blur 5px

def highPass(im, px):
    low_pass = im.filter(ImageFilter.GaussianBlur(px))
    return ImageChops.subtract(im, low_pass, scale=1.0, offset=128)

def threshold(im, thresh):
    return im.point(lambda p: p > thresh and 255)
    
def getDiff(im1, im2):
    return abs(np.mean(np.array(im1) - np.array(im2)))

# loop diffusion until the difference is negligible
i = 0
while True:
    i = i + 1
    previous = im
    print(f'Iteration {i}')
    
    # high pass 
    im = highPass(im, 6)
    # threshold 
    im = threshold(im, 128)
    # gaussian
    im = im.filter(ImageFilter.GaussianBlur(5))
    
    # check difference
    if abs(diff - getDiff(im, previous)) <= STOP_THRESHOLD:
        break    
    diff = getDiff(im,previous)

# make it crisp for viewing
im = threshold(im, 128)

im.show()
#TODO turn sequence of pics into gif
print('Saving...')
im.save(sys.argv[1].replace(sys.argv[1].split('/')[-1],'out.png'))