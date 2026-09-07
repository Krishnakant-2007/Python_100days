# String are IMMUTABLE...(IMMUTABLE => Non-Changeable)
# eg.,
a = "Krishna Kant"
print(a.upper())    # KRISHNA KANT         variable.upper() use krne se variable mai assigned values capital ho jaayengi!!!
print(a.lower())    #krishna kant          variable.lower() use krne se variable mai assigned values small ho jaayengi!!!

print(a)    #"Krishna Kant" he rahega, aisa nhi hoga, ki .upper() yaa .lower() krne se "a" ki bhi value change ho jaayegi(matlab "KRISHNA KANT" yaa "krishna kant" mai se kuchh ho jaayegi.) (Aisa isiliye nhi hoga kyunki strings immutable hoti hai!)




a = "!!Krishna Kant!!!!!"
print(a.rstrip("!"))    #"!!Krishna Kant" aayega, variable.rstrip(), variable mai assigned value ke end se, un values ko remove kr deta hai, jinko hmm () mai likhdete hai





a = '''Krishna Kant is currently studying in SSIU
Krishna Kant is 19 years old
Krishna Kant is from Haryana
Krishna Kant is CodingGita's Student'''

print(a.replace("Krishna Kant", "Doraemon"))   #variable.replace() use krne se hmm kisi specific word ya sentence ko replace kr skte h.





a = "Krishna Preeyaansh Ashish"
print(a.split(" "))   #['Krishna', 'Preeyaansh', 'Ashish']  (The split() method splits the given string at the specified instance and returns the separated strings as list items.)     




blogHeading = "introduction to js"
print(blogHeading.capitalize())     #"Introduction to js" (i --> I (capatalized))

blogHeading = "iNtRoDuCtIoN tO jS"
print(blogHeading.capitalize())     #"Introduction to js" (i --> I) but baaki ke peeche waale letters small ho jaayenge.
                                                       #  (N --> n)  
                                                       #  (R --> r)
                                                       #  (D --> d)
                                                       #  (C --> c)
                                                       #  (I --> i)
                                                       #  (N --> n)
                                                       #  (O --> o)
                                                       #  (S --> s)





str1 = "Welcome to the console"
print(str1.center(50))

# isko aise samjho:
print(str1.center(50, "-"))   #"--------------Welcome to the console--------------"
                              # \____________/\____________________/\____________/
                              #      14                22                 14
                              # \________________________________________________/
                              #                        50

#So basically center(50) aise kaam krta hai; (50 - len(str))/2) spaces or any character we want to apply on the both side of string...
# Hence
print(len(str1)) #22

#But
print(len(str1.center(50))) #50







a = "Krishna Kant , Krishna Kant , Krishna Kant , Krishna"
print(a.count("Kant"))  #3      Variable.count() batata hai, ki koi word yaa letter kitni baar aaya hai string mai.






str = "Welcome to the Console!!!"
print(str.endswith("!")) #True    variable.endswith() batata hai ki kya aapke variable ki value, iss word yaa letter se end hoti h...
print(str.endswith("!!")) #True
print(str.endswith("!!!")) #True
print(str.endswith("!!@")) #False

str = "Welcome to the Console!!!"
print(str.endswith("to",6 ,10 ))  #True   Matlab index[6] se index[10] ke baach mai, kya "to" exist krta hai???
                                  # e --> idx[6]
                                  #   --> idx[7]
                                  # t --> idx[8]
                                  # o --> idx[9]
                                  #   --> idx[10]
#Hence, we can clearly see.... idx[6] and idx[10] ke beech mai "to" aa rha h.








str1 = "His name is Dan. He is an Honest man."
print(str1.find("is")) #idx = 1    variable.find() batata hai hai ki string ke anadar, jo word hmm dhoond rahe hai, vo hai bhi yaa nahi...
#                             agar hai to, jaha pe vo word sabse pehele dikhta hai, uska index bata deta hai...

str1 = "He's name is Dan. He is an Honest man."
print(str1.find("is"))  #idx = 10

#Agar vo word string mai hai he nahi, jise hamm dhoond rahe hai, to idx = -1 return hoga








str1 = "He's name is Dan. He is an Honest man."
print(str1.index("is"))  #10  Similar to variable.find(), but jab koi word found nhi hota, to yr idx = -1 NAHI DETA, seedha error show krta hai...
# eg.;
#print(str1.index("ishh"))   #ValueError: substring not found








str = "WelcomeToTheConsole1"
print(str.isalnum())  #True   agar string mai only A-Z, a-z, 0-9 ke he characters hai, to True print hoga...(Agar Space bhi aagya to bhi False print hoga.)

str = "WelcomeToTheConsole!"
print(str.isalnum()) #False  Kyuki "!" bhi hai

str = "WelcomeToTheConsole 1"
print(str.isalnum()) #False







str = "WelcomeToTheConsole"
print(str.isalpha()) #True   ONLY TAKE A-Z, a-z







str = "elcomeoheonsole1"
print(str.islower())  #True  agar poori variable ki value lowercase mai hai, to True aayega...

str = "WelcomeToTheConsole1A"
print(str.islower())  #False  Because "A" is Capital







str = "WelcomeToTheConsole1"
print(str.isprintable())  #True

str = "WelcomeToTheConsole1\n"
print(str.isprintable())  #Fale  Because "\n" print nahi hota h







str1 = "      "   #Using TAB
print(str1.isspace()) #True     The variable.isspace() method returns True only and only if the string contains whitespaces, else returns False.

str1 = "      "   #Using SPACEBAR
print(str1.isspace()) #True

str1 = "Hello           World"
print(str1.isspace())  #False







str1 = "World Health Organisation"
print(str1.istitle())  #True;  The istitle() returns only True if the First letter of each word of the string is capitalised, else it returns False

str1 = "To kill a Mocking bird"
print(str1.istitle())  #False









str1 = "Python is a Compiled Language"
print(str1.replace("Compiled", "Interpreted"))  #Python is a Interpreted Language...








str1 = "Python is a Interpreted Language..."
print(str1.startswith("Python"))  #True








str1 = "hello"
print(str1.swapcase())  #HELLO    swapcase() changes the character casing of the string, uppercase to lower & Viceversa

str1 = "HELLO"
print(str1.swapcase())  #hello

str1 = "Hello"
print(str1.swapcase())  #hELLO








str1 = "He's name is Dan. He is an Honest man."
print(str1.title())  #He'S Name Is Dan. He Is An Honest Man.    (Capitalised each letter of the word within the string)