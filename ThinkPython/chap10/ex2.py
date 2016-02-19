test1 = [['John','merry','alan'],['dwight','Bill'],['monica','sarah','Jerry','Samuel']]
test2 = [['John','merry','alan'],['d','Bill'],['monica','sarah','J','Samuel']]
test3 = [['John','merry','alan'],['dwight','2'],['monica','sarah','Jerry','Samuel']]
test4 = [['John','merry','alan'],['dwight',2],['monica','sarah','Jerry','Samuel']]

def capitalize_all(l):
#    res = []
#    for s in l:
#        if type(s) != str:
#                return False
#        res.append(s.capitalize())
    res = [s.capitalize() for s in l if type(s) == str]    
    return res

def capitalize_nested(n):
    """
    Capitalizie all elements from all nested lists
    """
#    res = []
#    for l in n:
#        res.append(capitalize_all(l))
#        if not capitalize_all(l):
#            return False
    res = [capitalize_all(l) for l in n if capitalize_all(l)]
    return res

print capitalize_nested(test1)
print capitalize_nested(test2)
print capitalize_nested(test3)
print capitalize_nested(test4)

