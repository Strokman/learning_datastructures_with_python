from node import Node
import random
from my_queue import Queue
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
            # if temp is None:
            #     temp = new_node
            #     return
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

    def bfs(self):
        current_node = self.root
        queue = Queue()
        queue.enqueue(current_node)
        result = []
        while len(queue) > 0:
            current_node = queue.dequeue().value
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)
            result.append(current_node.value)
        return result

    def dfs_pre_order(self):
        first_node = self.root
        results = []

        def traverse(node):
            results.append(node)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)

        traverse(first_node)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node)
        traverse(self.root)
        return results

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

    # recursive approach
    def search(self, value, temp=None):
        if temp is None:
            temp = self.root
        elif temp is None:
            return False
        if value == temp.value:
            return True
        else:
            if value > temp.value:
                return self.search(value, temp.right)
            else:
                return self.search(value, temp.left)
