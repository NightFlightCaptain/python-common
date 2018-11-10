# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Node:
    def __init__(self, data):
        """
        节点结构
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

    def children_count(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    """
    查找节点，返回该节点和该节点的父节点
    """

    def lookup(self, data, parent=None):
        if data > self.data:
            if self.right:
                return self.right.lookup(data, self)
            else:
                return None, None
        elif data < self.data:
            if self.left:
                return self.left.lookup(data, self)
            else:
                return None, None
        else:
            return self, parent

    """
    删除节点，根据该节点有几个子节点来进行
    """

    def delete(self, data):
        node, parent = self.lookup(data)
        if node.children_count() == 0:
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
        elif node.children_count() == 1:
            if node.left:
                if parent.left == node:
                    parent.left = node.left
                    del node
                else:
                    parent.right = node.left
                    del node
            else:
                if parent.left == node:
                    parent.left = node.right
                    del node
                else:
                    parent.right = node.right
                    del node
        else:
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                node.right = successor.right
            del successor

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """
        二叉树数据结构
        """
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right

if __name__ == "__main__":
    head = Node(48)
    head.insert(49)
    head.insert(78)
    head.insert(4)
    head.insert(46)
    head.insert(23)
    head.insert(35)
    head.print_tree()
    head.delete(23)
    k = head.tree_data()
    print("___________________")
    for i in k:
        print(i)
