
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
a=guests.pop(4)
a
print(a)
print(guests)
