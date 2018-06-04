from lxml import etree
from myCrawler.utils.shop_manual import shop_name
from myCrawler.utils.shop_manual import shop_id
from myCrawler.utils.shop_manual import shop_url_id
from myCrawler.utils.shop_manual import shop_icon
import pymongo
from myCrawler.settings import MONGODB_HOST
from myCrawler.settings import MONGODB_PORT


url = 'http://www.dianping.com/shop/'+shop_url_id+'/review_all/p'
for i in range(1, 10):
    print('当前解析到: ' + str(i))
    html = open('../crawler_files/'+shop_icon+'_comments_p'+str(i)+'.html', 'r')
    selector = etree.HTML(html.read())
    comments_list = selector.xpath('//*[@class="reviews-items"]/ul/li')
    for each in comments_list:

        user = str(each.xpath('.//*[@class="name"]/text()')[0]).strip()

        comments_list = each.xpath('.//*[@class="review-words Hide"]/text()')
        comments = ''
        for each_comment in comments_list:
            comments = comments + str(each_comment).strip()

        recommend = str(each.xpath('.//*[@class="review-recommend"]/a/text()'))

        review_rank = ''
        for each_review_rank in each.xpath('.//*[@class="score"]/span/text()'):
            review_rank = review_rank + str(each_review_rank).strip() + '  '

        pictures_list = each.xpath('.//*[@class="review-pictures"]/ul/li')
        pictures = ''
        for each_picture in pictures_list:
            pictures = pictures + str(each_picture.xpath('./a/img/@data-big')) + '  '

        data = {
            'shop_id': shop_id,
            'url': url + str(i),
            'shop_name': shop_name,
            'user': user,
            'comments': comments,
            'recommand': recommend,
            'review_rank': review_rank,
            'pictures': pictures
        }
        # print(data)

        connection = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        tdb = connection.dinning_menu
        post_info = tdb.comments
        post_info.insert(data)
