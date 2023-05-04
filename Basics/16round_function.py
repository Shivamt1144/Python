# syntax: round(number, no. of digits)
print(round(23.22)) #this will give 23, no. of digits is optional
print(round(25.1238884,3)) #this will give 25.124
print(round(7,5))
print(round(647,-1)) #this will return the closests multiple of 10 i.e. 650, his works on power type i.e 10^(-no.of digits), in this case 10^(-(-1))=10^1=10
print(round(643,-1)) #this will return the closests multiple of 10 i.e. 640
print(round(674,-1000)) #this will return the closests multiple of 1000 i.e. 0
print(round(674.1024,-1))#this will return the closests multiple of 10 i.e. 670