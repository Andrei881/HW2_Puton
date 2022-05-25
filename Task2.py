from random import randint
import math

def numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def mult_pairs(mylist):
    return [list[i] + list[-i - 1] for i in range(math.ceil(len(list)/2))]

n = 9
frst = 1
last = 10

list = numbers(n, frst, last)
print(list)
print(mult_pairs(list))
