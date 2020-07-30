# -*- coding: utf-8 -*-

"""
猜數字
"""
import random

guessTaken = 0

print('Hello，請輸入你的名字')
name = input()

number = random.randint(1, 20)
print('well，' + name + '，開始遊戲吧')

for guessTaken in range(6):
    print('請猜數字: ')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('你猜得太低了')

    if guess > number:
        print('你猜得太高了')

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('恭喜，' + name + '，你第' + guessTaken + '次就猜對了')

if guess != number:
    number = str(number)
    print('太可惜，' + name + '，正確數字是: ' + number)
