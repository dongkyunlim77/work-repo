
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop()
guests.insert(0,deleted_guests)
del guests[0]
print(deleted_gues)
print(guests)
