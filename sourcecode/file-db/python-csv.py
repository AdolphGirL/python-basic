# -*- coding: utf-8 -*-

import os
import csv


def base_load(file_path):
    """
    基本讀取csv檔案，newline，確保換行符號可以正確解析
    :param file_path:
    :return:
    """
    with open(file_path, newline='') as csv_file:
        rows = csv.reader(csv_file)
        print(type(rows))
        if rows:
            for row in rows:
                print(row)
        else:
            print('none')


def base_load_with_split(file_path):
    """
    基本讀取csv檔案，指定分隔符號
    :param file_path:
    :return:
    """
    with open(file_path, newline='') as csv_file:
        rows = csv.reader(csv_file, delimiter=':')
        if rows:
            for row in rows:
                print(row)
        else:
            print('none')


def base_load_to_dict(file_path):
    """
    讀取成字典格式
    :param file_path:
    :return:
    """
    with open(file_path, newline='') as csv_file:
        rows = csv.DictReader(csv_file)
        if rows:
            for row in rows:
                print(row)
        else:
            print('none')


def base_write_csv(file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['姓名', '身高', '體重'])
        writer.writerow(['令狐沖', 175, 60])
        writer.writerow(['岳靈珊', 165, 57])


def dict_write_csv(file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        field_names = ['姓名', '身高', '體重']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # 寫入field_names
        writer.writeheader()

        # 寫入每筆資料
        writer.writerow({'姓名': '令狐沖', '身高': 175, '體重': 60})
        writer.writerow({'姓名': '岳靈珊', '身高': 165, '體重': 57})


if __name__ == '__main__':
    # 當前完整路徑
    # cwd = os.getcwd()

    cwd = os.curdir + os.sep + 'files'
    # test_file_path = os.path.join(cwd, 'iris.csv')
    # base_load(test_file_path)

    # test_file_path = os.path.join(cwd, 'passwd.csv')
    # base_load_with_split(test_file_path)

    # test_file_path = os.path.join(cwd, 'iris.csv')
    # base_load_to_dict(test_file_path)

    # 寫入基本csv
    test_file_path = os.path.join(cwd, 'out_test.csv')
    base_write_csv(test_file_path)

    # dict to csv
    test_file_path = os.path.join(cwd, 'out_test.csv')

