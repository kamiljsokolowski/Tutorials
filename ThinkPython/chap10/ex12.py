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

def is_reverse(l, w):
    """
    Check if a reverse pair exists for a given word in a given list.
    """
#    if type(w) != str or type(r) != str:
#        print 'At least one of the arguments is not a string.'
#        return None
    i = bisect_left(l, w[::-1])
    if i != len(l) and l[i] == w[::-1]:
        return l[i]
    else:
        return None

if __name__ == '__main__':
    f = raw_input('filename: ')
    o = open(f)
    l = make_word_list(o)
    for w in l:
        if is_reverse(l, w):
            print (w, is_reverse(l, w))
    o.close()

