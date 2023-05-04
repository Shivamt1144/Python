'''
there are two identity operators
is 
is not
'''
a=5
b=5
c=9
print(a is b) #prints true
print(a is c) #prints false

# the memory address of both the objects(variables a,b) is same this is why it is returning true and vice-versa
# let us check the memory location
print(id(a))
print(id(b))
print(id(c))

x=5
print(id(x))
x=8
print(id(x))
print(x is x)