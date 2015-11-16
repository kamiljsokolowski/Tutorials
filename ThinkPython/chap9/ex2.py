file = raw_input('filename: ')

def has_no_e(w):
    """
    Check if 'e' char is present in a given string.
    Return True is it is not or Flalse otherwise.
    """
    for l in w:
        if l == 'e':
            return False
    return True

f = open(file)

total_words = 0.0
no_e_words = 0.0

for word in f:
    total_words += 1
    if has_no_e(word) == True:
        print word
        no_e_words += 1

print "procentage of words in the list that have no 'e' is: ", int((no_e_words / total_words) * 100), "%"

f.close()

