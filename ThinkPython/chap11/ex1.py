f = raw_input('filename: ')

def make_word_dict(f):
    """
    Read the file f and, store each word as dictionary key.
    Values are not important.
    Return the dictioonary.
    """
    c = open(f)
    d = dict()
    i = 0
    for word in c:
        w = word.strip('\n\r')
        d[w] = i 
        i += 1
        #l.append(w)
    c.close()
    return d

print make_word_dict(f)

