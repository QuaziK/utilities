from PIL import Image, ImageFilter, ImageChops
import numpy as np
import sys
import os
import math

# open file and convert it to greyscale
# TODO experiment with separating color chanels and analyzing their Turing formations
im = Image.open(sys.argv[1]).convert('L')
previous = im
diff = math.inf
STOP_THRESHOLD = .01
DIR = sys.argv[1].replace(sys.argv[1].split("/")[-1],"")

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

print('Running Diffusion...')

# loop diffusion until the difference is negligible
i = 0
while True:
    i = i + 1
    previous = im
    print(f'\rIteration {i}',end='\r',flush=True)
    
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
    # save a crisper version for the gif
    threshold(im, 128).save(DIR+f'/out_{i:03d}.png')

print(f'Diffussion finished in {i} iterations.')
# turn sequence of pics into gif
print('Compiling GIF')
os.system(f'ffmpeg -y -hide_banner -loglevel error -f image2 -framerate 5 -i {DIR+"out_%03d.png"} {DIR+"out.gif"}')
# delete the pngs, all but the last one
for ii in range(1,i-1):
    print(f'\rCleaning Up {ii}/{i}',end='\r',flush=True)
    os.remove(f'{DIR}out_{ii:03d}.png')