
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

menu_dict['lamb']=50
print(menu['lish'])
menu_dict['lish']=100
del menu['noodles']    
print(menu_dict)         

