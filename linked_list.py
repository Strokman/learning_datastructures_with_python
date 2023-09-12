from functools import total_ordering
from collections.abc import Iterable

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value


@total_ordering
class LinkedList:

    def __init__(self, *args):
        self.length = 0
        self.head = None
        self.tail = None
        if args:
            for arg in args:
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

    def get(self, index):
        if 0 > index or index >= self.length:
            raise IndexError('List index ouf of range')
        counter = 0
        for i in self:
            if counter == index:
                return i
            counter += 1

    def find(self, value):
        index = 0
        for i in self:
            if i == value:
                return index, i
            index += 1

    def insert(self, index, value):
        if index > len(self) or index < 0:
            raise IndexError('List index ouf of range')
        if index == 0:
            self.prepend(value)
        elif index == len(self):
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def set(self, index, value):
        node = self.get(index)
        node.value = value

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        elif index == len(self):
            self.tail = self.get(index - 1)
        else:
            node = self.get(index - 1)
            node.next = node.next.next
        self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(len(self)):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def __repr__(self):
        return f'{[i for i in self]}'

    def __len__(self):
        return self.length

    def __iter__(self):
        temp = self.head
        while temp is not None:
            val = temp
            temp = temp.next
            yield val

    def __eq__(self, obj):
        if len(self) != len(obj):
            return False
        if isinstance(obj, LinkedList):
            for i in range(len(self)):
                if self.get(i) != obj.get(i):
                    return False
        if isinstance(obj, (list, tuple)):
            for i in range(len(self)):
                if self.get(i).value != obj[i]:
                    return False
        return True

    def __lt__(self, other):
        return list(self) < other
