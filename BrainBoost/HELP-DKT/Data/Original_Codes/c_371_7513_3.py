
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_obj=guests.pop()
guests.insert(2,deleted_obj)
guests.pop(1)
print(deleted_obj)
print(guests)
