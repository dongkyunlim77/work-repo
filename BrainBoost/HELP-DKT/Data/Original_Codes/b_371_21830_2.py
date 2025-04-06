
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest = guests.pop()
print(delguest)
guests.insert(2,deleted_guest)
print(guests)
