
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=[]
deleted_guest.append(guests.pop(-1))
guests.insert(2,"deleted_guest")
deleted_guests=guests.inspop(1)
print(deleted_guest)

