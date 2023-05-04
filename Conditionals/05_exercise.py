'''
WAP to buy pizza
small pizza=100rs
medium pizza=200rs
large pizza=300rs 
then ask the user if they want to add peperoni
peperoni for small pizza=20rs
peperoni for medium and large pizza=30rs
also ask for extra cheese
extra cheese= 25rs all
'''
print("Hello to the Python Pizza Store ")
print("What size of pizza you want?")
bill=0
size=input("Enter S for small, M for medium and L for large ")
if(size=="S" or size=="s"):
    a=input("Do you want to add peperoni for 20 rupees? Y/N ")
    b=input("Do you want to add extra cheese for 25 rupees? Y/N ")
    if((a=="y" or a=="Y") and(b=="y" or b=="Y")):
        bill=145
        print(bill)
    if((a=="y" or a=="Y") and(b=="n" or b=="N")):
            bill=120
            print(bill)
    if((a=="n" or a=="N") and(b=="y" or b=="Y")):
            bill=125
            print(bill)
    elif((a=="n" or a=="N") and(b=="N" or b=="n")):
            bill=100
            print(bill)

if(size=="M" or size=="m"):
    a=input("Do you want to add peperoni for 30 rupees? Y/N ")
    b=input("Do you want to add extra cheese for 25 rupees? Y/N ")
    if((a=="y" or a=="Y") and(b=="y" or b=="Y")):
        bill=255
        print(bill)
    if((a=="y" or a=="Y") and(b=="n" or b=="N")):
            bill=230
            print(bill)
    if((a=="n" or a=="N") and(b=="y" or b=="Y")):
            bill=225
            print(bill)
    elif((a=="n" or a=="N") and(b=="N" or b=="n")):
            bill=200
            print(bill) 
    
if(size=="L" or size=="l"):
    a=input("Do you want to add peperoni for 30 rupees? Y/N ")
    b=input("Do you want to add extra cheese for 25 rupees? Y/N ")
    if((a=="y" or a=="Y") and(b=="y" or b=="Y")):
        bill=355
        print(bill)
    if((a=="y" or a=="Y") and(b=="n" or b=="N")):
            bill=330
            print(bill)
    if((a=="n" or a=="N") and(b=="y" or b=="Y")):
            bill=325
            print(bill)
    elif((a=="n" or a=="N") and(b=="N" or b=="n")):
            bill=300
            print(bill)
    
            
    