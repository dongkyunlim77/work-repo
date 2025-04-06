
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted=guests[-1]
print(deleted)
guests[1]=deleted
guests.pop()
print(guests)
 
