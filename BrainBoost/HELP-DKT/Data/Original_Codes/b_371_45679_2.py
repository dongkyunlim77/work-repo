
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(-1)
print(deleted_guests)
print(guests)
 
