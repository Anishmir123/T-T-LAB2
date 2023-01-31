marks = int(input("Enter the marks: "))

if(marks >=90 and marks<=100):
    print("The grade is O",marks)
elif(marks >=80 and marks<=90):
    print("The grade is E",marks)
elif(marks >=70 and marks <=80):
    print("the grade is A",marks)
elif(marks >=60 and marks <=70):
    print("The grade is B",marks)
elif(marks >= 50 and marks <=60):
    print("The grade is C",marks)
else:
    print("Fail")