
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
del guest[4]
del guest[1]
guests.insert(1,'hu ba')
