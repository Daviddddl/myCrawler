from lxml import etree
from myCrawler.utils.shop_manual import shop_name
from myCrawler.utils.shop_manual import shop_id
from myCrawler.utils.shop_manual import shop_url_id
from myCrawler.utils.shop_manual import shop_icon
import pymongo
from myCrawler.settings import MONGODB_HOST
from myCrawler.settings import MONGODB_PORT


url = 'http://www.dianping.com/shop/'+shop_url_id+'/dishlist/p'
for i in range(1, 28):
    print('当前解析到: ' + str(i))
    html = open('../crawler_files/'+shop_icon+'_dishlist_p'+str(i)+'.html', 'r')
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

        connection = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        tdb = connection.dinning_menu
        post_info = tdb.menu
        post_info.insert(data)
