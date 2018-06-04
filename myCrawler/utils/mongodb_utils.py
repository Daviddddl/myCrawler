import pymongo

connection = pymongo.MongoClient(host='123.206.70.190', port=27017)
tdb = connection.dinning_menu
post_info = tdb.comments


def insert_data(data):
    post_info.insert(data)


def remove_data(data):
    post_info.remove(data)


# test02 = {'name': '我就试试', 'age': 345, 'skills': ['吃饭', '睡觉', '打飞机']}
# # test03 = {'change': '我要change了！'}
# #
# post_info.insert(test02)
# #
# # post_info.insert(test03)
#
# # post_info.remove({'name': '我就试试'})

# print("mongodb数据库操作完成！")
