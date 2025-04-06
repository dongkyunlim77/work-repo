
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

price['lamb']=50
print( price['fish'])
price['fish']=100
del  price['noodles']
print( price)


