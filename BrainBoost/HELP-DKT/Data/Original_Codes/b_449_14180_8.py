n = int(input())
print('yes'+str(n))
def fact(n):
	i=1
	m=1
	while(i <= n):
		m=m*i
		i=i+1
	return m
print(fact(n))
