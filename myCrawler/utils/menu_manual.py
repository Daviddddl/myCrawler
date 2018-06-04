from lxml import etree
from myCrawler.utils.mongodb_utils import *


shop_name = '杭州酒家(延安路店)'
url = 'http://www.dianping.com/shop/11549988/dishlist/p'
shop_id = '01'

for i in range(1, 28):
    print('当前解析到: ' + str(i))
    html = open('../crawler_files/hzjj_dishlist_p'+str(i)+'.html', 'r')
    selector = etree.HTML(html.read())
    dishes_list = selector.xpath('//*[@class="list-desc"]/ul/a')
    for each_dish in dishes_list:
        picture = str(each_dish.xpath('.//*[@class="shop-food-img"]/img/@src'))
        dish_name = str(each_dish.xpath('.//*[@class="shop-food-name"]/text()'))
        dish_recommend = str(each_dish.xpath('.//*[@class="recommend-count"]/text()'))
        price = str(each_dish.xpath('.//*[@class="shop-food-money"]/text()'))
        data = {
            'shop_id': shop_id,
            'shop_name':shop_name,
            'url': url+str(i),
            'picture': picture,
            'dish_name': dish_name,
            'dish_recommend': dish_recommend,
            'price': price
        }
        # print(data)
        insert_data(data=data)
