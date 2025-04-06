
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_obj = guests.pop()
guests.insert(1,deleted_obj)
del guests[2]
print(deleted_obj)
print(guests)
