"""
Requirement: Find out maximum number below. using if elif else logic
"""

a = 10
b = 30
c = 20

if a > b and a > c:
    print("The greater value : {0}".format(a))
elif b > a and b > c:
    print("The greater value : {0}".format(b))
else:
    print("The greater value : {0}".format(c))

"""
students must met below required conditions to promote to higher class
1. 65 percent and above attendance
2. 50 percent and above marks
3. no fees due
"""

attendance = float(input('enter the attendance percent % : '))
marks_percent = float(input('enter the marks percent % : '))
fees_due = input('enter fees due yes or no : ')
if attendance < 0 or attendance > 100:  # validation 1
    if marks_percent < 0 or marks_percent > 100:
        print('enter valid attendance percent and marks percent')
    else:
        print('enter valid attendance percent')
else:
    if marks_percent < 0 or marks_percent > 100:    # validation 2
        print('enter valid marks percent')
    else:
        if attendance >= 65:
            print('first condition met')
            if marks_percent >= 50:
                print('second condition met')
                if fees_due == 'no':
                    print('third condition met')
                    print('student met all the required conditions and promoted to higher class')
                else:
                    print('student did not met the third condition and not being promoted to higher class ')
            else:
                if fees_due == 'no':
                    print('student did not met the second condition and not being promoted to higher class')
                else:
                    print('student did not met the second and third condition and not being promoted to higher class')
        else:
            if marks_percent >= 50:
                if fees_due == 'no':
                    print('student did not met the first condition and not being promoted to higher class ')
                else:
                    print('student did not met the first and third conditions and not being to promoted higher class')
            else:
                if fees_due == 'no':
                    print('student did not met the first and second condition and not being promoted to higher class')
                else:
                    print('student did not met all the required conditions  and not being promoted to higher class')
