
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(-1)
guests.insert(2,deleted_guests)
del guests[1]
print(deleted_guests)
print(guests)



 
