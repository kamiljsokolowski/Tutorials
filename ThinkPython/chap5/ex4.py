raw_a = raw_input('a = ...\n') 
raw_b = raw_input('b = ...\n') 
raw_c = raw_input('c = ...\n') 
a = int(raw_a)
b = int(raw_b)
c = int(raw_c)

def is_triangle(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        print 'No.'
    elif (a + b == c) or (a + c == b) or (b + c == a):
        print "'degenerate' triangle."
    else:
        print 'Yes.'

#is_triangle(3, 4, 5)
#is_triangle(2, 2, 3)
#is_triangle(2, 2, 4)
#is_triangle(2, 2, 5)
is_triangle(a, b, c)

