#
number = int(input('Please enter your number: '))
ognumber = number
final = 0
while (number > 0 ): 
    rem = number%10 
    final = final + (pow(rem,3))
    number = number//10

if (final == ognumber):
    print("This is an armstrong number :D")
else:
    print("This is not an armstrong number :(")
