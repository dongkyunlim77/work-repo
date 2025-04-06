
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest = []
deleted_guest.append()
guests.pop(0)
guests[1] = 'Wang shi'
guests.append('Hu qi')
print(guests)
 
