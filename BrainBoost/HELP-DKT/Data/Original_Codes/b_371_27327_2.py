
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
del guests[0]
guests[2]='Wang '
print(guests)
