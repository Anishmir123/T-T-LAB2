num = int(input("Enter the number n:"))
fact = 1
sum=0
for i in range(1,num+1):
    fact *= i
    sum = sum + i/fact
print("sum is",sum)
