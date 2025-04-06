
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests[-1]
guests.pop()
guests.insert(1,deleted_guest)
guests.pop(0)
print(deleted_guest)
print(guests)
