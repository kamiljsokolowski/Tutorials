file = raw_input('filename: ')
forbidden_str = raw_input('Insert a string of forbidden characters: ')

def avoids(w, s):
    """
    Check if the word contains any of the characters specified in a string.
    Return True if it does not
    """
    for l in w:
        for c in s:
            if c == l:
                return False
    return True

f = open(file)

words_that_avoid = 0

for word in f:
    if avoids(word, forbidden_str):
        words_that_avoid += 1
        print 'The word:', word, 'avoids any character from the specified string'

print 'Total number of words that avoid any characters from the specified string is:', words_that_avoid

f.close()

