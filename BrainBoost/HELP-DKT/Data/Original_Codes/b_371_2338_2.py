
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop(-1)
print(deleted_guest)
guests=guests.insert(2,deleted_guest)
print(guests.pop(1))
 
