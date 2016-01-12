from random import randint

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

num_of_students = 23
num_of_matches = 0.0
num_of_tests = 10000
for t in range(1, num_of_tests):
    if has_duplicates(gen_bday_list(num_of_students)):
        num_of_matches += 1

estimate = (num_of_matches / num_of_tests) * 100
print 'With', num_of_students, 'students in class, chances that two of them have the same birthday are', estimate, '%'

