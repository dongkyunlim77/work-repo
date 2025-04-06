
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
print(guests)
guests.pop(0)
print(guests)
guests[1]='Wang shi'
print(guests)
