
def factors(num):
    output_list=[]
    for i in range(1, num+1):
        if num % i ==0:
            output_list.append(i)
    print(output_list)

factors(10)