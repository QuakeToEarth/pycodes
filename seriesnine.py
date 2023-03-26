#x/1 + x/3 + x/5 + x/7 ... n terms
x = int(input("Enter Numerator: "))
n = int(input("Enter Denominator: "))
sum = 0
for i in range(1,n+1,2):
    sum = sum + x/i
print(sum)