import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bunkrr"
    
    headers = {
        'Host': 'stats.bunkr.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Prefer': 'safe',
        'Referer': 'https://bunkr.si/',
        'Origin': 'https://bunkr.si',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=4',
    }
    
    api_url = 'https://stats.bunkr.ru/api/file/stats/{}'
    
    start_urls = [
        ""
    ]

    def parse(self, response):
        # vid_links = response.xpath('//div[@class="grid-images_box rounded-lg dark:bg-gray-200 xl:aspect-w-7 xl:aspect-h-8 p-2.5 border-2 display relative flex text-center"]/div/a/@href')    
        vid_links = response.xpath('//div[@class="relative group/item theItem"]/div/a/@href')
        yield from response.follow_all(vid_links, self.vid_link_parse)        

        
    def vid_link_parse(self, response):
        id = response.xpath('//div[@id="fileTracker"]/@data-file-id').get()
        
        link = ''
        
        if response.xpath('//video[@id="player"]/source/@src').get():
            link = response.xpath('//video[@id="player"]/source/@src').get()
        elif response.xpath('//img[@title="Behave or T4C0 will spank u :cumsby:"]/@src').get():
            link = response.xpath('//img[@title="Behave or T4C0 will spank u :cumsby:"]/@src').get()
        elif response.xpath('//video/source/@src').get():
            link = response.xpath('//video/source/@src').get()
        elif response.xpath('//meta').getall():
            ending = response.xpath('//meta')[4].xpath('@content').get()
            begin = response.xpath('//meta')[5].xpath('@content').get()
            offset = 2 if '.png' in begin or '.jpeg' in begin else 3
            link = 'http://nachos.bunkr.ru/' + begin.split('/')[-1].split('.')[-offset] + '.mp4?n=' + ending
        else:
            link = 'SOURCE LINK NOT FOUND'
        

        yield scrapy.Request(
            url=self.api_url.format(id),
            headers=self.headers,
            callback=self.api_parse,
            method="GET",
            meta={
                'link': link,
                'size': response.css('p.text-xs::text').get().strip(),
                'id': id
            }
        )
        
    def api_parse(self, response):
        resp=response.json()
        if 'SOURCE LINK NOT FOUND' not in response.meta['link']:
            yield {
                'link': response.meta['link'],
                'size': response.meta['size'],
                'id': response.meta['id'],
                'downloadCount': resp['downloadCount']
            }