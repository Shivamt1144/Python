# wap a prgram, consider a name of few friends by user and select randomly who will pay the bill
import random
names=input("Enter names separated by comma ")
list_names=names.split(",")
# print(list_names)
length=len(list_names)
a=random.randint(0,length-1)
x=list_names[a]
print(f"{x}, will pay the bill")