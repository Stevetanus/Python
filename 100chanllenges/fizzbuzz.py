def fizzbuzz(num):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    if output:
        return output 
    else: return num
print(fizzbuzz(37))