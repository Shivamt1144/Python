import random
# to import random module

'''
some functions:
1.randint(a,b) this will return a random integer number b/w a and b both a and b inclusive
2.randrange(a,b) this will also return b/w a and b but here b will not be included
3. random(), this will return floating point number with range 0.0<=x<1(not iclusive)
4. uniform(), returns floatiing point number within a range
5. choice(), to select a random element from sequence{mainly used for lists}
6.shuffle(), to shuffle any sequence

'''
# a=random.randint(1,7)
# a=random.randrange(1,7)
# a=random.random()
# a=random.uniform(1,5)
a=[1,5,6,8,9,52,4,59,84,989,59]
b=random.choice(a)
print(b)