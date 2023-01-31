#WAP to find whether the given number is an Amstrong number or not.

num = int(input("Enter The Number: "))
sum =0
temp=num
while temp<0:
  digit=temp%10
  cube=digit**3
  sum=sum+cube
  fd=cube // 10

if (sum==num):
    print("Number are Armstrong Number")
else:
    print("Number are Armstrong Number")
