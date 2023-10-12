from functools import total_ordering


@total_ordering
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.value < other.value
        return False


# @total_ordering
class DoublyLinkedList:

    def __init__(self, *args):
        self.__length = 0
        self.head = None
        self.tail = None

        for arg in args:
            self.append(arg)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.__length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.__length += 1

    def pop(self):
        if self.__length == 0:
            raise IndexError('pop from empty list')
        temp = self.tail
        if self.__length == 1:
            self.tail = self.head = None
            return temp
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.__length -= 1
        return temp

    def pop_first(self):
        if self.__length == 0:
            raise IndexError('pop from empty list')
        temp = self.head
        if self.__length == 1:
            self.head = self.tail = None
        elif self.head is not None:
            self.head = self.head.next
            self.head.prev = None
        self.__length -= 1
        return temp

    def __len__(self):
        return self.__length

    def __iter__(self):
        temp = self.head
        while temp is not None:
            value = temp
            temp = temp.next
            yield value

    def __repr__(self):
        return f'{[i for i in self]}'
