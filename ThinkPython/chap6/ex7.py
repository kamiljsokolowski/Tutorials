def is_power(a, b):
    if a % b == 0:
        if a / b == 1:
            print True
        elif a / b > 1:
            a = a / b
            is_power(a, b)
    else:
        print 'a is not the power of b'

is_power(8, 2)
is_power(27, 3)
is_power(64, 8)
is_power(16, 8)

