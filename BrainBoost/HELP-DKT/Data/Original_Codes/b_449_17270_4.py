
n = int(input())
c=1
def fact(a):
    for i in range (1, n+1):
        c*=i
    return c

print(fact(n))




