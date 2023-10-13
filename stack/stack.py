from node import Node


class Stack:

    def __init__(self, *args):
        self.top = None
        self.__height = 0
        for arg in args:
            self.push(arg)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.__height += 1

    def pop(self):
        if self.__height == 0:
            raise IndexError('Pop from empty stack')
        val = self.top
        self.top = self.top.next
        self.__height -= 1
        val.next = None
        return val

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f'{[i for i in self]}'

    def __iter__(self):
        temp = self.top
        while temp is not None:
            val = temp
            temp = temp.next
            yield val
