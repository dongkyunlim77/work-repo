
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
print('hu ba')
del guests[1]
guests.insert(1,'hu ba')
deleted_obj = guests.pop(4)
print(guests)
 
