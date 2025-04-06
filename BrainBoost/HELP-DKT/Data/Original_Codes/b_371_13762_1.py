
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests[-1]
guests.pop()
guests
guests.pop(1)
print(deleted_guest)
print(guests)

 
