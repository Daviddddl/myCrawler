import scrapy
from scrapy.spiders import CrawlSpider
# from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from myCrawler.utils.mongodb_utils import *
import datetime
from lxml import etree

# AJAX网页特点
# 1. 页面加载快速
# 2. 不刷新网页就能更新信息
# 3. 源代码内容与网页内容不同

# 从js文件读取内容
# 1. 审查元素列出js文件
# 2. 寻找可疑文件
# 3. 解析js文件内容

nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 现在时刻


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
        # 'http://210.46.97.225/gov_corpus/corpus_look1.html'
        'http://xiaodu.baidu.com/saiya/gaokao/schooldetail?schoolId=8&tab=2&logFrom=sl_8%27'
        # "https://www.dianping.com/search/keyword/3/0_"
        # 'http://www.dianping.com/shop/97567356'
        # 'http://www.dianping.com/shop/97567356/review_all/p2'
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        res_url = response.url
        # with open('../crawler_files/dianping_shop'+nowTime+'.html', 'w') as f:
        #     f.write(res_url)
        #     f.write('\n\n')
        #     f.write(response.text)

        # print(response.text.encode('utf-8').decode('unicode_escape'))

        # selector = Selector(response=response)
        # ques_list = selector.xpath('//*[@class ="c-container tie-container"]')
        # print(ques_list)


        #
        # selector = Selector(response=response)
        # web_content = selector.xpath('//*[@class="comment-item"]')
        # for each in web_content:
        #     data = {
        #         'user': str(each.xpath('./p/a/text()')),
        #         'price': str(each.xpath('./div/p/span/text()')),
        #         'comments': str(each.xpath('.//*[@class="desc"]/text()')),
        #         'comments_detail': str(each.xpath('.//*[@class="desc J-desc"]/text()')),
        #         'time': str(each.xpath('.//*[@class="time"]/text()'))
        #     }
        #     insert_data(data=data)
        #     print(data)
