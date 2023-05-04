'''
make a love calculator
input 2 names
now check for letter 't','r','u' ,'e'
the check for 'l','o','v','e'
sum of occurence of true and sum of occurence of love is the %
eg:
Bradd Pitt
Angelina Jolie
t comes 2 times,r comes 1 time,  u comes 0 times, e comes 2 times: sum=5
then
l comes 2 times, o comes 1 time, v comes 0 times, e comes 2 times: sum=5

percentage:55%
'''

a=input("Enter Boys's name")
b=input("Enter Girl's name")
combined_name=a+b
lower_name=combined_name.lower()

t=lower_name.count('t')
r=lower_name.count('r')
u=lower_name.count('u')
e=lower_name.count('e')
true=t+r+u+e
l=lower_name.count('l')
o=lower_name.count('o')
v=lower_name.count('v')
e=lower_name.count('e')
love=l+o+v+e

love_score= str(true)+str(love)
print(love_score)