
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

a=(tuple(menu_list))
print(a)
menu_list.sort(reverse=True)
print(menu_list[0])





