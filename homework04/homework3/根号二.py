import math
a = 1
b = 2
def f(left,right):
    mid = (left + right) / 2
    if(abs(mid * mid - 2) < 0.000000000000001):
        return mid
    elif(mid * mid > 2):
        return f(left,mid)
    elif(mid * mid < 2):
        return f(mid,right)

c = f(1.25,2)
print(c)  #第一种（分治法)


def f():
    a = 1
    b = 2
    mid = (1 + 2) / 2 
    while(abs(mid * mid - 2) > 0.00000001):
        if(mid * mid > 2):
            b = mid
        else:
            a = mid
        mid = a/2 +b/2
    print(mid)

f()  #二分法

def f(x):
    a = 2
    x = 1
    for i in range(9999999):
        x = x + ((a/x) - x) / 2
    print(x)  #数列递推
