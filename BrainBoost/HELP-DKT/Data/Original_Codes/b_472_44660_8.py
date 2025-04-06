
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

del menu_dict['noodles']
insert.menu_dict['lamb']=menu_dict
menu_dict['lamb']=50
print(menu_dict['fish'])
menu_dict['fish']=100
print(menu_dict)




