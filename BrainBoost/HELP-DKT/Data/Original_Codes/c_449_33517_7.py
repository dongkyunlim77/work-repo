
n = int(input())

def fact(n):
    if n<2:
       return 1
    else:
         return n*fact(n-1)
print(fact(n))
    





