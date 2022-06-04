def sum_pos_divisor(num):
    sumDivisor = 0
    for i in range(1, num+1):
        if num % i ==0:
            sumDivisor += i
    if sumDivisor-num == num:
        return True
    else: return False
