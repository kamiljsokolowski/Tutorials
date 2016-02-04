from random import randint
from time import time

def has_duplicates(l):
    """
    Return True if any list element appears more then once.
    Return Flase if otherwise.
    """
    for e in l:
        tmp_l = l[:]
        tmp_l.remove(e)
        if e in tmp_l:
            return True
    return False

def has_duplicates_new(l):
    """
    Return True if any list element appears more then once.
    Return Flase if otherwise.
    """
    d = {}
    for e in l:
        d[e] = d.get(e, 0) + 1
        if d[e] > 1:
            return True
    return False

def gen_bday_list(n):
    """
    Return a list of n randomly generated birthdays.
    Birthdays are appended to the list as strings in DD.MM format.
    """
    l = []
    for i in range(0, n-1):
        d = randint(1,31)
        m = randint(1,12)
        e = str(d) + '.' + str(m)
        l.append(e)
    return l

def exec_time(f,a):
    """
    check execution time for a single-arg function.
    """
    start = time()
    f(a)
    elapsed = time() - start
    return elapsed


if __name__ == '__main__':
    num_of_students = 23
    bday_list = gen_bday_list(num_of_students)
    elapsed_old = exec_time(has_duplicates, bday_list)
    elapsed_new = exec_time(has_duplicates_new, bday_list)

    print 'Old function implementation executed in', elapsed_old, 'seconds'
    print 'New function implementation (with a dict) executed in', elapsed_new, 'seconds'

