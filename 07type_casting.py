print(len("12345"))
# the above name is string but if we do like this:
# print(len(12345))
# throws error because it is an int data type. TypeError: object of type 'int' has no len()

length=len("Shivam Tripathi")
# print("your name is "+length +" characters")
# TypeError: can only concatenate str (not "int") to str; here the length stores number i.e. int
# so in order to concatenate we have to typecast variabe length so
print("your name has "+str(length) +" characters")

new_length=str(length)
print(type(new_length))
 
 
'''
int():will convert to integer data type
float():will convert to float data type

'''

# reason why we need type casting is
print(10+10)
# this will give 20
print("10"+"10")
# this will give 1010
print(int("10")+int("10"))
# this will give 20

#if we try
# name="Shivam"
# #print(10+int(name))
# this will throw error ValueError: invalid literal for int() with base 10

name="123"
print(10+int(name))
# this will give 133 because now name has base 10

