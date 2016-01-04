test1 = [1, 2, 3]
test2 = [1, 2, 3, 4, 5, 6]
test3 = [1, 2, '3', 4, 5, 6]
test4 = ['a', 'b', 'c', 'd']

def middle(l):
    """
    Modify the list by choping first and last elements of a list.
    Return None.
    """
    del l[::len(l)-1]

print middle(test1)
print test1
print middle(test2)
print test2
print middle(test3)
print test3
print middle(test4)
print test4

