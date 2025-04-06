
guests = ['Zhang san','Li si','Wang wu','zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
del gus
guests[2]=('Wang shi')
print(guests)
