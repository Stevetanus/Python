# Date-detection
import re
dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9]+)')


def transfer(day, month, year):
    if ((m in (4, 6, 9, 11)) & (d < 31)):
        valid = True
    elif (leap == True) & (m == 2) & (d < 30):
        valid = True
    elif (leap == False) & (m == 2) & (d < 29):
        valid = True
    elif ((m in (1, 3, 5, 7, 8, 10, 12)) & (d < 32)):
        valid = True
    else:
        valid = False
    return valid


while True:
    print('Enter a date, I will tell you if it is valid or not.')
    enterday = input()
    mo = dateRegex.findall(enterday)
    day, month, year = mo[0]
    d = int(day)
    m = int(month)
    y = int(year)
    if (((y % 4 == 0) & (y % 100 != 0)) | ((y % 4 == 0) & (y % 400 == 0))) == True:
        leap = True
    else:
        leap = False
    result = day + "/" + month + "/" + year
    if transfer(day, month, year) == True:
        print(result + " is a valid date.")
        break
    else:
        print("Please enter another valid date.")
