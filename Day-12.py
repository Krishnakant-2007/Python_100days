names = "Krishna Kant"
a = len(names)       #prints length of word, which was assigned as "names" variable, (number of spaces bhi include hote h).
print(f"{names} is a {a} letter word.")

print(names[0:6])    #Krishn (K -> index(0))      (0 - 5 indexes tak he print honge, jitne ham daalte hai, ek kamm he print hota h.)
                            #(r -> index(1))
                            #(i -> index(2))
                            #(s -> index(3))
                            #(h -> index(4))
                            #(n -> index(5))

print(names[0:7])    #Krishna (K -> index(0))      
                             #(r -> index(1))
                             #(i -> index(2))
                             #(s -> index(3))
                             #(h -> index(4))
                             #(n -> index(5))
                             #(a -> index(6))

print(names[:7])     #"Krishna" he aayega, agar ham starting mai index nhi bhi likhenge, to bhi python waha pe apne aap he "0" assume ke chalega.  

print(names[:])      #"Krishna Kant" aayega, Starting mai Python ZERO Assume krega, ending mai LEN(NAMES) ko assume krega, as len(names) = 12, it means  1 -> K -> index(0)
               #2 -> r -> index(1)
               #3 -> i -> index(2)
               #4 -> s -> index(3)
               #5 -> h -> index(4)
               #6 -> n -> index(5)
               #7 -> a -> index(6)
               #8 ->   -> index(7)
               #9 -> K -> index(8)
               #10-> a -> index(9) <-------------------------------------------------|
               #11-> n -> index(10)                                                  |
               #12-> t -> index(11)                                                  |
#                         index(12) <---------|                                      |
#                                             |                                      |
print(names[:len(names)])      #print(names[:12])                                    |
#                                                                                    |
print(names[:-3])  #"Krishna K" (names[0:len(names)-3]) = (names[0:12-3]) = (names[0:9])
#
# jab bhi hmm indexing mai -ve term ka use krta hai, python automatically, -ve k aage, length(variable) laga leta h
#
#
print(names[-1:-3])  #kuchh nhi aayega, PYTHON be like: names[len(names)-1:len(names)-3] = names[12-1:12-3] = names[11:9] => NO SENSE
#
#                                                                                                  
print(names[-3:-1]) #"an" aayega, (names[len(names)-3:len(names)-1]) = (names[12-3:12-1]) = (names[9:11])


#Home Work:-
# nm = "Harry"
#print(nm[-4:-2])
# Isko run krne k baad kya aayega?

#Solution:
#as len(nm) = 5
#so,
#(nm[-4:-2]) = (nm[5-4:5-2]) = (nm[1:3]) => ar