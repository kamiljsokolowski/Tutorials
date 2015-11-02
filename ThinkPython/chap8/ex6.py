s = raw_input('string: ')
c = raw_input('char: ')
n = raw_input('begin at: ')

def count(s,c,n):
    """
    Return the number of times char c occures in a string.
    Start the count at n-th char.
    s and c variables must be of str type while n must be of type int.
    """
    count = 0
    i = int(n)
#    if type(s) != str
#        return -1
#    if type(c) != str
#        return -1
    if i > len(s):
        print 'Counting in the void.. only Sith deals in absolutes'
        return -1
    while i < len(s):
        if s[i] == c:
            count += 1
        i += 1
    return count


print count(s,c,n)

