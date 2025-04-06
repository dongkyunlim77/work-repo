
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
del guests[1]
del guests[3]
guests.insert(1,'hu ba')
