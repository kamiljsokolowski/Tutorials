file = raw_input('filename: ')

def double_times_3(w):
    """
    Check if two three consecutive double characters are present.
    Return False if otherwise.
    """
    l = 0

    if len(w) < 6:
        return False

    while l < len(w) - 5:
        if w[l] == w[l+1]:
            if w[l+2] == w[l+3]:
                if w[l+4] == w[l+5]:
                    return True
        l += 1
    return False

f = open(file)

word_count = 0

for word in f:
    word = word.strip()
    if double_times_3(word):
        word_count += 1
        print 'The word', word, 'has three consecutive double letters'

print 'Three consecutive double letters are present in', word_count, 'words.'

f.close()

