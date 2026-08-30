a = "Krishna"
b = "Kant"
print(a + b)      #KrishnaKant
print(a+""+b)     #KrishnaKant
print(a+" "+b)     #Krishna Kant


a = "1"
b = "2"
print(a + b)    #12
print(int(a) + int(b))    #3            It is TypeCasting, pehele a aur b sring the, but hmne "a" ke peeche "int" laga diya, jis se vo integer bn gya!


a = "Krishna Kant"
print(type(a))

string = "15"
number = 7
string_number = int(string)    #throws an error if the string is not a valid integer

sum = number + string_number

print(f"The Sum of both the numbers is : {sum}") 


#Implicit TypeCasting   -> Python automatically changes data types!!! 
c = 1.9   #float
d = 8  #int

e = print(c+d)
print(type(e))    #float    (c+d krne k liye, python "d" ka data type apne aap "float" mai change kr dega, kyunki "c" to float he h, agar "c" ko int mai change krta, to 1.9 add ho he nhi pata...)