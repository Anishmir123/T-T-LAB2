#An organization decides to give bonus to all its employee. Bonus of 5 % is given to male
worker and 10 % to female worker. WAP to enter salary of an employee and gender of
the employee. If the salary of person is less than 20000 then the employ gets an extra 5%
bonus on salary. Calculate the bonus that has to be given to the employee and display the
salary that employee will get.

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
