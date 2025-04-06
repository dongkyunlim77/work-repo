
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
del guests[1]
print(guests)
 
