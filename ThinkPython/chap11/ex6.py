from time import time

STORE = {0:0, 1:1}

def old_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return old_fib(n-1) + old_fib(n-2)

def new_fib(n):
    if n in STORE:
        return STORE[n]
    else:
        res = new_fib(n-1) + new_fib(n-2)
        STORE[n] = res
        return res

def exec_time(f,a):
    start = time()
    f(a)
    elapsed = time() - start
    return elapsed

if __name__ == '__main__':
    tests = [1,2,3,10,20,50]
    for test in tests:
        print 'For n =', test,':'
        print '    When using old_fib() method, Fibonacci string is created in:', exec_time(old_fib, test)
        print '    When using new_fib() method, Fibonacci string is created in:', exec_time(new_fib, test)

