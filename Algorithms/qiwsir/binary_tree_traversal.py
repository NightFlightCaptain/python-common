# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

from collections import namedtuple
from sys import stdout

Node = namedtuple('Node',['data','left','right'])
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7,None,None),
                      None),
                 Node(5,None,Node)),
            Node(3,
                 Node(6,
                      Node(8,None,None),
                      Node(9,None,None)),
                 None))

