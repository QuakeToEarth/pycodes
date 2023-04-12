count = 0
num = int(input("Enter Number: "))
for i in range (1,num+1):
    if (num%i == 0):
       count = count+1
print(count)
