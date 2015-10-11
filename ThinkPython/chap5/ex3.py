print 'a**n + b**n == c**n'
raw_a = raw_input('a = ...\n') 
raw_b = raw_input('b = ...\n') 
raw_c = raw_input('c = ...\n') 
raw_n = raw_input('n = ...\n') 
a = int(raw_a)
b = int(raw_b)
c = int(raw_c)
n = int(raw_n)

def check_fermat(a, b, c, n):
    if (n > 2 and (a**n + b**n == c**n)):
        print 'Holy smokes, Fermat was wrong!'
    elif n <= 2 and (a**n + b**n == c**n):
        print 'n is less or equal 2, Fermat is still on top!'
    else:
        print "No, that doesn't work"

#check_fermat(1, 2, 3, 1)
#check_fermat(3, 4, 5, 2)
check_fermat(a, b, c, n)

