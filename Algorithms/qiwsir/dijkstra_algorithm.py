# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
最短路径问题的Dijkstra算法
是由荷兰计算机科学家艾兹赫尔·戴克斯特拉提出。迪科斯彻算法使用了广度优先搜索解决非负权有向图的单源最短路径问题，
算法最终得到一个最短路径树。该算法常用于路由算法或者作为其他图算法的一个子模块。
"""


G = {1: {1: 0, 2: 1, 3: 12},
     2: {2: 0, 3: 9, 4: 3},

     3: {3: 0, 5: 5},

     4: {3: 4, 4: 0, 5: 13, 6: 15},

     5: {5: 0, 6: 4},

     6: {6: 0}}

k = {'a': 333, 'b': 432, 'c': 444443}


def Dijkstra(G, INF=999):
    """
    计算指定点v0到图G中任意点的最短路径的距离

    :param G:
    :param INF:为设定的无限远距离值
    :return:
    """

    # 用于存放已知最短距离的点
    book = set()
    # 最短距离
    dis = [G[1][i] if i in G[1].keys() else INF for i in range(1,len(G)+1)]



Dijkstra(G,999)
