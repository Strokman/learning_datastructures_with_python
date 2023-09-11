from linked_list import LinkedList

# lst = LinkedList(1, 2, [1, 2, 3])
# lst.append([2, 2, 2])
# lst.pop()
# lst.pop_first()
# print(lst)

# lst = LinkedList(1)
# print(lst.length)
# print(lst.pop_first())
# print(lst)
# print(lst.length)




from random import randint

lst = LinkedList([randint(1, 200) for i in range(10)])

for i in range(len(lst)):
    print(i)
    lst.append(i)

print(lst)
print(len(lst))
