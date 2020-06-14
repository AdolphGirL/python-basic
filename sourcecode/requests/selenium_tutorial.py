# -*- coding: utf-8 -*-

from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
    driver.close()


def taiwan_high_speed_rail_search():
    url = 'http://www.thsrc.com.tw/tw/timetable/searchresult'
    ss = '左營站'
    es = '南港站'
    sd = '2020/06/17'
    st = '09:00'

    driver = webdriver.Chrome()
    driver.get(url)

    # 出發站
    driver.find_element_by_id('StartStation').send_keys(ss)
    # 到達站
    driver.find_element_by_id('EndStation').send_keys(es)
    # 出發日期
    driver.find_element_by_id('DepartueSearchDate').click()
    driver.find_element_by_id('DepartueSearchDate').send_keys(sd)
    # 出發時間
    driver.find_element_by_id('DepartueSearchTime').click()
    driver.find_element_by_id('DepartueSearchTime').send_keys(st)

    driver.find_element_by_id('SearchButton').click()


if __name__ == '__main__':
    # 寫在方法內執行完成式，瀏覽器就會被關閉
    # test()
    # taiwan_high_speed_rail_search()

    url = 'http://www.thsrc.com.tw/tw/timetable/searchresult'
    ss = '左營站'
    es = '南港站'
    sd = '2020/06/17'
    st = '09:00'

    driver = webdriver.Chrome()
    driver.get(url)

    # 出發站
    driver.find_element_by_id('StartStation').send_keys(ss)
    # 到達站
    driver.find_element_by_id('EndStation').send_keys(es)
    # 出發日期
    driver.find_element_by_id('DepartueSearchDate').click()
    driver.find_element_by_id('DepartueSearchDate').send_keys(sd)
    # 出發時間
    driver.find_element_by_id('DepartueSearchTime').click()
    driver.find_element_by_id('DepartueSearchTime').send_keys(st)

    driver.find_element_by_id('SearchButton').click()