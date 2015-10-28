s = raw_input('String is ')
l = raw_input('Letter to search for is ')
b = raw_input('Start the search at (index) ')

def find(s, l, b):
    """
    Search the string for a given char and return the index where that char appears.
    Start the search at certain index.
    """
    begin = int(b)
    if begin > len(s):
        print 'That search is beyond us'
        return -1
    i = begin
    while i < len(s):
        if l == s[i]:
            print 'Found it at', i
            return i
        else:
            print i ,'is not what You are looking for'
        i += 1
    return -1

find(s, l, b)

