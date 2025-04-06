
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
delguest = guests.pop()
print(delguest)
print(guests)
