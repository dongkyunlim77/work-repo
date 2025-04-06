
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_obj=guests.pop(0)
print(deleted_obj)
guests.insert(2,'deleted_obj')
del guests[1]
print(gusets)
 
