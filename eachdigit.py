#Write a program to input a number and display each digit of the number
number = int(input("Enter Number: "))

while(number>0):
    digit = number%10
    print(digit)
    number = number//10
