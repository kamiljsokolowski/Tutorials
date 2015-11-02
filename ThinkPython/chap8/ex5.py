s = raw_input('string: ')
c = raw_input('char: ')

def count(s,c):
    """
    Return the number of times char l occures in a string.
    s and l variables must be of str type.
    """
#    if type(s) != str
#        return -1
#    if type(c) != str
#        return -1
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

print count(s,c)

