def Rev_Num(num):
    original_num = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    print(original_num + rev)

n = int(input("Enter a Number : "))
Rev_Num (n)


#using Slicing.....
a = input("Enter a Number: ")
b = a[::-1]
sum = int(a)+int(b)
print(sum)