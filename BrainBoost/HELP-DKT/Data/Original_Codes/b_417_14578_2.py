
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu_list=tuple(menu_list)
x=mac(tuple)
print(menu_list)
print(x)




