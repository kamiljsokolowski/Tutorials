test1 = [1, 2, 3]
test2 = [1, 2, 3, 4, 5, 6]
test3 = [1, 2, '3', 4, 5, 6]

def cumulative_sum(l):
    """
    Return a cumulative sum, where the ith element is the sum of first i+1 elements of the original list.
    Check if list contains only integers.
    """
    new = []
    for e in l:
        if type(e) != int:
            return False
    for i in range(len(l)):
        new.append(sum(l[:i+1]))
    return new

print cumulative_sum(test1)
print cumulative_sum(test2)
print cumulative_sum(test3)

