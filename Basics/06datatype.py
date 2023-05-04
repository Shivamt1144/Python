a=123
print(type(a))
# type function is used to check the data type of the variable
# python itself detects the type of data
print(0b10)
# 0b here represents the number is in binary and when we will print the output will be 2
print(0o10)
# 0b here represents the number is in octal and when we will print the output will be 8
print(0x10)
# 0b here represents the number is in hexadecimal and when we will print the output will be 16
name="Shivam Tripathi"
print(name)
print(type(name))

b=554.25
print(b)
print(type(b))

var1="Mutable String"
print(var1[0])
# this will print the letter on 0th index i.e. M, the indexing starts with 0

# we cannot concatenate two different data type for example
var2="Shivam"
var3=11
# print(var2+var3) this will throw error, so we have to change the type of the var3
print(var2+str(var3))


print("Shivam\'s \"Programs\"") 
# \this is used to skip the special meaning of ' and ""