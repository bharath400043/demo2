''' Requirement : Find grade of a student based on below requirement.
marks >= 80 ==> A+ , 60-79 ==> A, 50-60==> B, 40-50 ==>C, Below 35 FAIL'''

marks = int(input("enter you marks : "))

if marks > 100 or marks < 0:
    print("Please Enter Valid Marks")
else:
    if marks >= 80:
        print("Grade A+")
    elif marks >= 60 and marks < 80:
        print("Grade A")
    elif marks >= 50 and marks < 60:
        print("Grade B")
    elif marks >= 40 and marks < 50:
        print("Grade C")
    else:
        print("FAIL")
