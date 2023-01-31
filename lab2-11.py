num = int(input("Enter the number: "))
count=0
i=1
while i<=num:
    if(num%i==0):
        count=count+1

    i=i+1
if count==2:
    print("This is Prime NUmber")
elif count>2:
    print("This is Composite")
else:
    print("neither number prime and composite")
