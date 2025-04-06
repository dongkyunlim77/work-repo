
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

a=(tuple(menu_list))
print(a)
print(a.sort(reverse=True))




