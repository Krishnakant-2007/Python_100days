# for example, We want ot calculate geometric mean...
a = 9
b = 8
gmean1 = (a*b)/(a+b)
print(gmean1)
print("")
c = 8
d = 7
gmean2 = (c*d)/(c+d)
print(gmean2)
print("")

# ab jab bhi hamko, gmean likhna hoga, hame ye baar baar likhna hoga
# is se badhiya hamm geometric mean ka function likh lenge

def geomean(a, b):
    mean = (a*b)/(a+b)
    print(f"G.M. of {a} and {b}: {mean}")

# now this is the function to find geometric mean of any numbers...
geomean(9, 8)     #bass itna he likhne se ab aapke paas 9 aur 8 ka geometric mean mil jaayega...
print("")
geomean(2, 2) #1.0
print("")

#agar hamm chahe to isi function mai yeh bhi bana sakte h, ki konsa number bada h.....
def geomean(a, b):
    mean = (a*b)/(a+b)
    print(f"G.M. of {a} and {b}: {mean}")

    if (a > b):
        print(f"{a} > {b}")
    elif (a == b):
        print(f"{a} = {b}")
    else:
        print(f"{a} < {b}")

geomean(9, 8)     
print("")
geomean(2, 2) 
print("")
geomean(8,9)
print("")

def compare(a, b):
    if (a > b):
        print(f"From {a} and {b}:           {a} > {b}   or we can say   {b} < {a}")
    elif (a == b):
        print(f"From {a} and {b}:              {a} = {b}")
    else:
        print(f"From {a} and {b}:              {a} < {b}      or we can say   {b} > {a}")

compare(100, 99)
compare(0, 0)
compare(2, 3)
compare(46, 67)