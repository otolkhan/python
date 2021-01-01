from functools import reduce
import math
def CRT(n, a):
    sum=0
    prod=math.prod(n)
    print(f'product of m : {prod}')
    count=0
    for n_i, a_i in zip(n,a):
        count+=1
        z=prod//n_i
        print(f'z{count}={z}')
        sum += a_i* inverse_mod(z, n_i)*z
    return sum % prod
def inverse_mod(a, b):
    count=0
    count+=1
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    print(f"y{count} = {x1}")
    return x1
size=int(input("Enter Number of compisite value: "))
m=list(map(int,input("Enter values of m: ").strip().split()))[:size]
a=list(map(int,input("Enter values of a: ").strip().split()))[:size]
print(CRT(m,a))


