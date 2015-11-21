file = raw_input('filename: ')
string = raw_input('Insert a string of forbidden characters: ')

def uses_all(w, s):
    """
    Check if each character specified in a string is used at least once.
    Return False if it does not
    """
    for c in s:
        if w.find(c) == -1:
            return False
    return True

f = open(file)

word_count = 0

for word in f:
    word = word.strip()
    if uses_all(word, string):
        word_count += 1
        print 'All characters in', string, 'are used at least once in word', word, '.'

print 'All characters in the string', string, 'are used at least once in', word_count, 'words.'

f.close()

