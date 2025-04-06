
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=[]
pop_guest=guests.pop[-1]
deleted_guest.append(pop_guest)
insert_guests=guests.insert(2,"deleted_guest")
deleted_guests=insert_guests.pop(1)
print(deleted_guest)

