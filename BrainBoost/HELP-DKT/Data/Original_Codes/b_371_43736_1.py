
guests = ['Zhang san','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests.remove('Zhang san')
guests[1]=('Wang shi')
 
