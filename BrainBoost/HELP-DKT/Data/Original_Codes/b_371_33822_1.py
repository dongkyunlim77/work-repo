
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	

guests.append('Hu qi')
guests.remove('zhang san')
guests[1]='Wang shi'
print(guests)
