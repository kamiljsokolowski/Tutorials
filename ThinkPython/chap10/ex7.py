a1 = 'mary'
b1 = 'army'
a2 = 'mary'
b2 = 'mark'

def is_anagram(a, b):
    """
    Return True if words a and b are anagrams.
    Return Flase if otherwise.
    """
    a_list = list(a)
    b_list = list(b)
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        return True
    else:
        return False

print is_anagram(a1, b1)
print is_anagram(a2, b2)

