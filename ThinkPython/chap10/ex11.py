from bisect import bisect_left

f = raw_input('filename: ')
word = raw_input('word: ')

def make_word_list(f):
    """
    Read the file f and, using append() method, append each word as new list element.
    Return a sorted list.
    """
    c = open(f)
    l = []
    for word in c:
        w = word.strip('\n\r')
        l.append(w)
    c.close()
    return l

def bisect(l, w):
    """
    Perform a bisection search for word w on list l.
    Return the index at which the word was found.
    Return None if the word was not found.
    """
# original solution - FAIL
#    i = len(l) / 2
#    print i
#    if l[i] == w:
#        return i
#    elif w < l[i]: 
#        return i + bisect(l[:i], w)
#    elif w > l[i]: 
#        print i + bisect(l[i:], w)
#        return i + bisect(l[i:], w)
#    else:
#        return None
# proposed solution
    i = bisect_left(l, w)
    if i != len(l) and l[i] == w:
        return i
    else:
        return None

if bisect(make_word_list(f), word) == None:
    print 'The word', word, 'was not found'
else:
    print 'The word', word, 'was found at', bisect(make_word_list(f), word), 'index'

