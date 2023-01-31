#WAP to read numbers till _1 is encountered. Find the positive and negative numbers
entered by user.
num = int(input("Enter the number: "))

pos=0
nega=0

while num!=-1:
    if(num>0):
        pos=pos+1
    elif(num<0):
        nega=nega+1
    else:
        num=0
print("Positive number are: ",pos)
print("Negative number are:",nega)
