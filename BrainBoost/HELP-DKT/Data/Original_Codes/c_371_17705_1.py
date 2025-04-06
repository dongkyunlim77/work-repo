
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
del guests[1]
deleted_obj = guests.pop(-1) 
guests.insert(1,deleted_obj)
print(deleted_obj)
print(guests)