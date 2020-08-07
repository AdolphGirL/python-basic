# -*- coding: utf-8 -*-

import random
import time


def display_intro():
    print('''
    開始遊戲
    ''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('你要往左還是往右? (左(1) or 右(2))')
        cave = input()

    return cave


def check_cave(chosen_cave):
    print('已經選擇了方向...')
    time.sleep(2)
    print('嗯嗯嗯...')
    time.sleep(2)

    # 友善的方向
    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('給你個驚喜')
    else:
        print('老天保佑你')


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    caveNumber = choose_cave()
    check_cave(caveNumber)

    print('Do you want to play again? (yes or no)')
    play_again = input()
