#input 10 numbers from the user & find the sum of even and odd number seperately
odd = 0
even = 0
for i in range(1,11):
    num = int(input("Enter Number: "))
    if (num%2 ==0):
        even = even + num
    else:
        odd = odd + num
print("odd numbers", odd)
print("even numbers", even)