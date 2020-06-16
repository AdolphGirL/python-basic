# -*- coding: utf-8 -*-


def test_file_open():
    open_file = open('./data/file_test.txt', mode='r', encoding='UTF-8')

    # 逐行讀取全部資料
    for line in open_file.readlines():
        print(line)

    # 關閉串流
    open_file.close()


def test_file_seek():
    seek_file = open('./data/file_test.txt', mode='r', encoding='UTF-8')
    seek_file.seek(10)

    # 逐行讀取全部資料
    for line in seek_file.readlines():
        print(line)

    # 關閉串流
    seek_file.close()


# 開啟一個不存在的檔案，寫入
def test_file_writes():
    write_file = open('./data/file_write.txt', mode='w', encoding='UTF-8')
    write_file.write('this is write line\n')
    write_file.writelines('''
    this is writelines line\n
    this is writelines line\n
    this is writelines line\n
    \n
    ''')

    write_file.close()


if __name__ == '__main__':
    # test_file_open()
    # test_file_seek()
    test_file_writes()
