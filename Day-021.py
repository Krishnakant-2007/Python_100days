#Function Arguments....

def average(a, b):
    avg = (a+b)/2
    print(f"Average of {a} and {b} is: {avg}")

average(2,2)
average(9, 18)
print("")

# abhi hamm apni marzi se kinhi bhi do numbers ke average nikal paa rhe h.....But, seee......
def average(a=9, b=9):
    avg = (a+b)/2
    print(avg)

average() #9      ise, Default argument kehete hai..... Function ke andar a=9 and b=9 already defined hai....But if...we do,
average(1) #5     ab yaha a=1 ho gya hai, but b=9 he h, by default
average(1,3) #2   ab yaha a=1 aur b=3 ho gya h
average(b=1) #5   a=9 by default, but hmne b ki value ko 1 kr diya h..   note: hame b likhna zaruri hai, nhi likhinge to vo value a ko assign ho jaayegi
print("")

def name(fname, mname="Kant", lname="Tiwari"):
    print(f"Hello! {fname} {mname} {lname}")

name("Krishna")

print("")
#Required Arguments....

def average(a,b=1):
    print("The average is ", (a+b)/2)   #ab yaha pe a ki value dena required hai.....
average(2)

print("")
#VARIABLE LENGTH ARGUEMENT....

def average(*num):    # "*" lagane se ham kitne bhi arguements le skte h...
    print(type(num))
    sum=0
    for i in num:
        sum = sum + i
    print(f"Average is: {sum/len(num)}")

average(1,2,3,4,5)

# note: *num ka matlab hai:

#       "Function ko jitne bhi positional arguments milenge, un sabko collect karke num naam ke tuple mein rakh do."

#       Tum call kar rahe ho:  average(1, 2, 3, 4, 5)
#       Python internally roughly aise treat karta hai:  num = (1, 2, 3, 4, 5)

#       Isliye:  print(type(num))  => <class 'tuple'>

print("")
def name(**name):
    print(type(name))
    print("Hello! ", name["fname"], name["mname"], name["lname"])

name(mname="Kant", lname="Tiwari", fname="Krishna")

# note: **num ka matlab hai:

#       "Function ko jitne bhi positional arguments milenge, un sabko collect karke num naam ke dictionary mein rakh do."

#       Isliye:  print(type(num))  => <class 'dict'>