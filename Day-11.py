name = "Krishna"
friend = "Preeyansh"
anotherFriend = "Bhavya"
apple = '''He said,
Hi Krishna
hey I am good
"I want to eat an apple'''                 #Tripple double quotes yaa tripple single quotes se hamm, kisi bhi para ko aise ke aise he print kara skte h

print("Hello, " +name)
print(apple)

mango = '''A mango is an edible stone fruit produced by the tropical tree Mangifera indica. It originated in the northeastern part of the South Asia, in what is now Bangladesh, northeastern India and Myanmar. M. indica has been cultivated in South and Southeast Asia since ancient times, resulting in two modern mango cultivar lineages: the "Indian" and the "Southeast Asian" types. Other species in the genus Mangifera also produce edible fruit called "mangoes", most of which are found in the Malesian ecoregion.

There are several hundred cultivars of mango worldwide. Depending on the cultivar, mango fruits vary in size, shape, sweetness, skin colour, and flesh colour, which may be pale yellow, gold, green, or orange. Mango is the national fruit of India, Pakistan, and the Philippines, while the mango tree is the national tree of Bangladesh.'''

print(mango)





print(name[0])   #K
print(name[1])   #r
print(name[2])   #i
print(name[3])   #s
print(name[4])   #h
print(name[5])   #n
print(name[6])   #a
print(name[7])   #THROWS ERROR....

print('''Lets use a "For Loop"\n''')
for character in name:
    print(character)
for character in apple:
    print(character)
for character in mango:
    print(character)