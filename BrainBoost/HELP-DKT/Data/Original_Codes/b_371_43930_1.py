
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_obj=guests.pop(-1)
guests.insert(2,'deleted_guest')
del guests[1]
print(deleted_obj)
print(guests)
