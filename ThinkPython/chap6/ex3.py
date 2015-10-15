raw_x = raw_input('x = ...\n') 
raw_y = raw_input('y = ...\n') 
raw_z = raw_input('z = ...\n') 
x = int(raw_x)
y = int(raw_y)
z = int(raw_z)

def is_between(x,y,z):
    return x <= y <= z

#print is_between(1,1,1)
#print is_between(1,2,3)
#print is_between(2,2,3)
#print is_between(2,3,3)
#print is_between(4,3,3)
#print is_between(3,4,3)
print is_between(x,y,z)

