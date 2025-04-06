
n = int(input())

def fact(n):
    a=0
    b=1
    for i in range(n):
        a=a+i
        b*=a
    return b
print(fact(n))





