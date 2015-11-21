file = raw_input('filename: ')

def is_abecedarian(w):
    """
    Check if all letters in a word appear in alphabetical order.
    Return False if otherwise.
    """
    l = len(w) - 1
    while l > 0:
        if w[l] < w[l-1]:
            return False
        l -= 1
    return True


f = open(file)

word_count = 0

for word in f:
    word = word.strip()
    if is_abecedarian(word):
        word_count += 1
        print 'All letters in word', word, 'appear in alphabetical order'

print 'All letters in appear in alphabetical order in', word_count, 'words.'

f.close()

