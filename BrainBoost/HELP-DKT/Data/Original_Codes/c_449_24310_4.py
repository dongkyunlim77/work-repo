
n = int(input())

def fact(n):
    if (n<0):
       a=None
    else:
         i=1
         if (n==0 or n==1):
             a=n
         else:
             a=1
             while (i<=n):
                  a=a*i
                  i=i+1
    return a
   

print (fact(n))


