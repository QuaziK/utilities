import scrapy


class CoomerSpider(scrapy.Spider):
    name = "coomer"
    
    headers = {
        'Host': 'kemono.su',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Prefer': 'safe',
        'Referer': 'https://kemono.su/account/favorites/artists',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Cookie': '__ddgid_=ssnd1jtUz47rfWyU; __ddg2_=94JtOiPhvUoRSur3; __ddg1_=t8RB2dY6Z74dsWU9Nk9K; session=eyJfcGVybWFuZW50Ijp0cnVlLCJhY2NvdW50X2lkIjozOTQ5fQ.Z8EJ0Q.LDFGA6kjNl1i4MMRromQlag9x1A; thumbSize=180; __ddg8_=OO54fJGH9PmC10K0; __ddg10_=1740860066; __ddg9_=74.102.6.163; __ddgmark_=hW9C4ZT2eR6hKR9w; __ddg5_=Nwtn6O1PeGN42TcW',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'If-Modified-Since': 'Tue, 28 Jan 2025 03:56:37 GMT',
        'If-None-Match': "67985575-3fc",
        'Priority': 'u=0, i'
    }
    
    start_urls = [
        "https://kemono.su/patreon/user/107199244"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url, 
                headers=self.headers,
                callback=self.parse)

    def parse(self, response): 
        pages = response.xpath('//a[@aria-current="page"]/@href').getall()
        
        # parse page 1
       
        for page in pages:
            yield from response.follow_all(vid_links, self.parse_page)
            
    def parse_page(self, response):
        yield {
                'url': response.url
            }