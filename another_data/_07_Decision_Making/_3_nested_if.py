''' Requirement : Check whether entered year is leap year or not '''

year = int(input(" enter year for checking : "))

print("**** First method ***")

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("It's a Leap Year")
    else:
        print("Not a Leap Year")
else:
    pass


print("*** Second method ***")

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Entered year is a leap year")
else:
    print("not a leap year")

print("*** Third method ***")

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
