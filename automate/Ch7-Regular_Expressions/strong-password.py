import re
# at least eight characters long
eightRegex = re.compile(r'\w{8,}')
# contains both uppercase and lowercase characters
upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
# has at least one digit
digitRegex = re.compile(r'[0-9]')
validations = {}


def strongPassword(password):
    def regexToDictionary(Regex, password, key):

        if Regex.search(password) == None:
            validations.setdefault(key, 0)
        else:
            validations.setdefault(
                key, len(Regex.search(password).group()))
    regexToDictionary(eightRegex, password, 'eightwords')
    regexToDictionary(upperRegex, password, 'uppercase')
    regexToDictionary(lowerRegex, password, 'lowercase')
    regexToDictionary(digitRegex, password, 'digit')

    if 0 in validations.values():
        valid = False
    else:
        valid = True
    return valid


while True:
    print('Enter your password, with eight, uppercase, lowercase words and at least one digit.')
    yourPassword = str(input())

    if strongPassword(yourPassword) == True:
        print('Valid password!!!')
        break
    else:
        print('Please enter another password')
        for k, v in validations.items():
            if v == 0:
                print('You need to enter a password with ' + k + '.')
    validations = {}
