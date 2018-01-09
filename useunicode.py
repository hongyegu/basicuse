#! /usr/bin/env python
#-*-coding:utf-8-*-

def funobj(n):
    '''
    :param n:
    :return n:
    '''
    return 1 if n < 2 else n * funobj(n-1)
if __name__ == '__main__':
    s = 'cafe'
    print(len(s))
    print(s.encode('utf-8'))
