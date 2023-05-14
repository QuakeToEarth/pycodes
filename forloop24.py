#Write a program to input a number and check wheter it is a perfect number or not
#Perfect number is : 
a = 0
number = int(input("Enter a number please: "))
for i in range(1, number):
    if (number% i ==0):
        a = a+i
        print(a)

if (a == number):
    print("This is a perfect number :)")
else:
    print("This is not a perfect number :(")