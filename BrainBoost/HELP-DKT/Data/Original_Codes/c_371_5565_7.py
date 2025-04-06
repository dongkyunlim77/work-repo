
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
dei=guests.pop()
print(dei)
guests.insert(2,dei)
guests.pop(1)
print(guests)