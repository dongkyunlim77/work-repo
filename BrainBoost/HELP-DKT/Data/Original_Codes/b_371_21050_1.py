
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('hu qi')
guests.remove('zhang san')
guests[2]='wang shi'
print(guests)

 
