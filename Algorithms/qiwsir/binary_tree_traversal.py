# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

from collections import namedtuple
from queue import Queue
from sys import stdout

Node = namedtuple('Node',['data','left','right'])
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7,None,None),
                      None),
                 Node(5,None,None)),
            Node(3,
                 Node(6,
                      Node(8,None,None),
                      Node(9,None,None)),
                 None))


def preorder(node):
    if node is not None:
        print(node.data,end=",")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data,end=",")
        inorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=",")


def leverorder(node):
    mylist = Queue()

    if node is not None:
        mylist.put_nowait(node)
    while not mylist.empty():
        a = mylist.get()
        print(a.data,end=",")
        if a.left is not None:
            mylist.put(a.left)
        if a.right is not None:
            mylist.put(a.right)


# preorder(tree)
# print()
# inorder(tree)
# print()
# postorder(tree)
# print()
leverorder(tree)
print()




