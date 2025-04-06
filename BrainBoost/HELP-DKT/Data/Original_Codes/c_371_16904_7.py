
my_menu = []
while True:
	try:
		food = input()
		my_menu.append(food)
	except:
		break

print(my_menu[::3])



