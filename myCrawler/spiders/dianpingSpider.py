import scrapy
from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest
from scrapy.selector import Selector

# AJAX网页特点
# 1. 页面加载快速
# 2. 不刷新网页就能更新信息
# 3. 源代码内容与网页内容不同

# 从js文件读取内容
# 1. 审查元素列出js文件
# 2. 寻找可疑文件
# 3. 解析js文件内容

class Dianping(CrawlSpider):
    name = "dianpingTest"
    start_urls = [
        "https://www.dianping.com/search/keyword/3/0_杭州酒家"
        # "http://movie.douban.com/top250"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print(response.text)
