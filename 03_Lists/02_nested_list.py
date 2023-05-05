# normal list
a=[1,2,3,5,78,54,84,54,1,151,84,84]
print(a)
print(f"the length of this list is {len(a)}")

# nested list
b=[1,2,54,4,4,854,484,[54,848,48,8748,744,5],955,656]
print(b)
print(f"the length of this list is {len(b)}")
'''
# to access the list inside list
print(b[7])
# to print the nested list's element
print(b[7][3]) #this will give 4th element of the nested list

print(b[len(b)-3])
'''
# slicing of the nested list
print(b[7][0:4])
# similarly we can use all other functions