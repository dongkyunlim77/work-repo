
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_gue
deleted_guest=guests.pop(-1)
guests.insert(2,deleteded_guest)
guests.pop(1)
print(deleted_guest)
print(guests)
 
