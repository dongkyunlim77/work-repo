
x = int(input())

result = []
for j in range(int(x/2)+1):
    for i in range(2, x+1):
        t = x % i
        if t == 0:
           result.append(i)
           x = x//i 
           break
for m in range(0,len(result)):
    x=x*int(result[m])





print(x,'=','*'.join(map(str,result)))


