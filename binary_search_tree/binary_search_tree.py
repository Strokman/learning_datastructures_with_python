from node import Node
import random

import sys


class BinarySearchTree:

    def __init__(self, *args):
        self.root = None
        for arg in args:
            self.insert(arg)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp is None:
                temp = new_node
                return
            if new_node == temp:
                return False
            if new_node > temp:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right
            if new_node < temp:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left

    def lookup(self, value):
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False


# lst = [random.randint(1000000, 10000000000) for i in range(10000)]
# b = BinarySearchTree(1, 8, 9)
# print(b.lookup(9))
a = BinarySearchTree(1, 5, 9)
print(a.lookup(1))
print(a.lookup(11))
# @time_counter
# def bst_search(bst, value):
#     return bst.lookup(value)
#
# @time_counter
# def index_search(lst: list, value):
#     for i in range(len(lst)):
#         if lst[i] == value:
#             return i
#     return False
#
# val = lst[100000 - 1]
#
# print(bst_search(a, val))

# print(index_search(lst, val))