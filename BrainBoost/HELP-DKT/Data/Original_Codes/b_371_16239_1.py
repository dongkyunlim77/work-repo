
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(len(guests)-1)
guests.insert(2)
del guests[1]
print(guests)
