
n = int(input())

def fact(n):
    a=0
    b=1
    for i in range(1,n+1):
        a=a+1
        b*=a
    return b
print(fact(n))





