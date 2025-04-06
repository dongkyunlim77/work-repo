
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests[2]='Wang shi'
del guests[0]
print(guests)
