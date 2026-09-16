#WHILE LOOPS...

for i in range(3):
    print(i)   #0
               #1
               #2

print("")

#DOING IT BY "WHILE LOOP"
i = 0
while (i<3):
    print(i)
    i = i+1    #0
               #1
               #2 

#SEE HOW IT EXECUTES....
# Taking i = 0:
# since, 0 < 3 (True) => print(0) => 0

# Now, 0 +1
#Taking i = 1:
# since, 1 < 3 (True) => print(1) => 1

# Now, 1 +1
#Taking i = 2:
# since, 2 < 3 (True) => print(2) => 2

# Now, 2 +1
#Taking i = 3:
# as, 3 < 3 (False) => EXECUTION STOPS

print("")

i = 0
while (i<=3):
    print(i)
    i = i+1    #0
               #1
               #2
               #3   

print("")

i = 0
while (i <= 38):
    i = int(input("Enter a number: ".title()))
print("Loop Ended....")  #Ab isme, jab tak user i ki value ko 38 se kam yaa uske barabar nhi daalta, tab tak, user se input leta rahega

print("")

i = 0
while (i <= 38):
    a = input("Enter a name: ".title())
    i = int(input("Enter a number: ".title()))
print("Loop Ended....")

print("")

i = 0
while (i <= 38):
    i = int(input("Enter a number: ".title()))
    a = input("Enter a name: ".title())
print("Loop Ended....")

print("")

#DECREASING LOOP....
i = 5
while (i > 0): 
    print(i)
    i = i-1  #5
             #4
             #3
             #2
             #1

print("")

#INFINITE LOOP...
i = 5
while (i > 0): 
    print(i)
    i = i+1  

print("")

#ELSE WITH WHILE LOOP.....
i = 5
while (i > 0): 
    print(i)
    i = i-1  
else:
    print("I AM EXECUTED BECAUSE CONDITION FOR WHILE LOOP GOT FALSE...")  #Yeh tab print hoga, jab while loop ke liye, koi condition false ho jaayegi

i = 0
while (i>5 or i<5):
    print(i)
    i = i+1
else:
    print("I AM EXECUTED BECAUSE CONDITION FOR WHILE LOOP GOT FALSE...")
i = i+1
while (i>5 or i<5):
    print(i)
    i = i+1
    if i == 500:
        break           #output => 1
                        #          2
                        #          3
                        #          4
                        #          I AM EXECUTED BECAUSE CONDITION FOR WHILE LOOP GOT FALSE...
                        #          6
                        #          7
                        #          till 499

