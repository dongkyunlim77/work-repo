
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop(0)
guests.insert(2,deleted_guest)
guests.remove(0)
print(deleted_guest)
print(guests)
