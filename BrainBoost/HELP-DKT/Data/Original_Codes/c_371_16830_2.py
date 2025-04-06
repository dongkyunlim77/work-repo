
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
d=guests.pop(-1)
guests.insert(2,d)
guests.pop(1)
print(d)
print(guests)

