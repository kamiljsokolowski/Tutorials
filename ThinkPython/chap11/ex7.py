STORE = {}

def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    try:
        return STORE[m, n]
    except KeyError:
        STORE[m, n] = ack(m - 1, ack(m, n - 1))
        return STORE[m, n]

if __name__ == '__main__':
    tests = {1:[3, 4], 2:[3,6]}
    for test in tests:
        print ack(tests[test][0], tests[test][1])

