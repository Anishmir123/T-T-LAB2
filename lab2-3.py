sal = int(input("Enter your salary: "))
gen = input("Enter your age: ")

if gen=="m":
    bonus=0.5*sal
elif gen=="f": 
    bonus=0.10*sal

if (sal<20000):
    bonus=bonus+0.05*sal

sal=sal+bonus

print("Now salary is: ",sal)
