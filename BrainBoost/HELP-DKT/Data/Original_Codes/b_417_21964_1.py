
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

tuple(menu_list)
print(menu_list)
max1=max(menu_list)
print(max1)




