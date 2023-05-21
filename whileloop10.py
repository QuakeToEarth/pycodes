#Write an program to input a number and count how many zeros are in there
number = int(input("Please enter you number here! ———> "))
count = 0
while (number > 0):
    rem = number%10
    if (rem ==0):
        count = count + 1
    number = number//10

print(count)