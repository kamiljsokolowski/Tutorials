s = raw_input('string = ')

def traverse_back(s):
    i = len(s) - 1
    while i >= 0:
        print s[i]
        i -= 1

#traverse_back('john')
#traverse_back('carol')
#traverse_back('ann')
traverse_back(s)

