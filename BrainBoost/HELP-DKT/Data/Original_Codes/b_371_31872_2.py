
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_obj=guest.pop(-1)
guest.insert(2,deleted_guest)
guest.pop(1)
print(deleted_guest)
print(guests)
