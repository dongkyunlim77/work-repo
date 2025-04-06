
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

print(tuple(menu_list))
sorted(menu_list)
print([0])


