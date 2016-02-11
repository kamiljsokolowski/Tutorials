from pronounce import read_dictionary

def make_word_dict(f='words.txt'):
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

def if_homophone(a, b, p):
    """
    Return True if words a and b have the same pronounciation.
    """
    if (a in p) and (b in p):
        if p[a] == p[b]:
            return True


if __name__ == '__main__':
    d = make_word_dict()
    p = read_dictionary()
    for w in d:
        h1 = w[1:]
        h2 = w[0] + w[2:]
        if (h1 in d) and (h2 in d):
            if if_homophone(w, h1, p) and if_homophone(w, h2, p):
                print 'Word', w, ' solves the homophone Puzzler'

