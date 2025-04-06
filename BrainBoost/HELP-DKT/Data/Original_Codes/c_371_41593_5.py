
my_menu = []
while True:
	try:
		food = input()
		my_menu.append(food)
	except:
		break

L=my_menu[0::3]
A=my_menu[-3::]
print(L)
print(A)



