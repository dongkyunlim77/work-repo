
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(-1)
guests.insert(2,guests)
del guests[1]
print(deleted_guest)
print (guests)
 
