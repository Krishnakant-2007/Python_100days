# Question: Make a Calculator

#Answer:
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = input("Select What you want to do; \"+\" , \"-\" , \"*\" , \"/\" , \"**\" , \"//\" , \"%\" :")


if c == "+":
    print(f"{a}+{b} = {a+b}")
if c == "-":
    print(f"{a}-{b} = {a-b}")
if c == "*":
    print(f"{a}*{b} = {a*b}")
if c == "/":
    print(f"{a}/{b} = {a/b}")
if c == "**":
    print(f"{a}**{b} = {a**b}") 
if c == "//":
    print(f"{a}//{b} = {a//b}")
if c == "%":
    print(f"{a}%{b} = {a%b}")
else:
    print("\nbachodi mat kar".title())