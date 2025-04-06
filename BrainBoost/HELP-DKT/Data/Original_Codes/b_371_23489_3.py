
guests = ['Zhang San','Li si','Wang wu','Zhao liu']

while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop(3)
guests.insert(2,'Zhao liu')
del guests[1]
print(deleted_guests)
print(guests)

