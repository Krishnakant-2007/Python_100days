a = int(input("Enter Your age: "))
print(f"Your age is {a}")

#Conditional Operators
# > , < , >= , <= , == , !=
print(a>18)
print(a<18)
print(a==18)
print(a<=18)
print(a>=18)
print(a!=18)

if (a>18):
    print("You can Drive")
else:
    print("You Cannot Drive")
    print("Go and Drink Milk")
print("Hello")      #exited else, to ab ise print hone ke liye koi condition nhi chahiye, ye end mai print hoga he hoga....






num = int(input("Enter the value of num: "))
if (num < 0):    #Agar ye waali condition match kr gyi, to code yahi end ho jaayega, fir seedha "I am Hppy Now" print hoga....
    print("Num is Negative.")
elif(num == 0):    #Agar first waali condition fasle ho gyi to fir code yaha pe aayega, agr yaha condition match kr gyi, to yehi end ho jaayega. Fir seedha "I am Happy Now" Show krega.. 
    print("Number is Zero.")
elif(num == 999):    #Agar second waali bhi condition match nhi ki, to code 3rd condition pr aayega.... (Jb tak condition True nhi ho jaati, tab tak aise he chalta rahega....)
    print("Number is special")
else:
    print("Number is Positive")
print("I am Happy Now")  #Ye to execute hoga he hoga....





num = int(input("Enter Your Num :"))
if (num < 0):
    print("number is negative".title())
elif (num > 0):
    print("number is positive".title())
    if num > 0 and num <= 10:
        print("number is between 0-10".title)
    elif num > 10 and num <= 20:
        print("Number is between 10-20".title())
    elif num > 20 and num <= 30:
        print("number is between 20-30".title())
else:
    print("number is zero".title())