# -*- coding: utf-8 -*-
#Quick Python Script Explanation for Progeammers
#给程序员的超快速Py脚本解说
import os

def main():
    print 'Hello World!'
    print "这是Alice\'的问候."
    print '这是Bob\'的问候.'
    
    foo(5,10)
    
    print '='*10
    print '这将直接执行'+os.getcwd()
    
    counter = 0
    counter +=1
    
    food = ['苹果','香蕉','火龙果','桃子']
    for i in food:
        print '俺就爱吃:'+i
    
    print '数到10'
    for i in range(10):
        print i

def foo(param1,param2):
    res = param1+param2
    print  '%s 加 %s 等于 %s' % (param1,param2,param1+param2)
    if res < 50:
        print '小于50'
    elif (res>=50):
        print '大于等于50'
    else:
        print '不是数字'
    return res
    '''这是多
    行注释'''
if __name__=='__main__':
    main()
    