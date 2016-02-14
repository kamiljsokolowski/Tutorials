def sumall(*args):
    """
    Take any number of arguments and return their sum
    """
    sumall = 0
    sumall = sum(args[0], *args[1:])
    return sumall

if __name__ == '__main__':
    tests = [[1, 2, 3], [1, 2, 3, 4, 5, 6]]
    for test in tests:
        print sumall(test)

