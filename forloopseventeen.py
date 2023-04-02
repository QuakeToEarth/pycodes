#input 10 numbers and find the maximum amoung them
max = 0 
for i in range(1,11):
    num = int(input("Enter Number: "))
    if (num > max):
        max = num
    
print("The highest Number is : ", max)