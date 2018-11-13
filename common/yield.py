# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def yield_test(n):
    for i in range(n):
        yield call(i)
    print("do something.")

def call(i):
    return i*2

if __name__ =="__main__":
    f = yield_test(5)
    for i in f:
        print(i)

    # mygenerator = (x*x for x in range(3))
    # for i in mygenerator:
    #     print(i)

