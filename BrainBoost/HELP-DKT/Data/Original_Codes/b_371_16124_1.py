
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.pop(0)
guests[1] = 'Wang shi'
guests.append('Hu qi')
print(guests)
 
