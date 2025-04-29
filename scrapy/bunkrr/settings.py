BOT_NAME = "bunkrr"

SPIDER_MODULES = ["bunkrr.spiders"]
NEWSPIDER_MODULE = "bunkrr.spiders"

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; tv:109.0) Gecko/20100101 Firefox/115.0'

ROBOTSTXT_OBEY = False

# DOWNLOAD_DELAY = 1

COOKIES_ENABLED = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, defalte, br",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive"
}