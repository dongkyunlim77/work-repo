
n = int(input())

def fact(n):
    if n==1:
        return n
    else:
        x=n*fact(n-1)
        return x
print(fact(n))





