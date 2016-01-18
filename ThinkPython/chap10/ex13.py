from bisect import bisect_left

def make_word_list(f):
    """
    Read the file f and, using append() method, append each word as new list element.
    Return a sorted list.
    """
    l = []
    for word in f:
        w = word.strip('\n\r')
        l.append(w)
    return l

def has_interlock(l, w):
    """
    Traverse the given list in search of given word' interlock pair.
    If found, return the pair.
    If not found, return None.
    """
    interlocks = []
    for e in l:
        new_w = ''
        if len(e) == len(w):
            for j in range (0, len(w)):
                new_w = new_w + (w[j]+e[j]) 
        i = bisect_left(l, new_w)
        if i != len(l) and l[i] == new_w:
            interlocks.append(e)
    return interlocks

if __name__ == '__main__':
    f = raw_input('filename: ')
    o = open(f)
    l = make_word_list(o)
    for w in l:
        if has_interlock(l, w):
            print (w, has_interlock(l, w))
    o.close()

