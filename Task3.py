from random import uniform

def real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(num):
    num = [round(x - int(x), 2) for x in (num)]
    return max(num) - min(num)

n = 5
frst = 1
last = 10
num = real_nums(n, frst, last)

print (num)