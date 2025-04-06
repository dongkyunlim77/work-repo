
s = int(input())

def S(s):
    if (s==1):
        return 1
    d=s*S(s-1)
    return d
print(S(s))

