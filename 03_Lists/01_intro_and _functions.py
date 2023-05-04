'''
# Lists are used to store multiple items in a single variable. example
# name=["John","Alfred","Simon"]
# print(name)
# we can store various data types
# list_1=["John",199,True,13.33]
# print(list_1)

# it allows duplicate values
list_2=["Apple","Banana","Cherry","Apple","Kiwi"]
print(list_2)

# lists are mutable
# they have 0 based indexing
list_2[0]="Mango"
print(f"The changed list is {list_2}")
'''
# Now we will discuss some of the function/methods
num=[1,2,4,6,-15,3]
''' 
print(num[0])
# negative index starts from backwards
print(num[-1])
# to print length of the list
print(f"the length of the list num is {len(num)}")

# slicing of the list
# print(num[2:4])
print(num[0:4]) #this will print the elements of the list, if we dont write the second limit i.e. 4, the complete list will be printed
# print(num[0:])
# print(num[:]) this will also print the whole list
# to skip the steps in slicing
print(num[0:5:2])
# to sort the list
num.sort()
print(num)
# we can't write print(num.sort()), this will not work
# we can not sort the list which has different data types

# to reverse the list
num.reverse()
print(num)

# maximum of the list
print(max(num))
print(min(num))

# to add element to the end of the list
num.append(69)
print(num)
# to insert at a particular position
num.insert(2,99)
# the first arguement in above function is the index and the other is the input
print(num)


#  to add more than one element at the end of the list
num.extend([88,89,77,215])
print(num)

# muatation of the string can be done like this also
num[1:4]=[201,202,203]
print(num)


# to remove the item from the list
num.remove(215) #note:this removes only the first occurence
print(num)
'''
# to remove the last element of the list
num.pop()
# can also be written as print(num.pop()), this will print the number removed
print(num)

# to remove the specific element, pass the index inside the pop
num.pop(3)
print(num)