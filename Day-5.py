# print("Hey I am a Good Boy
# and this viewer is also a good boy")       #Error (Aisa Krne se 'and this viewer is also a good boy' new line mai nahi jaayega)

# Hey Krishna, please dont remove this line.    (This is a comment, Which does not execyte with code.  shortcut -> CTRL + /)

print("Hey I am a Good Boy\nand this viewer is also a good boy")         #\n -> Escape Sequence Character(Isko use krne se, and this viewer is also a good boy, new line mai chala jaayega)

print("Hey I am a \"Good Boy\"\nand this viewer is also a \"Good Boy\"")     #\" -> Escape Sequence Character(Isko use krne se, hmm sentence ke beech mai double quotes add krskte hai, jo ki run krne k baad bhi show hoga. eg., Run Krne pr Good Boy double quotes mai show ho rha h.) (Ise hmm single quotes k liye bhi use kr skte hai.)

print("Hey", 6, 7, sep="~")     #Separater madad krta hai, ek he print statement mai di hui cheezon ko separatev krne mai, vo depend krta hai, ki hmm kis symbol ki help se separate krna chahate hai.

print("Hey", 6, 7, sep="~", end="009")     #End is used to specify, what to print at the end.
print("Krishna")

print("Hey", 6, 7, sep="~", end="009\n")     
print("Krishna")