
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guest.pop( )
print(deleted_guest)
guest.insert(2,deleted_guest)
del guest[1]
print(guest)

