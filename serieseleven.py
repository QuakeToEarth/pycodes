#-1 , -3 , -5 , -7 .. m terms
m = int(input("Enter Number of Terms: "))
for i in range(1,m+1,2):
    print(i*-1,end=",")