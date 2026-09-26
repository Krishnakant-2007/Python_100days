# TUPLES  --> Tuples are not mutable, means not changeable

tup = (1, 3, 5)
print(type(tup), tup)       # <class 'tuple'> (1, 3, 5)

tup = (1, 3)
print(type(tup), tup)       # <class 'tuple'> (1, 3)

tup = (1)
print(type(tup), tup)       # <class 'int'> 1

tup = (1,)
print(type(tup), tup)       # <class 'tuple'> (1,)

tup = (1, 2, 3, 76, 342)
# tup[0] = 90
# print(type(tup), tup)       # ---> Throws an error, because, tuples are immutable, so we can not add "90" in tup at 0th index...

tup = (1, 2, 76, 342, 32, "Green", True)
print(type(tup), tup)       #<class 'tuple'> (1, 2, 76, 342, 32, 'Green', True)

print(len(tup))             #7

print(tup[0])               #1
print(tup[-1])              #True           tup[len(tup)-1] = tup[7-1] = tup[6] = True
print(tup[2])               #76

# print(tup[34])       THROWS ERROR AS "No value occurs at 34th index"

if 342 in tup:
    print("Yes 342 is present in this tuple")
else:
    print("Absent")


tup2 = tup[1:4]
print(tup2)                 #New Tuple get formed