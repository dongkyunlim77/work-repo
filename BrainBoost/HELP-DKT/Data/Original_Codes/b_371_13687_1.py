
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
if 'zhao liu' in guests:
    guests.append('hu qi')
if 'zhang san' in guests:
    guests.remove('zhang san')
if 'wang wu' in guests:
    guests['wang wu']='wang shi'
print(guests)
