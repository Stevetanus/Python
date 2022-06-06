# print
print("Hello", "Steven", end="\n")
print("I'm on the next line.", end=" | ")
print("I'm on the same line.")
# arithmatic
print(10//3) #整數商
# string
hello = "Hello WORLD"
print(hello.capitalize())
print(hello.count("OR"))
# order
print(ord('a'))
print(ord('A'))
# list
x = [4, True, "hi"]
x.extend([4,5,5,5,5])
print(x)
for i, element in enumerate(x):
    print(i, element)
# slice
sliced = x[0:len(x):2]
first3 = x[:3]
reverseX = x[::-1]
reverseHello = hello[::-1]
print(sliced)
print(first3)
print(reverseX)
print(reverseHello)
# set
y = set() # create empty set
s = {4,32,2,2}
s.add(5)
s.remove(2)
print(s)
print(2 in s)
# dictionary
dic = {"Name": "Steven", 31: 31, "Married": False}
for key, value in dic.items():
    print(key, value)
# comprehensions
com = [x for x in range(10)]
print(com)
module5 = [x for x in range(100) if x % 5 == 0]
print(module5)
# args
def func(*args,**kwargs):
    print(*args,kwargs)
pairs = [(1,2),(3,4)]
for pair in pairs:
    func(*pair, **{'pairs':pair})
# raise
# raise Exception("Bad!")
# try except
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally: 
    print("Close the file.")
# map
num_list = [1,2,3,4,5,6,7,8,9]
mp = map(lambda i: i*i, num_list)
mp2 = filter(lambda i:(i*i)==25, num_list)
print(list(mp))
print(list(mp2))