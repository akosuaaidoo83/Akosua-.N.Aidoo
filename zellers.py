name= input("Enter your name")
year = int(input('Enter year(e.g. 2015): '))
month = int(input('Enter month(1-12): '))
day = int(input('Enter day of the month(1-31): '))
if month == 1:
    month = month + 12
    year = year - 1
    
elif month == 2:
    month = month + 12
    year = year - 1

print("{} was born on {}".format(name,day))
century = (year // 100)
century_year = (year % 100)

week= (day + ((26 * (month + 1)) // (10)) + century_year + ((century_year) // \
    (4)) + ((century) // (4)) + (5 * century)) % 7

if week == 0:
    print('Your name is {}, and you were born on Saturday'.format(name))
elif week == 1:
    print('Your name is {},and you were born on Sunday'.format(name))
elif week == 2:
    print(' Your name is {},and you were born on Monday'.format(name))
elif week == 3:
    print('Your name is {},and you were born on Tuesday'.format(name))
elif week == 4:
    print('Your name is {},and you were born on Wednesday'.format(name))
elif week == 5:
    print('Your name is {},and you were born on  Thursday'.format(name))
elif week == 6:
    print('Your name is {},and you were born on  Friday'.format(name))

