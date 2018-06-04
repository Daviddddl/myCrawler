from lxml import etree
from myCrawler.utils.mongodb_utils import *


# shop_id = '01'
# shop_name = 'Au79 Brunch(龙湖滨江天街店)'
# address = '龙湖滨江天街南侧室外商业街铂金岛1层(天街4号门向西100米)'
# phone = '0571-85229751'
# detail = '人均：131元 口味：8.5 环境：9.2 服务：9.1'
# shop_url = 'http://www.dianping.com/shop/97567356'

# shop_id = '02'
# shop_name = '杭州酒家(延安路店)'
# address = '延安路205号1-3楼(延安路邮电路口)'
# phone = '0571-87087123'
# detail = '人均:88元 口味:8.5 环境:8.5 服务:8.2'
# shop_url = 'http://www.dianping.com/shop/11549988'

# shop_id = '03'
# shop_name = '绿茶餐厅(西湖银泰店)'
# address = '延安南路98号西湖银泰3楼(近吴山广场)'
# phone = '0571-87002788 0571-87002988'
# detail = '人均：63元 口味：8.0 环境：8.5 服务：7.7'
# shop_url = 'http://www.dianping.com/shop/5506896'
# 还有几个分店

# shop_id = '04'
# shop_name = '院子餐厅(桥西直街店)'
# address = '桥西直街64-73号(中国刀剪剑博物馆南侧运河边)'
# phone = '0571-88194788'
# detail = '人均：74元 口味：8.3 环境：9.0 服务：8.0'
# shop_url = 'http://www.dianping.com/shop/4503523'
# 还有几个分店

# shop_id = '05'
# shop_name = '弄堂里(湖滨银泰in77C区店)'
# address = '东坡路7号杭州湖滨银泰in77C1区3层A301号'
# phone = '0571-85870518'
# detail = '人均：65元 口味：7.9 环境：8.3 服务：7.6'
# shop_url = 'http://www.dianping.com/shop/8937538'
# 还有几个分店

# shop_id = '06'
# shop_name = '外婆家(湖滨银泰店)'
# address = '东坡路7号杭州湖滨银泰in77C1区2层209室'
# phone = '0571-85870307'
# detail = '人均:76元 口味:7.9 环境:8.3 服务:8.0'
# shop_url = 'http://www.dianping.com/shop/9037892'
# 还有几个分店

# shop_id = '07'
# shop_name = '新发现(龙湖时代天街店)'
# address = '金沙湖CBD龙湖时代天街4楼'
# phone = '0571-87256661 0571-87256663'
# detail = '人均：56元 口味：8.0 环境：8.4 服务：8.1'
# shop_url = 'http://www.dianping.com/shop/15860205'
# 还有几个分店

# shop_id = '08'
# shop_name = '新白鹿餐厅(龙游路店)'
# address = '龙游路56号(近武林路鞋城)'
# phone = '0571-87922071'
# detail = '人均:54元 口味:8.0 环境:7.9 服务:7.8'
# shop_url = 'http://www.dianping.com/shop/536713'
# 还有分店

# shop_id = '09'
# shop_name = '老头儿油爆虾(武林店)'
# address = '戒坛寺巷25号万华武林商务大厦A座'
# phone = '0571-85151117'
# detail = '人均：70元 口味：8.8 环境：8.9 服务：8.7'
# shop_url = 'http://www.dianping.com/shop/8301189'

# shop_id = '10'
# shop_name = '新周记(鼓楼总店)'
# address = '鼓楼十五奎巷3号(近鼓楼城门)'
# phone = '0571-86070806'
# detail = '人均:67元 口味:8.6 环境:7.7 服务:7.7'
# shop_url = 'http://www.dianping.com/shop/2280109'

# shop_id = '11'
# shop_name = '楼外楼(孤山路店)'
# address = '孤山路30号(近平湖秋月)'
# phone = '0571-87969023 0571-87969682'
# detail = '人均：168元 口味：6.9 环境：7.4 服务：6.6'
# shop_url = 'http://www.dianping.com/shop/536375'

# shop_id = '12'
# shop_name = '粥皇港式餐厅(文晖店)'
# address = '湖墅南路118号文晖大厦3楼(近文晖路)'
# phone = '0571-88377987'
# detail = '人均：79元 口味：8.0 环境：8.0 服务：7.5'
# shop_url = 'http://www.dianping.com/shop/6052468'

# shop_id = '13'
# shop_name = '小杨生煎(杭州西湖银泰)'
# address = '延安路98号B1楼'
# phone = '0571-87002014'
# detail = '人均：23元 口味：7.9 环境：7.6 服务：7.8'
# shop_url = 'http://www.dianping.com/shop/21018359'

# shop_id = '14'
# shop_name = '秋叶小町(砂之船店)'
# address = '解放东路8号砂之船国际生活广场B1层，银心街47号'
# phone = '0571-87210769'
# detail = '人均：45元 口味：6.9 环境：7.1 服务：7.0'
# shop_url = 'http://www.dianping.com/shop/6208538'

# shop_id = '15'
# shop_name = '知味观·味庄(杨公堤店)'
# address = '杨公堤10-12号(近花港观鱼西门)'
# phone = '0571-87970568 0571-87971913'
# detail = '人均：145元 口味：7.9 环境：8.1 服务：7.3'
# shop_url = '0571-87970568 0571-87971913'

# shop_id = '16'
# shop_name = '张生记(万象城店)'
# address = '富春路701号(万象城6楼668号)'
# phone = '0571-89705917 0571-89705907'
# detail = '人均:170元 口味:8.2 环境:8.9 服务:7.9'
# shop_url = 'http://www.dianping.com/shop/4065061'

# shop_id = '17'
# shop_name = '胖哥俩肉蟹煲(天虹店)'
# address = '新塘路108号天虹购物中心B座5层'
# phone = '0571-89801234'
# detail = '人均：67元 口味：8.6 环境：8.5 服务：8.3'
# shop_url = 'http://www.dianping.com/shop/18607345'

shop_id = '18'
shop_name = ''
address = ''
phone = ''
detail = ''
shop_url = ''

data = {
    'shop_id': shop_id,
    'shop_name': shop_name,
    'address': address,
    'phone': phone,
    'detail': detail,
    'shop_url': shop_url
}
insert_data(data)
