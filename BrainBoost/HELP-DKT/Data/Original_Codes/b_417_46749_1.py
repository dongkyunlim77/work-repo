
menu_list = []
while True:
	try:
		food = input()
		menu_list.append(food)
	except:
		break

menu = tuple(menu_list)
print(menu)
if len(menu) == 4:
   print



