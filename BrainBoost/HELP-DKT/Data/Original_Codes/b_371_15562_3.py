
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop(-1)
guests.insert(2,'delted_guest')
del guests[1]
print(deleted_guest)
print(guests)
