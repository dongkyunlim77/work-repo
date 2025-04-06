
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
delete_guest=guest[4]
print(delete_guest)
guests.pop()
guests.insert(2,delete_guest)
guests.pop(1) 
print(guests)
