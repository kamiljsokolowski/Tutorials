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

def rotate_word(s, n):
    """
    Rotate each char in a string by the given amount.
    Wrap around to the beginning (if necessary).
    """
    rotate = ''
    for c in s:
        start = ord('a')
        num = ord(c) - start
        r_num = (num + n) % 26 + start
        r_c = chr(r_num)
        rotate += r_c
    return rotate

if __name__ == '__main__':
    word_dict = make_word_dict(f)
    for k in word_dict:
        for i in range(1, 14):
            rot_k = rotate_word(k, i)
            if rot_k in word_dict:
                if not rot_k == k:
                    print k, 'and', rot_k, 'are a rotate pair'

