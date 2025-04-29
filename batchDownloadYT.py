import os
import sys

write_target = 'pages.txt'

if (len(sys.argv)>1):
    write_target = sys.argv[1]

pages = open(write_target, 'r')
data = pages.read()
lis = data.split('\n')

for url in lis:
    if url:
        print('[info] {}/{}'.format(lis.index(url)+1,len(lis)))
        print('[info] {}'.format(url));
        try:
            os.system('yt-dlp {}'.format(url))
        except:
            print('fucky wuppy happenerd')
        