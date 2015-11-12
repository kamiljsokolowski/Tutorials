def is_palindrome(word):
    """
    Check if a given string is a palindrome
    """
    if word[::1] == word[::-1]:
        print 'The string', word, 'is a palindrome'
    else:
        print 'The string', word, 'is not a palindrome'

is_palindrome('noon')
is_palindrome('redivider')
is_palindrome('redimer')

