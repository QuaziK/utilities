import json
import os
import sys

with open(sys.argv[1], 'r') as json_file:
    json_list = list(json_file)

method = sys.argv[2]

total_size = 0

for j in json_list:
    
    if method == 'yt-dlp' or method == '1':
        os.system('yt-dlp ' + json.loads(j)['link'])
    elif method == 'curl' or method == '2':
        output = 1
        while output:
            output = os.system(f"curl \"{json.loads(j)['link']}\" -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\" -H \"Accept-Language: en,en-US;q=0.5\" -H \"Accept-Encoding: gzip, deflate, br, zstd\" -H \"Prefer: safe\" -H \"Referer: https://get.bunkrr.su/\" -H \"DNT: 1\" -H \"Sec-GPC: 1\" -H \"Connection: keep-alive\" -H \"Cookie: __ddg8_=pr0bGew6SKZuSwdp; __ddg9_=96.242.179.229; __ddg10_=1734049741; __ddg1_=vDaXWeeX8yyLvYQ9HNcU\" -H \"Upgrade-Insecure-Requests: 1\" -H \"Sec-Fetch-Dest: document\" -H \"Sec-Fetch-Mode: navigate\" -H \"Sec-Fetch-Site: cross-site\" -H \"Sec-Fetch-User: ?1\" -H \"Priority: u=0, i\" -H \"TE: trailers\" -C - -O")
    else:
        print('dumbass')

    total_size = total_size + float(json.loads(j)['size'].strip()[:-3])
    
print(f'TOTAL DOWNLOADED: %.2f % {total_size/1000.0} GB')
