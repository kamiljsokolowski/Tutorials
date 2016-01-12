test1 = [1, 2, 2]
test2 = ['b', 'a']

def is_sorted(l):
    """
    Return True if a list is sorted in scending order.
    Return Flase if otherwise.
    """
    for i in range(1, len(l)):
        print l[i]
        print l[i - 1]
        if l[i] < l[i - 1]:
            return False
    return True

print is_sorted(test1)
print is_sorted(test2)

