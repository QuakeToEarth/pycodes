#Write a program to input a number and display only even digits from the number
number = int(input("Enter Number: "))
while(number>0):
    digit = number%10
    if (digit%2 == 0):
        print(digit)
    number = number//10