def is_palindrome(d, start, len):
    """
    Return true if digits in int d form a palindrome, when starting at [start] index and checking [len] digits.
    """
    s = str(d)[start:start+len]
    return s[::-1] == s

d = 100000

while d <= 999997:
    if (is_palindrome(d, 2, 4) and
        is_palindrome(d+1, 1, 5) and
        is_palindrome(d+2, 1, 4) and
        is_palindrome(d+3, 0, 6)):
        print 'The odometer reading', d, 'satisfies the puzzler.'
    d += 1

