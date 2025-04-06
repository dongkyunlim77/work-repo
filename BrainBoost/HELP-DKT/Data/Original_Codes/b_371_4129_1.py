
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
print(guests[-1])
 
