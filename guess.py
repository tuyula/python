#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
secret = random.randint(1,100)
guess = 0
tries = 0

print "AHOY! 我是埃罗坦机器人，我有一个秘密"
print "这个密码是数字1-99,我给你6次猜的机会"

while guess != secret and tries < 6:
    guess = input("快猜快猜?")
    if guess < secret:
	print "Too low,SB（帅比）狗!"
    elif guess > secret:
	print "Too high,旱鸭子!"
    elif guess == secret:
        print "wa! Good"
    tries = tries + 1
