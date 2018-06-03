from lxml import etree
from myCrawler.utils.mongodb_utils import *


html = open('../crawler_files/dianping_shop20180603195212.html', 'r')

selector = etree.HTML(html.read())
content = selector.xpath('//*[@class="comment-item"]')
for each in content:
    data = {
        'user': str(each.xpath('./p/a/text()')),
        'price': str(each.xpath('./div/p/span/text()')),
        'comments': str(each.xpath('.//*[@class="desc"]/text()')),
        'comments_detail': str(each.xpath('.//*[@class="desc J-desc"]/text()')),
        'time': str(each.xpath('.//*[@class="time"]/text()')),
        'photos': str(each.xpath('.//*[@class="item J-photo"]/img/@src'))
    }
    insert_data(data=data)
    print(data)
