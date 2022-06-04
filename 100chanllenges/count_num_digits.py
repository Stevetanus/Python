
def count_num_digits(input_string):
    count = 0
    for i in input_string:
        if i.isdigit() == True:
            count +=1
    return count

