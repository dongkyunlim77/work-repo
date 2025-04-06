
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu_list=(tuple(menu_list))
print(menu_list)
menu_list.sort(reverse=True)
print(menu_list)





