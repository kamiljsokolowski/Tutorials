test1 = [1, 2, 3]
test2 = [1, 2, 3, 4, 5, 6]
test3 = [1, 2, '3', 4, 5, 6]
test4 = ['a', 'b', 'c', 'd']

def middle(l):
    """
    Return a new list containing all but first and last element of a given list.
    """
    new_l = l[:]
    del new_l[::len(new_l)-1]
    return new_l

print middle(test1)
print middle(test2)
print middle(test3)
print middle(test4)

