#write program to enter a number and check if is an niven number
#If the number is divisible by it's digits sum then it is an niven number
number = int( input( "Please enter you number :)  ----> "))
Ognumber = number
sum = 0
while (number > 0):
    rem  = number%10
    sum = sum + rem
    number = number//10
    
if (Ognumber % sum == 0):
    print("This is a niven number!! :D")
else:
    print( "This is not a niven number :(")

