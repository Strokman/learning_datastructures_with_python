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
                # self.append(arg)
                if isinstance(arg, Iterable):
                    for i in arg:
                        self.append(i)
                else:
                    self.append(arg)

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

    def pop_first(self):
        if self.head is not None:
            val = self.head.value
            self.head = self.head.next
            self.length -= 1
            return val

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def __repr__(self):
        lst = []
        temp = self.head
        while temp is not None:
            val = temp.value
            temp = temp.next
            lst.append(val)
        return f'{lst}'

    def __len__(self):
        return self.length

    def __iter__(self):
        temp = self.head
        while temp.next is not None:
            val = temp.value
            temp = temp.next
            yield val
