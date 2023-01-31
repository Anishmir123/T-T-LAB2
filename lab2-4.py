
#WAP to find a given year is leap year.
year = int(input("Enter The Year: "))

if (year % 400 ==0) :
    print("This is leap year")
elif(year % 100==0):
    print("This is leap year ")
elif(year % 4 ==0):
    print("This is leap year")
else:
    print("This is not leap year")
