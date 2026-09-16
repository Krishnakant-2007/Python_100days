num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
if num1 > num2:
    print("PLEASE ENTER 2nd NUMBER LARGER..... :)")
elif num1==num2:
    print(f"Prime Numbers between {num1} and {num2} are ZERO....")

sum = []

for i in range (num1+1, num2):
    s = 0
    for q in range(1, num2+1):
        if i%q==0:
            s += 1
    sum.append(s)

count=0   
for i in sum:
    if i == 2:
        count+=1
print(f"Total Prime Numbers Between {num1} and {num2} are {count}")