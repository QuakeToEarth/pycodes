# a = 24
# b = 36
# answer = pow(a,b)
# print(answer)

answer = 0
powerS= int(input("Enter Upper Range: "))
for i in range(1,powerS+1):
    answer = answer + pow(2,i)
print(answer)
