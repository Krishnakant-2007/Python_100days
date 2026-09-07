# For Loops....

name = "Krishna Kant"
for i in name:
    print(i, end=", ")   #K, r, i, s, h, n, a,  , K, a, n, t,

print("")
print("")

name = "Krishna Kant"
for i in name:
    print(i)       #K
                   #r
                   #i
                   #s
                   #h
                   #n
                   #a
                   #
                   #K
                   #a
                   #n
                   #t

print("")

name = "Krishna Kant"
for i in name:
    print(i)
    if i.lower() == "k":
        print("This is something special!")  #K
                                             #r
                                             #i
                                             #s
                                             #h
                                             #n
                                             #a
                                             #
                                             #K
                                             #a
                                             #n
                                             #t

print("")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)  #Red
                  #Green
                  #Blue
                  #Yellow

print("")

for color in colors:
    print(color)
    for i in color:
        print(i)   #Red
                   #R
                   #e
                   #d
                   #Green
                   #G
                   #r
                   #e
                   #e
                   #n
                   #Blue
                   #B
                   #l
                   #u
                   #e
                   #Yellow
                   #Y
                   #e
                   #l
                   #l
                   #o
                   #w

print("\n\n")
#RANGE....

for k in range(5):     #(by default starts with ZERO)
    print(k)  #0        (0-4 numbers print hoyenge, 5 print nhi hoyega...) (agar "range(3)" hai, to 0-2 print numbers print hoyenge!!)
              #1
              #2
              #3
              #4

print("\n\n")

for k in range(5):
    print(k+1)   #0 +1 => print(1) => 1
                 #1 +1 => print(2) => 2
                 #2 +1 => print(3) => 3
                 #3 +1 => print(4) => 4
                 #4 +1 => print(5) => 5
                 #5 NOT INCLUDED

print("\n\n")

for k in range(5):
    print(k+2)   #0 +2 => print(2) => 2
                 #1 +2 => print(3) => 3
                 #2 +2 => print(4) => 4
                 #3 +2 => print(5) => 5
                 #4 +2 => print(6) => 6
                 #5 NOT INCLUDED

print("\n\n")

for k in range(1,5):
    print(k)   #NOW, by default ZERO se start nhi hoga...; 1 se start hoga.... #1
                                                                               #2
                                                                               #3
                                                                               #4

print("\n\n")

for k in range(1,5,2):  #(start, stop, step)
    print(k)   #1 
               #3 (stepped 2)
               #"5 aayega he nhi"

print("\n\n")

for k in range(1,12,2):
    print(k)  #1
              #3   (stepped 2)
              #5   (stepped 2)
              #7   (stepped 2)
              #9   (stepped 2)
              #11  (stepped 2)

print("\n\n")

for k in range(1,12,3):
    print(k)  #1
              #4  (stepped 3)
              #7  (stepped 3)
              #10 (stepped 3)
              #"13 NOT INCLUDED"

