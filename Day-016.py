#Match Case Statements.... (similar to if-elif-else statement)

x = int(input("Enter the value of x: "))
# x is the variable to match
match  x:
    case 0:      #if x is 0
        print("x is zero")       #agar x ki value zero daali, to code execution yahi khatam ho jaayega, nahi to next line pe chala jaayega
    case 4:
        print("x is 4")          #agar x ki value 4 daali, to code execution yahi khatam ho jaayega, nahi to next line pe chala jaayega
    #case with if-condition...
    case _ if x!=90:
        print(f"{x} is not 90")  #agar x ki value "0", "4", "90" ke alawa kuchh bhi hui, to code execution yahi khatam ho jaayega, nahi to next line pe chala jaayega
    case _ if x!=80:
        print(f"{x} is not 80")  #agar x ki value 90 hui, to he ye yaha execute hoga, kyunki agar 90 nhi hui, to upar waali line he execute hogi...

    case _:       #"_" is called a wildcard pattern.  "_" accepts all the values..
        print(x)  #ye line tab execute hogi, jab upar mai se koi bhi case execute nhi hoga....




#Exapmle-2

x = int(input("Enter x: "))

match x:
    case 0:
        print("x is zero")

    case 4:
        print("x is four")

    case _:
        print(x)   #ab agr x ki value, 0 aur 4, ke alawa kuchh bhi, to ye execute hoga...



#Example-2

# note: "case _": should generally be the last case.

# match x:
#     case _:
#         print("Anything")
#     case 4:
#         print("Four")

#The case 4 will never get a chance, because _ already accepts 4.
#So, 
# match x:
#     case 0:
#         ...
#     case 4:
#         ...
#     case _:
#         ...   is the correct structure...