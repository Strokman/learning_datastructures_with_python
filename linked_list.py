from collections.abc import Iterable


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, *args):
        self.length = 0
        self.head = None
        self.tail = None
        if args:
            for arg in args:
                if isinstance(arg, Iterable):
                    for i in arg:
                        self.append(i)
                else:
                    self.append(arg)

    def print_list(self):
        if self.head is None:
            return ''
        temp = self.head
        lst = []
        while temp is not None:
            val = temp.value
            temp = temp.next
            lst.append(val)
        return lst

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        node = temp.value
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return node
