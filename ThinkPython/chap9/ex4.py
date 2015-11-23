file = raw_input('filename: ')
string = raw_input('Insert a string of available characters: ')

def uses_only(w, s):
    """
    Check if the word consists only of the characters specified in a string.
    Return False if it does not
    """
    for l in w:
        if s.find(l) == -1:
            return False
    return True

f = open(file)

for word in f:
    word = word.strip()
    if uses_only(word, string):
        print 'Word', word, 'consists only of characters specified in', string

f.close()

