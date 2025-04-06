
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests.pop(0)
guests.pop(1)
guests.insert(1,'Wang shi')
print(guests)
