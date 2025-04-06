
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['Zhang san','Li si','Wang wu','Zhao liu']
guests.pop(0)
guests.insert(1,'Wang shi')
guests.pop(2)
guests.append('Hu qi')
print(guests)