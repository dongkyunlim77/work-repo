
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('hu qi')
guests.pop(1)
guests[3]='wang shi'
print(guests)
 
