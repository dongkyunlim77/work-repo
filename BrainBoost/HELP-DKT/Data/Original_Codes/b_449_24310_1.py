
n = int(input())

def fact(n):
    if (n<0):
       a=None
    else:
         i=0
         if (n==0 or n==1):
             a=n
         else:
             a=1
             i=i+1
             while (i<=n):
                  a=a*i
    return a
   

print (fact(n))


