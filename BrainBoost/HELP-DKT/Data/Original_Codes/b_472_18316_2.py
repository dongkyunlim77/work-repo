
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

del menu_dict[2,3]
print(menu_dict['fish'])
print(menu_dict)




