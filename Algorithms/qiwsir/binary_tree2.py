# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


class CNode:
    left,right,data = None,None,0

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


class CBOrdTree:
    def __init__(self):
        self.root = None

    def add_node(self,data):
        return CNode(data)

    def insert(self,root,data):
        if root is None:
            return self.add_node(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
            return root

    def lookup(self,root,target):
        if root is None:
            return False
        else:
            if target == root.data:
                return True
            elif target<root.data:
                return self.lookup(root.left,target)
            else:return self.lookup(root.right,target)

    def min_value(self,root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root.data

    def max_depth(self,root):
        if root is None:
            return 0
        return max(self.max_depth(root.left),self.max_depth(root.right))+1

    def size(self,root):
        if root is None:
            return 0
        return self.size(root.left)+self.size(root.right)+1

    def print_tree(self,root):
        if root is None:
            return None
        if root.left:
            self.print_tree(root.left)
        print(root.data,end=",")
        if root.right:
            self.print_tree(root.right)


if __name__ == "__main__":
    tree = CBOrdTree()
    root = tree.add_node(5)
    tree.insert(root,78)
    tree.insert(root,12)
    tree.insert(root,7)
    tree.insert(root,1)
    tree.print_tree(root)
    print("\nmax_depth",tree.max_depth(root))
    print("min_value",tree.min_value(root))
    print("lookup7",tree.lookup(root,7))
    print("lookup77",tree.lookup(root,77))
    print("size",tree.size(root))

    # for i in range(5):
    #     data = int(input("insert the node value is %d")%i)
    #     tree.insert(data)
