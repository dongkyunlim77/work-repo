
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break


tuple(seq(menu_list))
print(menu_list)
print(max(menu_list))



