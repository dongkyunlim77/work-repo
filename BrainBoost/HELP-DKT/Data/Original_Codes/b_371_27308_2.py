
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop()
guests.insert(2,delete_guest)
guests.pop(1)


