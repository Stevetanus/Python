import re

chars = 'bat'
chars2 = re.escape(chars)


def regex_strip(s, chars=None):

    if chars:
        trim = '[' + re.escape(chars) + ']*'
    else:
        trim = r'\s*'

    return re.fullmatch(f"{trim}(.*?){trim}", s).group(1)


s1 = 'batmanbat'
s2 = '      batmanbat'
s3 = 'batmanbat      '
s4 = 'tabBatmanabt'
s5 = 'tabatbBatwomentabbat'


chars = 'bat'
chars2 = ''
regex_strip(s1, chars)
regex_strip(s2, chars)
regex_strip(s2, chars2)
regex_strip(s2,)
regex_strip(s3, chars)
regex_strip(s4, chars)
regex_strip(s5, chars)
