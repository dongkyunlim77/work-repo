
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

del menu_dict['noodles']
print(menu_dict['fish'])
print(menu_dict)




