def hist(s):
    """
    Count the number of times each char appears in a given string.
    Store chars as dict keys and number of appearencess as values.
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    """
    Print dictionaries keys and their values in alphabetical order
    """
    keys_list = h.keys()
    keys_list.sort()
    for c in keys_list:
        print c, h[c]

if __name__ == '__main__':
    test1 = 'brontosaurus'
    print test1
    print_hist(hist(test1))
    test2 = 'tyranosaurus'
    print test2
    print_hist(hist(test2))

