def a(x, y):
    x = x + 1
    print 'a returning x * y =', x * y
    return x * y

def b(z):
    print 'calling a with x =', z, 'and y =', z
    prod = a(z,z)
    #print z, prod
    print 'b returning a(z, z) =', prod
    return prod

def c(x, y, z):
    total = x + y + z
    print 'calling b with z =', total
    square = b(total)**2
    print 'c returning b(z)**2 =', square
    return square

x = 1
y = x + 1
print 'calling c with x =', x, ', y =', y + 3, ', z =', x + y
print c (x, y+3, x+y)

