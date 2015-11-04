s1 = raw_input('first string: ')
s2 = raw_input('second string: ')

def is_reverse(s1, s2):
    """
    Compare two strings and return True if one is the reverse of the other.
    """
    if len(s1) != len(s2):
        return false

    i = 0
    j = len(s2) - 1

    while j >= 0:
        if s1[i] != s2[j]:
           return false
        i += 1
        j -= 1

    return True

print is_reverse(s1, s2)

