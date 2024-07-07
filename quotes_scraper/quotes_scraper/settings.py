

BOT_NAME = "quotes_scraper"

SPIDER_MODULES = ["quotes_scraper.spiders"]
NEWSPIDER_MODULE = "quotes_scraper.spiders"

ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
