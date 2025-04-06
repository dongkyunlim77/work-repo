
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
n=len(guests)
print(guests[0:n:3])
print(guests[-3:])

