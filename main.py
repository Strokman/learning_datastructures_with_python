from linked_list import LinkedList, Node
from random import randint

a = Node(2)
print(a == 3)

test_list = list(range(1, 11))
random_list = [randint(1, 100) for i in range(100)]

first_ll = LinkedList(*test_list)
second_ll = LinkedList(*test_list)
assert first_ll == second_ll
for i in range(len(test_list)):
    assert first_ll.get(i).value == test_list[i]
    assert second_ll.get(i).value == test_list[i]

random_ll = LinkedList(*random_list)
for i in range(len(random_ll)):
    assert random_ll.get(i).value == random_list[i]

assert random_ll.reverse() == random_list.reverse()

less_ll = LinkedList(0, 1, 2, 3, 4, 5)
half_ll = LinkedList(1, 2, 3, 4, 5)
gt_ll = LinkedList(*list(range(2, 12)))
lt_ll = LinkedList(*list(range(0, 10)))
assert first_ll > less_ll
assert first_ll != less_ll
assert first_ll < gt_ll
assert first_ll > lt_ll

assert first_ll != {i: 1 for i in range(10)}

