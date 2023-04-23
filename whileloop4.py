#Write a program to print a number and check if it is armstrong or not
number = int(input("Enter Number: "))
ognumber = number
total = 0
while(number>0):
    digit = number%10
    total = total+ pow(digit,3)
    number = number//10

if(total == ognumber):
    print("This number", ognumber, " is an Armstrong number")
else:
    print("This number", ognumber, " is not an Armstrong number")