from bs4 import BeautifulSoup as BS
import urllib.request
import os
import sys

write_target = "pages.txt"

if (len(sys.argv)>1):
    write_target = sys.argv[1]

pages = open(write_target, 'r')
data = pages.read()
lis = data.split('\n')

for url in lis:
    if url:
        html = urllib.request.urlopen(url)
        print('[info]{}/{}'.format(lis.index(url)+1,len(lis)))
        soup = BS(html,features="html.parser")
        print('[info]{}'.format(soup.source['src']))
        try:
            os.system('yt-dlp {}'.format(soup.source['src']))
        except:
            print('fucky wuppy happenerd')        
 