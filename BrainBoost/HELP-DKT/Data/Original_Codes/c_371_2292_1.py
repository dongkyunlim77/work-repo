
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop()
print(deleted_guests)
guests.insert(2,deleted_guests)
del(guests[1])
print(guests)
