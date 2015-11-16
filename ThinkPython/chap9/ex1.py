file = raw_input('filename: ')

f = open(file)
for word in f:
    if len(word.strip()) > 20:
        print word

f.close

