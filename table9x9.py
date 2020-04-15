#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class PrintTable:
    def __init__(self):
        print('开始打印9x9乘法表')
        self.print99()

    def print99(self):
        for i in range(1, 10):
            for j in range(1,i+1):
                print('%dx%d=%2s' %(j, i, j*i),end=' ')
            print('\n')


if __name__ == '__main__':
    pt = PrintTable()
