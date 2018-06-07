from lxml import etree


html = open('../htmls/ques_res.html', 'r')
selector = etree.HTML(html.read())
root_path = selector.xpath('//*[@id="viewport"]/div/div/div[4]')
test = selector.xpath('//*[@id="13161"]/div[1]/div[2]/a/div')
print(test)
for each_root in root_path:
    ques_list = each_root.xpath('./div[1]/span/text()')
    for each_ques in ques_list:
        print(each_ques)



        # with open('../crawler_files/dianping_shop'+nowTime+'.html', 'w') as f:
        #     f.write(res_url)
        #     f.write('\n\n')
        #     f.write(response.text)

        # print(response.text.encode('utf-8').decode('unicode_escape'))

        # print(response.text)