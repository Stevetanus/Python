import math
def decimal_part(num):
    if num.is_integer() == True:
        return 'INTEGER'
    else:
        return round(num - int(num),2)