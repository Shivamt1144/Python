'''
three logical operators are there
and, or , not

'''
a,b=5,4
print(a>4 and b<10) # true will be the output
print(a>4 and b>10) # false will be the output
# the important point here is to note that both the condition should be true for 'and' to give true as a output
print(a>4 or b<10) # true will be the output
# for 'or', if even one condition is true, it gives true as a output

# logical not is used to reverse the result
x=True
print(not(x))