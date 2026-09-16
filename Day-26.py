#GOOD MORNING SIR!!!  
name = input("Enter Your Name :")
x = name.title()
from datetime import datetime
now = datetime.now()
a = int(now.strftime("%H"))

print(f"\nCurrent Time- {now.strftime("%I:%M:%S%p")}")

if a >= 00           and a < 12:
    print(f"\n\nGood Morning {x}, Have a Good Day!!")
elif a >= 12 and a < 17:
    print(f"\n\nGood Afternoon {x}!!")
elif a >= 17 and a < 20:
    print(f"\n\nGood Evening {x}!!")
else:
    print(f"\n\nGood Night {x}, Have Sweet Dreams!!")