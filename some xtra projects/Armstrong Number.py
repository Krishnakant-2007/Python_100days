num = input("Enter a number: ")
sum = 0
for i in num:
    sum += int(i)**len(num)

if sum == int(num):
    print(num, "is Armstrong Number")
    
else:
    print(num, "is NOT Armstrong Number")