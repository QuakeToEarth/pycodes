#1 , -2 , 3 , -4 , 5 , -6 .... n
# if i/2 =0 - =1 +
n = int(input("Enter Number: "))
for i in range(1,n+1):
    if (i%2 == 1):
        print(i)
    else:
        print(-i)