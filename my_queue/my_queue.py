from node import Node


class Queue:

    def __init__(self, *args):
        self.__length = 0
        self.first = None
        self.last = None
        if args:
            for arg in args:
                self.enqueue(arg)

    def enqueue(self, value):
        new_node = Node(value)
        if self.__length == 0:
            self.last = self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.__length += 1

    def dequeue(self):
        if self.__length == 0:
            raise IndexError('Dequeue from empty queue')
        val = self.first
        if self.__length == 1:
            self.first = None
        else:
            self.first = self.first.next
            val.next = None
        self.__length -= 1
        return val

    def __len__(self):
        return self.__length

    def __repr__(self):
        return f'{[i for i in self]}'

    def __iter__(self):
        temp = self.first
        while temp is not None:
            val = temp
            temp = temp.next
            yield val
