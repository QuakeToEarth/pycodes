#write a program to input 10 numbers from the user and siaplay only buz number 
#buzz number is end with 7 or are divsable by 7
for i in range(1,11):
    num = int(input("Enter Number: "))
    if (num%7 == 0 or num%10 == 7):
        print(num, "this is a buzz number :) ")