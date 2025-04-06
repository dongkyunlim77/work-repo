
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.insert(4,'Hu qi')
guests.pop(0)
guests[1]='Wang shi'
 
