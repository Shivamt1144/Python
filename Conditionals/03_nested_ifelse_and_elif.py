''' WAP to buy product according to the money you have
if you have money then
if you have more than 5000, buy shoes
if you have more than 2000 and less than 5000, buy jeans
if you have more than 1000 and less than 2000, buy t-shirt
else go home
'''
a=input("Do you have money? yes/no ")
if(a=="yes" or a=="Yes" or a=="YES"):
     money=int(input("Enter the amonut of money you have"))
     if(money>5000):
         print("You can buy shoes")
     elif(money>2000 and money<5000):
         print("You can buy jeans")
     elif(money>1000 and money<2000):
         print("You can buy a T-shirt")

else:
    print("Go home")       
  

