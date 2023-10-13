from hash_table import HashTable
from time_counter import time_counter
import random

@time_counter
def main():
    # hash = HashTable(100)
    # hash.set_item('krokozyabrik', [1, 2, 3])
    # print(hash)
    a = HashTable(10000)
    a.set_item('bolts', 5000)
    a.set_item('sickles', 1000)
    a.set_item('catafracts', 1000)
    a.set_item('smth', 1000)
    a.set_item('bolts', 1)
    a.set_item(0.8, 100)
    for i in range(random.randint(10000, 20000)):
        a.set_item(random.randint(123, 10000), random.randint(1, 100000))
    print(a.get(3233))
    # print(a.get('bolts'))
    # print(a.keys())
    # print(a)
    # b = HashTable()
    # print('bolts' in b)


@time_counter
def dict_comparator(list1, list2):
    compars = {}
    for i in list1:
        compars[i] = True
    for k in list2:
        if k in compars:
            return True


@time_counter
def set_comparator(list1, list2):
    return bool(set(list1) & set(list2))


if __name__ == '__main__':
    list1 = [1, 2, 5]
    list2 = [3, 4, 5]
    print(dict_comparator(list1, list2))
    print(set_comparator(list1, list2))

    main()
