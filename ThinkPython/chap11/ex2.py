def hist(s):
    """
    Count the number of times each char appears in a given string.
    Store chars as dict keys and number of appearencess as values.
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

if __name__ == '__main__':
    print hist('brontosaurus')
    print hist('tyranosaurus')

