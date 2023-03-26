#1/2 + 3/4 + 5/6 + 7/8 ... 19/20
sum = 0
for i in range(1,21,2):
    sum = sum + i/(i+1)
print(sum)

    