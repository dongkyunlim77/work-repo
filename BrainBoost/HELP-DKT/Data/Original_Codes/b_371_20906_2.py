
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.pop(0)
guests.pop(1)
guests.append('Hu qi')
guests.insert(1,'wang shi')
