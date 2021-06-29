age=int(input("Enter your age: "))

"""
if age>=18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')
"""

if age<13:
    if age<5:
        print('Infant')
    else:
        print('Child')
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior Citizen")
