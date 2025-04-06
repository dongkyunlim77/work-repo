
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
de=guests.pop()
print(de)
guests.insert(2,de)
guests.pop(1)
print(guests)
