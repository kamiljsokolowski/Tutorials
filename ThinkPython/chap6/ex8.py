def gcd(a, b):
    """
    Returns the greatest common divisor of a and b.
    GCD is the largest number that divides both numbers without a reminder.
    """
    print 'a = ', a
    print 'b = ', b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print gcd(48, 18)
print gcd(77, 49)

