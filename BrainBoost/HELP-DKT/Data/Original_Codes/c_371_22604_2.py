
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=[]
deleted_guest.append(guests[-1])
del guests[-1]
guests.insert(2,deleted_guest[0])
del guests[1]
print(deleted_guest[0])
print(guests)
 
