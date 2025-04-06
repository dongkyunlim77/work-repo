
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests.pop()
guests.insert(2,deleted_guest)
guests.remove(1)
print(deleted_guest)
pprint(guuests)
