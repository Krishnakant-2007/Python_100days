a = input()
print(a)

a = input("Enter your Name :")
print("My name is ",a)

x = input("Enter First Number :")    #let x = 12
y = input("Enter Second Number :")   #let y = 1000

print(x + y)   #result is 121000 (kyunki, input ke andar jo bhi aata h, vo by default string type mai badal jata hai, hence, x and y are basically strings)

x = int(input("Enter First Number :"))    #12
y = int(input("Enter Second Number :"))   #1000

# Ab hmne x aur y ke type ko already define kr diya h (i.e., Integer)
# Hence
print(x + y)        #1012

# We can also do
x = input("Enter First Number :")    #let x = 12
y = input("Enter Second Number :")   #let y = 1000
print(int(x) + int(y))        #1012
