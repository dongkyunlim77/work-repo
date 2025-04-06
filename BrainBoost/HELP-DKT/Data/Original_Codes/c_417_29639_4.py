
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu_list=tuple(menu_list)
x=max(tuple(menu_list))
print(menu_list)
print(x)




