
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guest(4)
guests.pop()
print(deleted_guest)
guest.insert(2,deleted_guest)
guest.pop(1)
print(guest)
 
