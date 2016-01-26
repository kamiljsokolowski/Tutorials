def hist(s):
    """
    Count the number of times each char appears in a given string.
    Store chars as dict keys and number of appearencess as values.
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def reverse_lookup(d, v):
    """
    Reverse lookup all corresponding keys of a given value.
    Return a lisy containing all the keys.
    Raise and exception if the list is empty.
    """
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    if l == []:
        raise ValueError
    else:
        return l

if __name__ == '__main__':
    tests = ['brontosaurus']
    test_args = [1, 2, 4]
    for test in tests:
        print hist(test)
        for arg in test_args:
            print reverse_lookup(hist(test), arg)

