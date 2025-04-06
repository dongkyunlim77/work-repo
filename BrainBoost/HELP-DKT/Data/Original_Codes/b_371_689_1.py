
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests[-1]
guests.pop()
guests.insert(deleted_guest,2)
guests.pop(1)
print(deleted_guest)
print(guests)

 
