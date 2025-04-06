
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('hu qi')
guests.pop(0)
guests[2]='wang shi'
print(guests)
 
