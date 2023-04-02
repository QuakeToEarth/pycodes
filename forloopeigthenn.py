#input 10 numbers and find the maximum amoung them
min = 99999999999999999999999999999999999999999
for i in range(1,11):
    num = int(input("Enter Number: "))
    if (min > num):
        min = num
    
print("The lowest Number is : ", min)