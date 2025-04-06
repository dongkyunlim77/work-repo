
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('hu qi')

guests.remove('wang wu')
guests.append('wang shi')
print(guests)
