l = [3, 5, 6]
print(l)
print(type(l))     # <class 'list'> 
print(l[0])        #3
print(l[1])        #5
print(l[2])        #6

# Lists are ordered collection of data items.
# They store multiple items in single variables.
# List items are separated by commas and enclosed within square brackets[].
# Lists are changeable, meaning we can alter them after creation.

list = [3, 5, 6, "Krishna", True]   #A single list can contain items of different data types.

# Each Item/Element in a list has its own unique index.... This index can be used to access any particular item from the list. The first item has index [0], second item has index[1], third item hax index[2] and so on..

print(list[-3])                 # Negative index ----------------------> "6" aayega.
print(list[len(list)-3])        # Converting to positive index
print(list[5-3])
print(list[2])                  # Converted to positive index ---------> "6" aayega.




#Check Whether an item is present in the list?

# We can check if a given item is present in the list. This is done using "in" key word...

colors = ["Red", "Green", "Yellow", "Blue", "White"]

if "Yellow" in  colors:
    print("Yellow is present")
else:
    print("Yellow is absent")

if "K" and "r" and "s" in "Krishna":
    print("Yes ")
else:
    print("No 😒, Krs is NOT present in Krishna...")


# SOMETHING MORE ON INDEX...

print(colors)        # ["Red", "Green", "Yellow", "Blue", "White"]
print(colors[:])     # ["Red", "Green", "Yellow", "Blue", "White"]
print(colors[1:])    # ["Green", "Yellow", "Blue", "White"]
print(colors[1:-1])  # color[1:(len(colors)-1)] ---> colors[1:(5-1)] ---> colors[1:4] ---> ["Green", "Yellow", "Blue"]

# Jump Index...
print(colors[1:4:2])   # sabse pehele list[1:4] nikalenge ---> i.e., ["Green", "Yellow", "Blue"] ---> [1:4:2] mai 2 ka malab 2 ka jump... ---> ["Green", "Yellow", "Blue"]
#   |________| |_______|
#      +1         +2

# as +2 ends at "Blue", hence,      print(colors[1:4:2]) ---> ["Green", "Blue"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:8:3])  #----> [3, 6]      Explanation: numbers[2:8] --> [3, 4, 5, 6, 7, 8]
#                                                                        |__|__|__|__|__|
#                                                                         +1 +2 +3 +1 +2
#                                                                          |_____|
#                                                                           [3, 6]

# COMPREHENSIVE LIST.....

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)