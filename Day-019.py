# BREAK & CONTINUE

for i in range(1,13):
    print(f"5 X {i} = {i*5}")
#But I want to stop it at 5 X 10 = 50
    if i == 10:
        break                  #(YAHA PR 10 KE BAAD BREAK KAREGA.....)
                                #OUTPUT => 5 X 1 = 5
                                #          5 X 2 = 10
                                #          5 X 3 = 15
                                #          5 X 4 = 20
                                #          5 X 5 = 25
                                #          5 X 6 = 30
                                #          5 X 7 = 35
                                #          5 X 8 = 40
                                #          5 X 9 = 45
                                #          5 X 10 = 50

print("")

for i in range(1,13):
    if i == 10:                #(YAHA PAR 10 KO AAGE BADHNE HE NAHI DEGA......)
        break
    print(f"5 X {i} = {i*5}")   #OUTPUT => 5 X 1 = 5
                                #          5 X 2 = 10
                                #          5 X 3 = 15
                                #          5 X 4 = 20
                                #          5 X 5 = 25
                                #          5 X 6 = 30
                                #          5 X 7 = 35
                                #          5 X 8 = 40
                                #          5 X 9 = 45

#BREAK => LOOP KO CHODKAR NIKAL JAO
#CONTINUE => ITERATION KO CHODKAR NIKAL JAO

for i in range(12):
    if i == 10:
        print("Iteration Skipped!")
        continue
    print(f"5 X {i} = {i*5}")   #OUTPUT => 5 X 1 = 5
                                #          5 X 2 = 10
                                #          5 X 3 = 15
                                #          5 X 4 = 20
                                #          5 X 5 = 25
                                #          5 X 6 = 30
                                #          5 X 7 = 35
                                #          5 X 8 = 40
                                #          5 X 9 = 45 
                                #          Iteration Skipped!
                                #          5 X 11 = 55

print("")

for i in range(12):
    print(f"5 X {i} = {i*5}")
    if i == 10:
        print("Iteration Skipped!")
    continue                    #           5 X 0 = 0
                                #           5 X 1 = 5
                                #           5 X 2 = 10
                                #           5 X 3 = 15
                                #           5 X 4 = 20
                                #           5 X 5 = 25
                                #           5 X 6 = 30
                                #           5 X 7 = 35
                                #           5 X 8 = 40
                                #           5 X 9 = 45
                                #           5 X 10 = 50
                                #           Iteration Skipped!
                                #           5 X 11 = 55

print("")

#DO-WHILE LOOP....
i = 0
while i < 1000:
    i += 1
    if (i%100==0):
        continue
    print(i)
    