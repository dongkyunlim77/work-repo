
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break


tuple(menu_list)
print(tuple(menu_list))
print(max(menu_list))



