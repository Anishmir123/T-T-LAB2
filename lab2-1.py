//WAP to determine whether a person is eligible to cast vote or not. If he /she was not
eligible display how many years left to be eligible.

age = int(input("Enter your age: "))

if (age>=18):
    print("your are eligible")
else:
    print(18-age,"years to left")
