
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.pop(0)
guests.insert(1,'Wang shi')
guests.pop(2)
guests.append('Hu qi')
print