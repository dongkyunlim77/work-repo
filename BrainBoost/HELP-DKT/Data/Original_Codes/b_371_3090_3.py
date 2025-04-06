
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	

guests.pop()
deleted_guest=guests.pop(index)
guests.insert(2,deleted_guest)
print(deleted_guest)
print(guests)
 
