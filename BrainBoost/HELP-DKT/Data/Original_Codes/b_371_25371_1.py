
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guest[-1]
guests.pop()
guests.insert(2,deleted_guest)
L.pop(1)
print(deleted_guest)
print(guests)
