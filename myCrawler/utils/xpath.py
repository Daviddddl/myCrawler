from lxml import etree


html = open('../crawler_files/dianping_shop01.html', 'r')

selector = etree.HTML(html.read())
content = selector.xpath('//*[@class="desc"]/text()')
for each in content:
    print(each)