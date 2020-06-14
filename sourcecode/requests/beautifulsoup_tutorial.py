# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


html = '''
<html>
    <head>
        <meta charset="UTF-8">
        <title>i am title</title>
    </head>
    <body>
        <p id="p1">我是段落一</p>
        <p id="p2" class="red">我是段落二</p>
    </body>
</html>
'''


def taiwan_lottery():
    """
    威力彩號碼
    :return: none
    """
    lottery_url = 'https://www.taiwanlottery.com.tw/'
    lottery_html = requests.get(lottery_url)
    if lottery_html.status_code == 200:
        # print(lottery_html.text)

        # 取出威力彩透區塊資料
        sp = BeautifulSoup(lottery_html.text, 'html.parser')
        data = sp.find('div', class_='contents_box02')
        # 取出期數，消除html標籤
        title = data.find('span', class_='font_black15').text
        print('威力彩期數: '.format(title))

        # 開獎號碼
        nums = data.find_all('div', 'ball_tx ball_green')
        if nums:
            print('開出順序: ', end=' ')
            for i in range(0, 6):
                print(nums[i].text, end=' ')
            print()

            print('大小順序: ', end=' ')
            for i in range(6, 12):
                print(nums[i].text, end=' ')
            print()
        else:
            print('none data')

if __name__ == '__main__':
    # sp = BeautifulSoup(html, 'html.parser')
    # print(sp.text)
    #
    # datas = sp.select("p")
    # if datas:
    #     for item in datas:
    #         print(item.get("id"))
    #         print(item["id"])
    taiwan_lottery()
