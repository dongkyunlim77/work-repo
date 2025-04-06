
n = int(input())

def s(n):
    if (n==1):
       return 1
    s=n*s(n-1)
print(s)   





