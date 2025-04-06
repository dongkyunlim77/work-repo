
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu_list1=tuple(menu_list)
max(menu_list1)
print(menu_list1)
print(max(menu_list1))




