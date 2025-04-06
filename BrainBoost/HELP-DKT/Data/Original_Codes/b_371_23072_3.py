
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests.pop(0)
guests[1]='Wang Shi'
print(guests)
 
