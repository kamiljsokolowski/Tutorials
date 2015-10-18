def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        print 'This is a palindrome'
    elif first(word) == last(word):
        is_palindrome(middle(word))
    else:
        print 'This is not a palindrome'

is_palindrome('noon')
is_palindrome('redivider')
is_palindrome('redimer')

