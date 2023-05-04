# WAP check if year is leap year or not

year=int(input("Enter the year to check "))

if(year%4==0 and year%100==0 and year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")