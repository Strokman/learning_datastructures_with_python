from linked_list.node import Node
from linked_list import LinkedList

def main():
    a = [1, 5, 9, 6]
    a = LinkedList(1, 7, 9, 12)
    head = a.head
    iter_over_ll(head)
    iter_over_ll(reverse(head))
    a.head = None
    print(a)


def list_to_ll(lst):
    pass


def iter_over_ll(node):
    temp = node
    while temp is not None:
        print(temp)
        temp = temp.next


def reverse(node):
    before = None
    temp = node
    after = temp.next
    while after is not None:
        after = temp.next
        temp.next = before
        before = temp
        temp = after
    return before


def reverse_recursion(node):
    temp = node
    after = node.next
    if after is None:
        return temp
    else:
        after = temp


if __name__ == '__main__':
    main()