
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
a=guests.pop(4)
print(a)
print(guests)
