
lower = int(input())
upper = int(input())
step = int(input())

date_list=list(range(lower,upper,step))

min_value=min(date_list)
max_value=max(date_list)
b=max(date_list)-min(date_list)
print(len(date_list))
print(b)                           


