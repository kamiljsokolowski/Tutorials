test1 = [1, 2, 2]
test2 = ['b', 'a']
test3 = ['b', 'a', 'a', 'c', 'd', 'e', 'f', 'd']

def remove_duplicates(l):
    """
    Remove any duplicates from the original list.
    Return a list without duplicates.
    """
    new_l = l[:]
    tmp_l = new_l[:]
    for e in l:
        tmp_l.remove(e)
        if e in tmp_l:
            new_l.remove(e)
    return new_l

print test1
print remove_duplicates(test1)
print test2
print remove_duplicates(test2)
print test3
print remove_duplicates(test3)

