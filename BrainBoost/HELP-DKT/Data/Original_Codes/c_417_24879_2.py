
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu_tuple = tuple(menu_list)
print(menu_tuple)

max_element = max(menu_tuple)
print(max_element)




