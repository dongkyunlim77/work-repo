
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['Zhang san','Li si','Wang wu','zhao liu']
guests.append('Hu qi')
guests.pop(1)
guests.remove('Wang wu')
guests.insert(2,'Wang shi')
