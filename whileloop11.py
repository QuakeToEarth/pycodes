#Write an program to input a number and count how many zeros are in there
number = int(input("Please enter you number here! ———> "))
count = 0
number = abs(number)
while (number > 0 ):
    rem = number%10
    if (rem ==0):
        count = count + 1
    number = number//10



#Tell user if it a duck number if it has Zero's or else not

if (count == 0):
    print("This is not a duck number")
else:
    print("This is a duck number")