#write a program to input a number and display the mazimum digit
number = int(input("Please enter your number: "))
min = 9999999
while( number > 0):
    rem = number%10
    if (rem<min):
        min = rem
    
    number = number//10

print(min)