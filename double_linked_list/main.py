from double_ll import DoublyLinkedList


def main():
    a = DoublyLinkedList(1, 2, 4)
    a.append(2)
    a.append(10)
    a.append(12)
    print(a.pop())
    print(a)
    print(a.pop_first())
    print(a)
    print(len(a))
    b = DoublyLinkedList(100, 3, 5)
    print(b.pop_first())
    print(b)
    print(len(b))


if __name__ == '__main__':
    main()
