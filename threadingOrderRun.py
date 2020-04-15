#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
import time


def showName(name):
    nowTime = time.strftime('%H:%M:%S',time.localtime())
    print('my name is function-%s,now %s ' %(name, nowTime))
    time.sleep(2)


if __name__ == '__main__':
    for i in range(20):
        showName(i)
"""

import time
import threading


def showName(threadNum, name):
    nowTime = time.strftime('%H:%M:%S',time.localtime(time.time()))
    print('i am thread-%d, my name is function-%s, now time is %s ' %(threadNum, name, nowTime))
    time.sleep(1)


if __name__ == '__main__':
    print('I am main ...')
    names = list(range(20))
    threadNum = 1 #threadNum 指线程执行的批次
    threadpool = [] #线程池
    while names:
       for i in range(6):
           try:
               name = names.pop()
           except IndexError as e:
               print('The list is empty')
               break
           else:
               t = threading.Thread(target=showName, args=(i,name,))
           threadpool.append(t)
           t.start()

       while threadpool:
            t = threadpool.pop()
            t.join()

       threadNum += 1
    print("main is over")
