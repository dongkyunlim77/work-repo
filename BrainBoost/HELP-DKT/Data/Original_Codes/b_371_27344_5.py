
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop(-1)
print(deleted_guest)
deleted_guest=str(deleted_guest)
guests.insret(2,deleted_guest)
del guests[1]
print(guests)
