#Neon number
number = int(input('Enter your number please :) '))
final = 0
ognumber = number
sqaure = pow(number,2)
while (sqaure > 0):
    rem = sqaure%10
    print(rem)
    final = final + rem 
    sqaure = sqaure//10

if (final == number):
    print(number, "is a neon number")
else:
    print(number, "isn't a neon number")


