def hist(s):
    """
    Count the number of times each char appears in a given string.
    Store chars as dict keys and number of appearencess as values.
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def invert_dict(d):
    """
    Invert a dictionary by mapping values to keys.
    If the val:key pair exists, then val maps to a list of keys.
    Return a new dictionary containing val:key pairs.
    """
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
#        if val in inverse:
#            inverse[val].append(key)
#        else:
#            inverse[val] = [key]
    return inverse

if __name__ == '__main__':
    tests = ['brontosaurus']
    for test in tests:
        print hist(test)
        print invert_dict(hist(test))

