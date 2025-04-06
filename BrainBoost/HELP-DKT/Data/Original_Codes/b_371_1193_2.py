
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['Zhang san','Li si','Wang wu','Zhao liu']
guests.append('Hu qi')
guests.pop(0)
guests[2]='Wang shi'
