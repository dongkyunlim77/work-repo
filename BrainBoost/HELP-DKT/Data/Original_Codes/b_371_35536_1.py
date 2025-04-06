
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
del guests[0]
guests[1]='Wang shi'
print(guests)
