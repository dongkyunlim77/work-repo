
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['zhang san','li si','wang wu','zhao liu']
guests.append('hu qi')
guests.remove('zhang san','wang wu')
guests.insert()
print(guests)
