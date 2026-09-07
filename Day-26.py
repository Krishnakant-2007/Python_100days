#GOOD MORNING SIR!!!  
name = input("Enter Your Name :")

from datetime import datetime
now = datetime.now()
a = int(now.strftime("%H"))

print(f"\nCurrent Time- {now.strftime("%I:%M:%S%p")}")

if a >= 00           and a < 12:
    print(f"\n\nGood Morning {name}, Have a Good Day!!")
elif a >= 12 and a < 17:
    print(f"\n\nGood Afternoon {name}!!")
elif a >= 17 and a < 20:
    print(f"\n\nGood Evening {name}!!")
else:
    print(f"\n\nGood Night {name}, Have Sweet Dreams!!")