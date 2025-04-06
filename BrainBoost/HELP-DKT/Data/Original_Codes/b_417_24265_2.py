
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

print(tuple(menu_list))
print(max(menu_list))


