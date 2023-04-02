#find the fictorical of 10 differnt numbers
for i in range(1,11):
    fic = 1
    num = int(input("Enter Number: "))
    for j in range (1,num+1):
        fic  = fic * j
    print("The Fictorial of", j, "is this: ", fic)