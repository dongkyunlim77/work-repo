
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(len(guests)-1)
guests.insert(3,deleted_guests)
del guests[1]
print(deleted_guests)
print(guests)
