
x = int(input())

result=[]
def zhi(x):
    for i in range(2,x):
        if x%i==0:
            return False
        
    return True

def sb(x):
    x=int(x)
    if zhi(x)==True:
        result.append(x)
        return
    else:
        for i in range(2,x):
            if x%i==0:
                x=x/i
                result.append(i)
                break
        sb(x)
                

        
sb(x)
                




print(x,'=','*'.join(map(str,result)))


