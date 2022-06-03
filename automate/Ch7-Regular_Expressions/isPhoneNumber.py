def isPhoneNumber(number):
    if len(number) != 12:
        return False
    for i in range(0, 4):
        if not number[i].isdecimal():
            return False
    if number[4] != '-':
        return False
    for i in range(5, 8):
        if not number[i].isdecimal():
            return False
    if number[8] != '-':
        return False
    for i in range(9, 12):
        if not number[i].isdecimal():
            return False
    return True


print('0912-345-678 is a phone number:')
print(isPhoneNumber('0912-345-678'))
print('Steven Wang is a phone number:')
print(isPhoneNumber('Steven Wang'))

Messege = "Hi, I'm Steven. This is my phone number: 0912-345-366. Call me if urgent!"
for i in range(len(Messege)):
    chunk = Messege[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        print(i)
print('Done')
