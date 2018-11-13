# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
问题：
以人民币的硬币为例，假设硬币数量足够多。要求将一定数额的钱兑换成硬币。要求兑换硬币数量最少。
思路说明：
这是用贪婪算法的典型应用。在本例中用python来实现，主要思想是将货币金额除以某硬币单位，然后去整数，即为该硬币的个数；余数则做为向下循环计算的货币金额。
这个算法的问题在于，得出来的结果不一定是最优结果。比如，硬币单位是[1,4,6],如果将8兑换成硬币，按照硬币数量最少原则，应该兑换成为两个4（单位）的硬币，
但是，按照本算法，得到的结果是一个6单位和两个1单位的硬币。这也是本算法的局限所在。所谓贪婪算法，本质就是只要找出一个结果，不考虑以后会怎么样。
"""


def coin_change_dynamic(money):
    coins = [1, 2, 5, 10, 20, 50, 100]

    c = [[money for i in range(money+1)] for j in range(len(coins))]
    c[0] = [i for i in range(money+1)]
    for i in c:
        i[0] = 0
    print(c)
    # for i in range(1,money+1):
    #     for j in range(1,len(coins)):
    #         if i >=coins[j]:
    #             c[j][i] = min(c[j-1][i],c[j][i-coins[j]]+1)
    #         else:
    #             c[j][i] = c[j-1][i]
    for i in range(1,len(coins)):
        for j in range(1,money+1):
            if j >= coins[i]:
                c[i][j] = min(c[i-1][j],c[i][j-coins[i]]+1)
            else:
                c[i][j]=c[i-1][j]


    for i in c:
        for j in i:
            print("%3d"%(j),end=",")
        print()

coin_change_dynamic(342)