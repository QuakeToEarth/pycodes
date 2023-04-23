#Write a program to input a number and find the sum of each digit
#3425
number = int(input("Enter Number: "))
total = 0
while(number>0):
    digit = number%10
    total = total+digit
    number = number//10
print(total)
