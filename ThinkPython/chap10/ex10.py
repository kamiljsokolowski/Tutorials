from time import time

file = raw_input('filename: ')

# ...

f = open(file)

def use_append(f):
    """
    Read the file f and, using append() method, append each word as new list element.
    """
    l = []
    for word in f:
        w = word.strip('\n\r')
        l.append(w)
    return l

def use_aug_assign(f):
    """
    Read the file f and, using augumented assignment idiom, append each word as new list element.
    """
    l = []
    for word in f:
        w = word.strip('\n\r')
        l = l + [w]
    return l

def exec_time(f,a):
    start = time()
    f(a)
    elapsed = time() - start
    return elapsed

print 'When using append() method, list is created in ', exec_time(use_append, f)
print 'When using augumented assignment, list is created in ', exec_time(use_aug_assign, f)

f.close()

