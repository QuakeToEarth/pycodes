#Write a program to input 10 numbers and display only the even numbers
for i in range(1,11):
        num = int(input("Enter Number: "))
        if (num%2 == 0):
            print(num)