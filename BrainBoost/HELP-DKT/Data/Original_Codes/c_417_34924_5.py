
menu_dict = {}
while True:
	try:
		food = input()
		price = int(input())
		menu_dict[food]= price
	except:
		break

for key in menu_dict.keys():
    print(key)
for value in menu_dict.values():
    print(value)



