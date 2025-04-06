
guests = ['Zhang san','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests.pop()
guests.insert(1,'Wang shi')
print(guests)
