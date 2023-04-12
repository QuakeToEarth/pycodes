#input number, check wheter it is a prime number or not
count = 0
num = int(input("Enter Number: "))
for i in range (1,num+1):
    if (num%i == 0):
       count = count+1
if (count == 2):
    print(num, "is a prime number! =]")
else:
    print(num, "isn't a prime number! =[")