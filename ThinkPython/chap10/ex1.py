test1 = [[1,2,3],[4,5],[6,7]]
test2 = [[1,2,3],['a','b'],[6,7]]

def nested_sum(l):
    """
    Add up all elements from all nested lists
    """
    total = 0
    for i in l:
        chunk = 0
        for e in i:
            if type(e) != int:
                return False
            chunk += e
        total += chunk
    return total

print nested_sum(test1)
print nested_sum(test2)
