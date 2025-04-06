
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('hu qi')
guests.pop(1)
guests.remove('wang wu')
guests.insert(2,'ang shi')
print(guests)
