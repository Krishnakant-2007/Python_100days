# LIST METHODS

l = [1, 2, 4, 6]
print(l)                # [1, 2, 4, 6]


l.append(7)
print(l)                # [1, 2, 4, 6, 7] --> 7 Added


l = [11, 45, 1, 2, 4, 6, 3]
l.sort()
print(l)                # [1, 2, 3, 4, 6, 11, 45] --> Ascending Order


l = [11, 45, 1, 2, 4 ,6, 3]
l.sort(reverse=True)
print(l)                # [45, 11, 6, 4, 3, 2, 1] --> Descending Order


l = [11, 45, 1, 2, 4 ,6, 3]
l.reverse()
print(l)                # [3, 6, 4, 2, 1, 45, 11] --> List Reversed


l = [11, 45, 1, 2, 4 ,6, 3]
print(l.index(1))       # 1 ka index dega, that is 2.... (index() method returns the index of the first occurence of the list item.)


l = [11, 45, 1, 4, 5, 1, 1, 9, 10]
print(l.count(1))       # list mai kitne 1 hai, count() method vo batayega......


m = l                   # Taking "m" as a reference of "l"
m[1] = 10               # ab kyunki, "m" "l" hai, to indirectly, "l" ke 1st index pe ham 10 ko put kra rhe h..
print(l)                # [11, 10, 1, 4, 5, 1, 1, 9, 10]
#                               ↓
#                    dekho, 10 1st index pe place ho gya


colors = ["violet", "indigo", "blue"]
colors.insert(1, "green")               # colors mai, 1st index pr, "green ko insert krdo....."
print(colors)


m = [900, 1000, 1100]
l.extend(m)                             # "l" mai "m" ko jod do....
print(l)                                # [11, 10, 1, 4, 5, 1, 1, 9, 10, 900, 1000, 1100]


k = l+m
print(k)                                # [11, 10, 1, 4, 5, 1, 1, 9, 10, 900, 1000, 1100, 900, 1000, 1100]
#                                          |____________________________________________| |______________|
#                                                               l                        +       m


