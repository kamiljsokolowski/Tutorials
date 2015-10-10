def print_string(s):
    print s

def do_n(f, s, n):
    if n <= 0:
        print 'done!'
    else:
        f(s)
        do_n(f, s, n-1)

do_n(print_string, 'Hello', 2)
do_n(print_string, 'Nana', 4)
do_n(print_string, 'Dada', 8)

