
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu = tuple(menu_list)
print(menu)
print(max(menu))



