from linked_list import LinkedList
from random import randint

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

