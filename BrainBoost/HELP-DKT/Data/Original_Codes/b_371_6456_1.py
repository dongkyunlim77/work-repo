
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop()
print(deleted_guest)
guests.insert(1,deleted_guest)
guests.pop(1)
print(guests)
