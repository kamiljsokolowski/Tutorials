s = raw_input('string: ')
rotate = raw_input('rotate by: ')
r = int(rotate)

def rotate_word(s, r):
    """
    Rotate each char in a string by through the alphabet by the given amount.
    Wrap around to the beginning (if necessary).
    """
    r_s = ''
    for c in s:
        num = ord(c)
        r_num = num + r
        r_c = chr(r_num)
        r_s += r_c
    return r_s

print rotate_word(s, r)

