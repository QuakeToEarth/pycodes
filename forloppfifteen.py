#write a program to input 10 numbers and display only positive even numbers
for i in range(1,11):
    num = int(input("Enter Number: "))
    if (num%2 == 0 and num > 0):
        print(num , "This is a positive and even number :D")