import random

def sort_by_lenght(words):
    """
    (basic DSU example)
    1. Build a list of tuples with word lenght and a random number as sort keys
    2. (reverse) sort the list
    3. Extract the (now sorted) elements of the original sequence
    """
    l = []
    for w in words:
        l.append((len(w), random.random(), w))

    l.sort(reverse=True)

    res = []
    for lenght, number, word in l:
        res.append(word)
    return res

if __name__ == '__main__':
    tests = [['man', 'woman', 'child', 'orphan'], ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
    for test in tests:
        print sort_by_lenght(test)

