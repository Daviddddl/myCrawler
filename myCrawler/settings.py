# -*- coding: utf-8 -*-

# Scrapy settings for myCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myCrawler'

SPIDER_MODULES = ['myCrawler.spiders']
NEWSPIDER_MODULE = 'myCrawler.spiders'

# 添加splash服务器地址
# docker run -p 8050:8050 scrapinghub/splash
# SPLASH_URL = 'http://localhost:8050'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'myCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = 'utf-8'

DEFAULT_REQUEST_HEADERS = {
    'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'https://dianping.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 '
                  'Safari/537.36',
}

DOWNLOAD_DELAY = 0.1
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'myCrawler.middlewares.MycrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 将splash middleware添加到DOWNLOADER_MIDDLEWARE中
# DOWNLOADER_MIDDLEWARES = {
#     # 'myCrawler.middlewares.MycrawlerDownloaderMiddleware': 543,
#     'scrapy.contrib.downloadermiddleware.seragent.UserAgentMiddleware': None,   # 禁用默认middleware
#     'myCrawler.middlewares.MyAgent': 543,
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# Enable SplashDeduplicateArgsMiddleware
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Set a custom DUPEFILTER_CLASS
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'myCrawler.pipelines.MycrawlerPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# a custom cache storage backend
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# 在settings.py中配置MongoDB的IP地址、端口号、数据记录名称，可以实现方便的更换MongoDB的数据库信息
# 在settings.py中引用pipelines.py 从而pipelines生效
# ITEM_PIPELINES = ['myCrawler.pipelines.MycrawlerPipeline']

MONGODB_HOST = '123.206.70.190'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'dinning_menu'
MONGODB_DOCNAME = 'menu'
