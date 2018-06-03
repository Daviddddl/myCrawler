import scrapy
from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from myCrawler.utils.mongodb_utils import *


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
    shops_list = [
        '杭州酒家',
        '绿茶餐厅',
        '院子餐厅',
        '弄堂里',
        '外婆家',
        '新发现',
        '新白鹿',
        '老头儿油爆虾',
        '新周记',
        '楼外楼',
        '粥皇',
        '小杨生煎',
        '秋叶小町',
        '知味观',
        '张生记',
        '胖哥俩肉蟹煲'
    ]
    start_urls = [
        # "https://www.dianping.com/search/keyword/3/0_"
        'http://www.dianping.com/shop/97567356'
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print(response.text)

        res_url = response.url
        res_body = response.body.decode("utf-8")
        res_header = response.headers
        print(res_header)
        print(res_url)
        print(res_body)

        selector = Selector(response=response)
        content = selector.xpath('//*[@id="rev_421498185"]/div/div[1]/p/text()[2]')
        print(content.extract())

        # data = {
        #     'name': '我就再试i 一试',
        #     'age': 3435,
        #     'skills': ['吃饭', '睡觉', '哗啦啦'],
        #     'caca': 'kaka123'
        # }
        #
        # insert_data(data=data)
        #
        # print(data)
