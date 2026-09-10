n = int(input("enter a number: ".title()))
s=0
for i in range(1,n+1):
  if n%i==0:
    s+=1
if s==2:
  print(f"{n} is a Prime Number...")
else:
  print(f"{n} is not a Prime Number...")
print("")
a = input("Want to check any other number? (y/n): ")

while True:
  if a == "y":
    n = int(input("enter a number: ".title()))
    s=0
    for i in range(1,n+1):
      if n%i==0:
        s+=1
    if s==2:
      print(f"{n} is a Prime Number...")
    else:
      print(f"{n} is not a Prime Number...")
    print("")
    a = input("Want to check any other number? (y/n): ")
  else:
    break
print("Thanks!!!\nVisit Again...")

    