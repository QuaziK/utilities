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
        print('[info]{}/{}'.format(lis.index(url)+1,len(lis)))
        url = url.replace('https://player.vimeo.com/','')
        url = url.replace('https://vimeo.com/','')
        url = url.replace('https://i.vimeocdn.com/video/','')
        url = url.replace('?share=copy','')
        print('[info]{}'.format(url));
        try:
            os.system('yt-dlp https://player.vimeo.com/video/{} --referer \"https://www.patreon.com/user/posts?u=24727122\"'.format(url))
        except:
            print('fucky wuppy happenerd')
        